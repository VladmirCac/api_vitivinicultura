from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from api_vitivinicultura.core.database import get_db
from api_vitivinicultura.models.user import User
from api_vitivinicultura.schemas.auth import Token, LoginInput
from api_vitivinicultura.core.security import create_access_token, verify_password

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.post(
    "/login",
    response_model=Token,
    summary="Login and retrieve Bearer JWT token",
    description="Authenticate a user using JSON body and receive a Bearer JWT token for accessing protected routes.",
    responses={
        200: {"description": "Login successfully."},
        401: {"description": "Invalid username or password."},
        422: {"description": "Validation Error."}
    }
)
def login_json(login_input: LoginInput, db: Session = Depends(get_db)):
    # Buscar usuário pelo nome
    user = db.query(User).filter(User.user_name == login_input.user_name).first()

    if not user or not verify_password(login_input.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Prepara os dados para o token
    token_data = {
        "sub": user.user_name,
        "id": user.id
    }
    access_token = create_access_token(data=token_data)

    return {"access_token": access_token, "token_type": "bearer"}