from fastapi import FastAPI
from fastapi import HTTPException
from fastapi.exceptions import RequestValidationError
from api_vitivinicultura.exceptions import handlers
from api_vitivinicultura.routers.users import router as user_router
from api_vitivinicultura.routers.auth import router as login_router

app = FastAPI(
    title="api_vitivinicultura",
    version="1.0.0",
    description="API inserção de dados ao modelo de predição"
)

app.include_router(login_router)
app.include_router(user_router)

app.add_exception_handler(RequestValidationError, handlers.validation_exception_handler)
app.add_exception_handler(HTTPException, handlers.http_exception_handler)
app.add_exception_handler(Exception, handlers.generic_exception_handler)