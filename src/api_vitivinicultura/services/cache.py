from diskcache import Cache

# Pasta .cache criada na raiz do projeto (ao lado do .venv, .env, etc.)
cache = Cache(".cache")  # pode ajustar o caminho, se quiser
expireTime = 60 * 60 * 24 * 15