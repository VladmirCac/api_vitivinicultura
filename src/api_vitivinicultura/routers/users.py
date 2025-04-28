from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from api_vitivinicultura.core.database import get_db
from api_vitivinicultura.models.user import User
from api_vitivinicultura.schemas.user import UserCreate, UserCreateResponse, UserResponse
from api_vitivinicultura.schemas.error import ErrorResponse
from api_vitivinicultura.core.security import get_current_user, hash_password
from api_vitivinicultura.schemas.auth import TokenData
from typing import List

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post(
    "/", 
    response_model=UserCreateResponse,
    status_code=201,
    responses={
        201: {"description": "User created successfully."},
        400: {"model": ErrorResponse},
        422: {"model": ErrorResponse},
    }
)
def create_user(user: UserCreate, db: Session = Depends(get_db)):

    user_exist = db.query(User).filter(User.user_name == user.user_name).first()

    if user_exist:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail= ["There is already a registered user with that name."]
        )

    new_user = User(
        user_name=user.user_name,
        password=hash_password(user.password),
        obs=user.obs
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"id": new_user.id, "message": "User created successfully!"}


@router.get(
    "/", 
    response_model=List[UserResponse],
    responses={
        200: {"description": "List of all users"},
        422: {"model": ErrorResponse},
    }
)
def list_users(
    current_user: TokenData = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    users = db.query(User).all()
    return users