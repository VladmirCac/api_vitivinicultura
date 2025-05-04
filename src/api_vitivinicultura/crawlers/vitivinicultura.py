from api_vitivinicultura.crawlers.base import fetch_html
import pandas as pd
from io import StringIO

BASE_URL = "http://vitibrasil.cnpuv.embrapa.br/index.php"

async def get_producao(ano: int):

    url = f"{BASE_URL}?ano={ano}&opcao=opt_02"
    # http://vitibrasil.cnpuv.embrapa.br/index.php?ano=2023&opcao=opt_02

    soup = await fetch_html(url)

    try:

        descricao_tag = soup.select_one("p.text_center")
        descricao = descricao_tag.text.strip() if descricao_tag else "Descrição não encontrada"
        table = soup.find('table', class_='tb_base tb_dados')  
        tabela_df = pd.read_html(StringIO(str(table)))[0]

    except ValueError:
        return {"erro": "error in scraping the site, check if there was a change in the htm of the source site."}

    dados_json = tabela_df.fillna('').to_dict(orient='records')

    return {
        "ano": ano,
        "descricao": descricao,
        "dados": dados_json
    }

async def get_processamento(ano: int, sub: int):

    url = f"{BASE_URL}?ano={ano}&opcao=opt_03&subopcao=subopt_0{sub}"
    # http://vitibrasil.cnpuv.embrapa.br/index.php?ano=2023&opcao=opt_03&subopcao=subopt_02
    
    soup = await fetch_html(url)

    try:

        descricao_tag = soup.select_one("p.text_center")
        descricao = descricao_tag.text.strip() if descricao_tag else "Descrição não encontrada"
        table = soup.find('table', class_='tb_base tb_dados')  
        tabela_df = pd.read_html(StringIO(str(table)))[0]

    except ValueError:
        return {"erro": "error in scraping the site, check if there was a change in the htm of the source site."}

    dados_json = tabela_df.fillna('').to_dict(orient='records')

    return {
        "descricao": descricao,
        "dados": dados_json
    }


async def get_processamentos(ano):
    from asyncio import gather
    tarefas = [
        get_processamento(ano, 1),
        get_processamento(ano, 2),
        get_processamento(ano, 3),
        get_processamento(ano, 4)
    ]
    resultados = await gather(*tarefas)
    return {
        "ano": ano,
        "dados": resultados
    }



