from api_vitivinicultura.crawlers.base import fetch_html

BASE_URL = "http://vitibrasil.cnpuv.embrapa.br/index.php"

async def get_dados(url):

    soup = await fetch_html(url)

    descricao_tag = soup.select_one("p.text_center")
    descricao = descricao_tag.text.strip() if descricao_tag else "Descrição não encontrada"

    table = soup.find("table", class_="tb_base tb_dados")
    if not table:
        return {"descricao": descricao, "dados": []}

    rows = table.find_all("tr")
    headers = [th.get_text(strip=True) for th in rows[0].find_all("th")]
    
    tipo = headers[0] if headers else "Tipo"
    unidade = ""
    if len(headers) > 1 and "(" in headers[1]:
        unidade = headers[1][headers[1].find("("):]

    dados = []
    item_atual = None

    for row in rows[1:]:
        cols = [td.get_text(strip=True) for td in row.find_all("td")]
        if not cols or len(cols) < 2:
            continue

        nome = cols[0]
        qtd_str = cols[1].replace(".", "").replace(",", ".")
        try:
            quantidade = float(qtd_str) if qtd_str and qtd_str != "-" else None
        except ValueError:
            quantidade = None

        valor = None
        if len(cols) > 2:
            val_str = cols[2].replace(".", "").replace(",", ".")
            try:
                valor = float(val_str) if val_str and val_str != "-" else None
            except ValueError:
                valor = None

        dado = {
            "Nome": nome,
            "Quantidade": quantidade,
            "Unidade": unidade,
        }
        if valor is not None:
            dado["Valor"] = valor

        classes = row.find("td").get("class", [])
        if "tb_item" in classes:
            item_atual = dado
            item_atual["subitens"] = []
            dados.append(item_atual)
        elif "tb_subitem" in classes and item_atual:
            item_atual["subitens"].append(dado)
        else:
            # Linha sem classe conhecida
            dados.append(dado)

    return {
        "descricao": descricao,
        "tipo": tipo,
        "itens": dados
    }

async def get_producao(ano: int):
    url = f"{BASE_URL}?ano={ano}&opcao=opt_02"
    return await get_dados(url)

async def get_processamento(ano: int, sub: int):
    url = f"{BASE_URL}?ano={ano}&opcao=opt_03&subopcao=subopt_0{sub}"
    # http://vitibrasil.cnpuv.embrapa.br/index.php?ano=2023&opcao=opt_03&subopcao=subopt_02
    return await get_dados(url)
    
async def get_processamentos(ano):
    
    from asyncio import gather
    
    tarefas = [
        get_processamento(ano, 1),
        get_processamento(ano, 2),
        get_processamento(ano, 3),
        get_processamento(ano, 4)
    ]

    resultados = await gather(*tarefas)
    
    return resultados

async def get_comercializacao(ano: int):
    url = f"{BASE_URL}?ano={ano}&opcao=opt_04"
    return await get_dados(url)

async def get_importacao(ano: int, sub: int):
    url = f"{BASE_URL}?ano={ano}&opcao=opt_05&subopcao=subopt_0{sub}"
    # http://vitibrasil.cnpuv.embrapa.br/index.php?ano=2023&opcao=opt_03&subopcao=subopt_02
    return await get_dados(url)

async def get_importacoes(ano):
    
    from asyncio import gather
    
    tarefas = [
        get_importacao(ano, 1),
        get_importacao(ano, 2),
        get_importacao(ano, 3),
        get_importacao(ano, 4),
        get_importacao(ano, 5)
    ]

    resultados = await gather(*tarefas)
    
    return resultados

async def get_exportacao(ano: int, sub: int):
    url = f"{BASE_URL}?ano={ano}&opcao=opt_06&subopcao=subopt_0{sub}"
    return await get_dados(url)

async def get_exportacoes(ano):
    
    from asyncio import gather
    
    tarefas = [
        get_exportacao(ano, 1),
        get_exportacao(ano, 2),
        get_exportacao(ano, 3),
        get_exportacao(ano, 4),
    ]

    resultados = await gather(*tarefas)
    
    return resultados