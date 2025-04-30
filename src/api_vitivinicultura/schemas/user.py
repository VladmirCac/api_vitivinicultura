from pydantic import BaseModel, Field

class UserCreate(BaseModel):
    user_name: str = Field(..., example="UserName")
    password: str = Field(..., example="UserPassword")
    obs: str | None = Field(None, example="Optional observation about the user")

class UserUpdate(BaseModel):
    user_name: str | None = Field(None, example="NewUsername")
    password: str | None = Field(None, example="NewPassord")
    obs: str | None = Field(None, example="New user observation")

class UserCreateResponse(BaseModel):
    id: int
    message: str

class UserResponse(BaseModel):
    id: int
    user_name: str
    obs: str | None = None
    
    #CLASSE UTILIZADA PARA converter um objeto ORM diretamente em um Pydantic model
    class Config:
        from_attributes  = True