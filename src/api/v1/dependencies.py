from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends, HTTPException, status
from src.storage import db
from src.enums.enums import UserRole
from src.models.user import User
from src.unit_of_work.unit_of_work import UnitOfWork
from src.auth.jwt import decode_access_token
from src.auth.services import AuthService
from src.services.space_services import SpaceService
from src.services.user_services import UserService
from src.services.location_service import LocationService
from src.utils.token_utils import TokenUtils


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")

async def get_session():
    async with db.get_session() as session:
        yield session

def get_uow(session: AsyncSession = Depends(get_session)):
    return UnitOfWork(session)

def get_user_service(uow: UnitOfWork = Depends(get_uow)):
    return UserService(uow)

def get_auth_service(uow: UnitOfWork = Depends(get_uow)):
    return AuthService(uow)

def get_space_service(uow: UnitOfWork = Depends(get_uow)):
    return SpaceService(uow)

def get_location_service(uow: UnitOfWork = Depends(get_uow)):
    return LocationService(uow)

def get_token_utils(uow: UnitOfWork = Depends(get_uow)):
    return TokenUtils(uow)


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
    user_id = payload.get("sub")
    if user_id is None:
        raise credential_exceptions
    user = await uow.user_repo.get_by_id(user_id)
    if not user:
        raise credential_exceptions
    return user


async def require_admin(user: User = Depends(get_current_user)):
    if user.role != UserRole.ADMIN:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="admin access required"
        )
    return user

async def require_super_admin(user: User = Depends(get_current_user)):
    if user.role != UserRole.SUPER_ADMIN:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="super_admin access required"
        )
    return user