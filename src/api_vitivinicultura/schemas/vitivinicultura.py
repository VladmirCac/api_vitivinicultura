from pydantic import BaseModel, Field
from enum import Enum

class TipoProcessamento(str, Enum):
    uvas_viniferas = "uvas_viniferas"
    uvas_americanas = "uvas_americanas"
    uvas_de_mesa = "uvas_de_mesa"
    sem_classificacao = "sem_classificacao"
    todos = "todos"

class ProcessamentoQueryParams(BaseModel):
    ano: int = Field(..., ge=1970, le=2023, description="Ano da análise")
    tipo: TipoProcessamento = Field(..., description="Tipo de uva a ser processada")

    def tipo_para_subopcao(self) -> int:
        return {
            TipoProcessamento.uvas_viniferas: 1,
            TipoProcessamento.uvas_americanas: 2,
            TipoProcessamento.uvas_de_mesa: 3,
            TipoProcessamento.sem_classificacao: 4,
            TipoProcessamento.todos: 0
        }[self.tipo]
    
class TipoImportacao(str, Enum):
    vinho_de_mesa = "vinho_de_mesa"
    espumantes = "espumantes"
    uvas_frescas = "uvas_frescas"
    uvas_passas = "uvas_passas"
    suco_de_uva = "suco_de_uva"
    todos = "todos"

class ImportacaoQueryParams(BaseModel):
    ano: int = Field(..., ge=1970, le=2023, description="Ano da análise")
    tipo: TipoImportacao = Field(..., description="Tipo de produto importado")

    def tipo_para_subopcao(self) -> int:
        return {
            TipoImportacao.vinho_de_mesa: 1,
            TipoImportacao.espumantes: 2,
            TipoImportacao.uvas_frescas: 3,
            TipoImportacao.uvas_passas: 4,
            TipoImportacao.suco_de_uva: 5,
            TipoImportacao.todos: 0
        }[self.tipo]
    
class TipoExportacao(str, Enum):
    vinho_de_mesa = "vinho_de_mesa"
    espumantes = "espumantes"
    uvas_frescas = "uvas_frescas"
    suco_de_uva = "suco_de_uva"
    todos = "todos"

class ExportacaoQueryParams(BaseModel):
    ano: int = Field(..., ge=1970, le=2023, description="Ano da análise")
    tipo: TipoExportacao = Field(..., description="Tipo de produto exportado")

    def tipo_para_subopcao(self) -> int:
        return {
            TipoExportacao.vinho_de_mesa: 1,
            TipoExportacao.espumantes: 2,
            TipoExportacao.uvas_frescas: 3,
            TipoExportacao.suco_de_uva: 4,
            TipoExportacao.todos: 0
        }[self.tipo]

class AnoQueryParams(BaseModel):
    ano: int = Field(..., ge=1970, le=2023, description="Ano da análise")

class Subitem(BaseModel):
    Nome: str = Field(..., description="Nome do subItem")
    Quantidade: float | None = Field(None, description="Quantidade do subItem")
    Unidade: str = Field(..., description="Unidade de medida da quantidade do subItem")
    Valor: float | None = Field(None, description="Valor do subItem em US$")

class ItemComSubitens(BaseModel):
    Nome: str = Field(..., description="Nome do item")
    Quantidade: float | None = Field(None, description="Quantidade do item")
    Unidade: str = Field(..., description="Unidade de medida da quantidade do item")
    Valor: float | None = Field(None, description="Valor do item em US$")
    subitens: list[Subitem] | None = Field(None, description="Lista de subitens realacionados")

class ResultadoDadosComSubitens(BaseModel):
    descricao: str = Field(..., description="Destrição dos itens")
    tipo: str = Field(..., description="Tipo dos itens listados")
    itens: list[ItemComSubitens] = Field(..., description="Lista dos itens")

class ResultadoDadosPorAno(BaseModel):
    ano: int = Field(..., description="Ano da análise")
    resultados: list[ResultadoDadosComSubitens] = Field(..., description="Lista dos resultados do ano")

    