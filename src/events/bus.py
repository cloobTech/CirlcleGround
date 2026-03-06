import asyncio
import inspect
from typing import Type, Dict, List, Callable, Awaitable, Union, Any, TypeVar, Generic
from src.events.base import DomainEvent

E = TypeVar("E", bound=DomainEvent)

Handler = Union[
    Callable[[E], Awaitable[Any]],   # async handler
    Callable[[E], Any]               # sync handler
]


class EventBus(Generic[E]):
    def __init__(self):
        self._subscribers: Dict[Type[E], List[Handler]] = {}

    def subscribe(self, event_type: Type[E], handler: Handler):
        self._subscribers.setdefault(event_type, []).append(handler)

    async def publish(self, event: E):
        handlers = self._subscribers.get(type(event), [])
        tasks = []

        for handler in handlers:
            if inspect.iscoroutinefunction(handler):
                tasks.append(asyncio.create_task(handler(event)))
            else:
                loop = asyncio.get_running_loop()
                tasks.append(loop.run_in_executor(None, handler, event))

        await asyncio.gather(*tasks, return_exceptions=True)

    def publish_sync(self, event: E):
        """Synchronously publish an event to all subscribers.

        Use this in non‑async contexts (e.g., Celery tasks, scripts).
        """
        handlers = self._subscribers.get(type(event), [])
        sync_tasks = []
        async_tasks = []

        for handler in handlers:
            if inspect.iscoroutinefunction(handler):
                async_tasks.append(handler(event))
            else:
                sync_tasks.append(handler)

        # Run sync handlers directly (they are just Python functions)
        for handler in sync_tasks:
            handler(event)

        # Run async handlers by creating a new event loop and running them
        if async_tasks:
            try:
                # Try to get the running loop – if one exists, we can't use asyncio.run()
                loop = asyncio.get_running_loop()
                # We are already in an async context – this method should not be called
                # from sync code if a loop is running. Fallback: run in a thread?
                # For simplicity, we'll raise a clear error.
                raise RuntimeError(
                    "publish_sync called from an async context. "
                    "Use await publish() instead."
                )
            except RuntimeError:
                # No running loop – safe to use asyncio.run()
                asyncio.run(self._run_async_handlers(async_tasks))

    async def _run_async_handlers(self, coros):
        """Helper to run a list of coroutines concurrently."""
        await asyncio.gather(*coros, return_exceptions=True)


event_bus = EventBus()
