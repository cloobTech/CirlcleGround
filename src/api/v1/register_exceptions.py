from fastapi import FastAPI
from fastapi import HTTPException

from src.core.exceptions import (
    UserAlreadyExistsError,
    InvalidCredentialsError,
    PermissionDeniedError,
    DatabaseConnectionError,
    EntityNotFound
)

from src.api.v1.exception_handler import (
    user_already_exists_handler,
    entity_not_found_handler,
    invalid_credentials_handler,
    permission_denied_handler,
    unique_violation_handler,
    token_expired_handler,
    duplicate_entry_handler,
    invalid_token_handler,
    http_exception_handler,
    internal_server_error_handler,
    database_connection_error_handler,
    invalid_coverage_selection
)


def register_exception_handlers(app: FastAPI):

    # User-related
    app.add_exception_handler(UserAlreadyExistsError,
                              user_already_exists_handler)
    app.add_exception_handler(InvalidCredentialsError,
                              invalid_credentials_handler)
    app.add_exception_handler(PermissionDeniedError, permission_denied_handler)
    app.add_exception_handler(EntityNotFound, entity_not_found_handler)
    

    # Token-related

    # Database
    app.add_exception_handler(DatabaseConnectionError,
                              database_connection_error_handler)

    # HTTPException
    app.add_exception_handler(HTTPException, http_exception_handler)

    # Fallback
    app.add_exception_handler(Exception, internal_server_error_handler)
