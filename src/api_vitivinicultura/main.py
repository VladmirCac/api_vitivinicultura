from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from api_vitivinicultura.exceptions import handlers
from api_vitivinicultura.routers.users import router as user_router
from api_vitivinicultura.routers.auth import router as login_router
from api_vitivinicultura.routers.vitivinicultura import router as vitivinicultura_router
from api_vitivinicultura.core.config import settings

app = FastAPI(**settings.API_SETTINGS)

app.include_router(login_router)
app.include_router(user_router)
app.include_router(vitivinicultura_router)

app.add_exception_handler(RequestValidationError, handlers.validation_exception_handler)
app.add_exception_handler(HTTPException, handlers.http_exception_handler)
app.add_exception_handler(Exception, handlers.generic_exception_handler)