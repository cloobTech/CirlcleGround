from src.storage import db
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends, HTTPException, status
from src.models.user import User
from fastapi.security import OAuth2PasswordBearer
from src.unit_of_work.unit_of_work import UnitOfWork
from src.auth.jwt import decode_access_token
from src.auth.services import AuthService


oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/api/v1/routes/user_routes/login')

async def get_session():
    async with db.get_session() as session:
        yield session

def get_uow(session: AsyncSession = Depends(get_session)):
    return UnitOfWork(session)

def get_auth_service(uow: UnitOfWork = Depends(get_uow)):
    return AuthService(uow)

async def get_current_user(
    token: str = Depends(oauth2_scheme),
    uow: UnitOfWork = Depends(get_uow),
) -> User:
    credential_exceptions = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate token",
        headers={"WWW-Authenticate": "Bearer"},
    )

    payload = decode_access_token(token, credential_exceptions)
    user = await uow.user_repo.get_by_id(payload)
    if not user:
        raise credential_exceptions

    return user
