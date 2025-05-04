from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from api_vitivinicultura.core.database import get_db
from api_vitivinicultura.models.user import User
from api_vitivinicultura.schemas.user import UserCreate, UserCreateResponse, UserResponse, UserUpdate
from api_vitivinicultura.schemas.error import ErrorResponse
from api_vitivinicultura.schemas.auth import TokenData
from api_vitivinicultura.core.security import get_current_user, hash_password


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
    response_model=list[UserResponse],
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

@router.put(
    "/{user_id}",
    response_model=UserCreateResponse,
    responses={
        200: {"description": "User updated successfully."},
        404: {"model": ErrorResponse},
        400: {"model": ErrorResponse},
        422: {"model": ErrorResponse}
    }
)
def update_user(
    user_id: int,
    user_update: UserUpdate,
    db: Session = Depends(get_db),
    current_user: TokenData = Depends(get_current_user)
):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=["User not found."]
        )

    if user_update.user_name:
        existing_user = (
            db.query(User)
            .filter(User.user_name == user_update.user_name)
            .filter(User.id != user_id)
            .first()
        )
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=["A user with that username already exists."]
            )
        user.user_name = user_update.user_name
    
    if user_update.password:
        user.password = hash_password(user_update.password)
    if user_update.obs is not None:
        user.obs = user_update.obs

    db.commit()
    db.refresh(user)

    return {"id": user.id, "message": "User updated successfully!"}

@router.delete(
    "/{user_id}",
    response_model=UserCreateResponse,
    responses={
        200: {"description": "User deleted successfully."},
        404: {"model": ErrorResponse},
    }
)
def delete_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: TokenData = Depends(get_current_user)
):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=["User not found."]
        )

    db.delete(user)
    db.commit()

    return {"id": user.id, "message": "User deleted successfully."}

