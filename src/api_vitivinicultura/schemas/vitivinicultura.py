from pydantic import BaseModel, Field
from typing import Dict

class ProdComercAnoResponse(BaseModel):
    ano: int = Field(..., description="Ano da produção")
    descricao: str = Field(..., description="Descrição da produção")
    dados: list[Dict[str, str]] = Field(..., description="Lista de registros da tabela")

    class Config:
        from_attributes = True