from fastapi import APIRouter, Depends, Query, HTTPException, status
from api_vitivinicultura.crawlers import vitivinicultura as crawlers_viti
from api_vitivinicultura.schemas.vitivinicultura import ProdComercAnoResponse
from api_vitivinicultura.schemas.error import ErrorResponse
from api_vitivinicultura.schemas.auth import TokenData
from api_vitivinicultura.core.security import get_current_user

router = APIRouter(
    prefix="/crawler",
    tags=["Crawler"]
)

@router.get(
    "/producao",
    response_model=ProdComercAnoResponse,
    responses= {
        404: {"model": ErrorResponse},
        422: {"model": ErrorResponse},
    }
)
async def producao(
    ano: int = Query(..., description="Ano da produção"),
    #current_user: TokenData = Depends(get_current_user),

):
    try:
        resultado = await crawlers_viti.get_producao(ano)
        if "erro" in resultado:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail=["Table not found The source site may be temporarily down. Please check back later."])
        return resultado
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail=["unexpected error in crawler", str(e)])
    

@router.get(
    "/processamentos",
    #response_model=ProdComercAnoResponse,
    responses= {
        422: {"model": ErrorResponse},
        500: {"model": ErrorResponse},
    }
)
async def processamentos(
    ano: int = Query(..., description="Ano do processamento"),
    #current_user: TokenData = Depends(get_current_user),
):
    try:
        resultado = await crawlers_viti.get_processamentos(ano)
        return resultado
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail=["unexpected error in crawler", str(e)])