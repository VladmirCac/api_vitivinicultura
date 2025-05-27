from fastapi import APIRouter, Depends, HTTPException, status
from api_vitivinicultura.crawlers import vitivinicultura as crawlers_viti
from api_vitivinicultura.schemas import vitivinicultura as schemas_viti
from api_vitivinicultura.schemas.error import ErrorResponse
from api_vitivinicultura.schemas.auth import TokenData
from api_vitivinicultura.core.security import get_current_user
from api_vitivinicultura.services.cache import cache, expireTime

router = APIRouter(
    prefix="/crawler",
    tags=["Crawler"]
)

@router.get(
    "/producao",
    response_model=schemas_viti.ResultadoDadosPorAno,
    responses= {
        422: {"model": ErrorResponse},
        500: {"model": ErrorResponse},
    }
)
async def producao(
    params: schemas_viti.AnoQueryParams = Depends(),
    current_user: TokenData = Depends(get_current_user),
):
    try:
        key = f"producao:{params.ano}"
        if key in cache:
            return cache[key]

        result = await crawlers_viti.get_producao(params.ano)
        resultado = {
            "ano": params.ano,
            "resultados": [result]
        }
        cache.set(key, resultado, expire=expireTime)
        return resultado
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail=["unexpected error in crawler", str(e)])
    

@router.get(
    "/processamentos",
    response_model=schemas_viti.ResultadoDadosPorAno,
    responses= {
        422: {"model": ErrorResponse},
        500: {"model": ErrorResponse},
    }
)
async def processamentos(
    params: schemas_viti.ProcessamentoQueryParams = Depends(),
    current_user: TokenData = Depends(get_current_user),
):
    
    subopcao = params.tipo_para_subopcao()
    ano = params.ano
    
    key = f"processamentos:{ano}:{subopcao}"
    if key in cache:
       return cache[key]

    try:
        if (subopcao == 0):
            results = await crawlers_viti.get_processamentos(ano)
            resultado = {
                "ano": ano,
                "resultados": results
            }
        else:
            result = await crawlers_viti.get_processamento(ano, subopcao)
            resultado = {
                "ano": ano,
                "resultados": [result]
            }
        cache.set(key, resultado, expire=expireTime)
        return resultado
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail=["unexpected error in crawler", str(e)])

@router.get(
    "/comercializacao",
    response_model=schemas_viti.ResultadoDadosPorAno,
    responses= {
        422: {"model": ErrorResponse},
        500: {"model": ErrorResponse},
    }
)
async def comercializacao(
    params: schemas_viti.AnoQueryParams = Depends(),
    current_user: TokenData = Depends(get_current_user),
):
    try:
        key = f"comercializacao:{params.ano}"
        if key in cache:
           return cache[key]

        result = await crawlers_viti.get_comercializacao(params.ano)
        resultado = {
            "ano": params.ano,
            "resultados": [result]
        }
        cache.set(key, resultado, expire=expireTime)
        return resultado
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail=["unexpected error in crawler", str(e)])


@router.get(
    "/importacoes",
    response_model=schemas_viti.ResultadoDadosPorAno,
    responses= {
        422: {"model": ErrorResponse},
        500: {"model": ErrorResponse},
    }
)
async def importacoes(
    params: schemas_viti.ImportacaoQueryParams = Depends(),
    current_user: TokenData = Depends(get_current_user),
):
    
    subopcao = params.tipo_para_subopcao()
    ano = params.ano
    
    key = f"importacoes:{ano}:{subopcao}"
    if key in cache:
        return cache[key]

    try:
        if (subopcao == 0):
            results = await crawlers_viti.get_importacoes(ano)
            resultado = {
                "ano": ano,
                "resultados": results
            }
        else:
            result = await crawlers_viti.get_importacao(ano, subopcao)
            resultado = {
                "ano": ano,
                "resultados": [result]
            }
        cache.set(key, resultado, expire=expireTime)
        return resultado
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail=["unexpected error in crawler", str(e)])
    

@router.get(
    "/exportacoes",
    response_model=schemas_viti.ResultadoDadosPorAno,
    responses= {
        422: {"model": ErrorResponse},
        500: {"model": ErrorResponse},
    }
)
async def exportacoes(
    params: schemas_viti.ExportacaoQueryParams = Depends(),
    current_user: TokenData = Depends(get_current_user),
):
    
    subopcao = params.tipo_para_subopcao()
    ano = params.ano
    
    key = f"exportacoes:{ano}:{subopcao}"
    if key in cache:
        return cache[key]

    try:
        if (subopcao == 0):
            results = await crawlers_viti.get_exportacoes(ano)
            resultado = {
                "ano": ano,
                "resultados": results
            }
        else:
            result = await crawlers_viti.get_exportacao(ano, subopcao)
            resultado = {
                "ano": ano,
                "resultados": [result]
            }
        cache.set(key, resultado, expire=expireTime)
        return resultado
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail=["unexpected error in crawler", str(e)])