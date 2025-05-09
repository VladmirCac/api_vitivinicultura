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
    except httpx.ConnectError:
        raise Exception("Unable to connect to Embrapa website. Please try again later.")
    except httpx.RequestError as e:
        raise Exception(f"Connection error when accessing URL: {url}")
    except Exception as e:
        raise Exception(f"Connection error when accessing {url}: {str(e)}")