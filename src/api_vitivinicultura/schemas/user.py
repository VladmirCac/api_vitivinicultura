from pydantic import BaseModel, Field

class UserCreate(BaseModel):
    user_name: str = Field(..., example="vladmir_cac", description="Username for the user")
    password: str = Field(..., example="strongpassword123", description="User password")
    obs: str | None = Field(
        default=None,
        example="This user is an admin",
        description="Optional observation about the user"
    )

class UserCreateResponse(BaseModel):
    id: int
    message: str

class UserResponse(BaseModel):
    id: int
    user_name: str
    obs: str | None = None # campo opcional

    class Config:
        from_attributes  = True