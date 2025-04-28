from pydantic import BaseModel
from typing import List

class ErrorResponse(BaseModel):
    errors: List[str]