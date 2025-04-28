from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: int | None = None
    user_name: str | None = None

class LoginInput(BaseModel):
    user_name: str
    password: str