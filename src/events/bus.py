import asyncio
import inspect
from typing import Type, Dict, List, Callable, Awaitable, Union, Any, TypeVar, Generic
import logging
from src.events.base import DomainEvent

logger = logging.getLogger(__name__)

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
        handlers = self._subscribers.get(type(event), [])
        sync_tasks = []
        async_tasks = []

        for handler in handlers:
            if inspect.iscoroutinefunction(handler):
                async_tasks.append(handler(event))
            else:
                sync_tasks.append(handler)

        # Run sync handlers with error logging
        for handler in sync_tasks:
            try:
                logger.exception(
                    "Sync handler failed for event %s", event, exc_info=True)
            except Exception:
                logger.exception("Sync handler failed for event %s", event)
                # Option: continue or re-raise depending on criticality

        # Run async handlers with error logging
        if async_tasks:
            try:
                asyncio.run(self._run_async_handlers(async_tasks))
            except Exception:
                # _run_async_handlers returns exceptions as values, so this shouldn't happen
                # but guard anyway
                logger.exception("Error during async handler execution")

    async def _run_async_handlers(self, coros):
        """Helper to run a list of coroutines concurrently."""
        await asyncio.gather(*coros, return_exceptions=True)


event_bus = EventBus()


