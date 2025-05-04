
from fastapi import Request, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"errors": exc.detail}
    )

async def generic_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"errors": "Internal server error"}
    )

async def validation_exception_handler(request: Request, exc: RequestValidationError):
    # Você pode personalizar como quiser
    errors = []
    for error in exc.errors():
        field = ".".join(str(loc) for loc in error["loc"] if isinstance(loc, str))
        message = error["msg"]
        errors.append(f"Erro no campo '{field}': {message}")

    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={"errors": errors}
    )
