import httpx
from bs4 import BeautifulSoup


async def fetch_html(url: str) -> BeautifulSoup:
    """
    Faz uma requisição GET assíncrona à URL e retorna o conteúdo como BeautifulSoup.
    """
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(url)
            response.raise_for_status()
            return BeautifulSoup(response.text, "html.parser")
    except httpx.RequestError as e:
        raise RuntimeError(f"Erro ao fazer requisição para {url}: {e}")
    except httpx.HTTPStatusError as e:
        raise RuntimeError(f"Erro HTTP ao acessar {url}: {e.response.status_code}")