# 🍇 API Vitivinicultura

API desenvolvida com [FastAPI](https://fastapi.tiangolo.com/) para disponibilizar dados públicos da vitivinicultura brasileira. Os dados são coletados do site da Embrapa Uva e Vinho via **web crawler assíncrono** e retornados em formato JSON estruturado.

---

## 📦 Funcionalidades

- 🔐 Autenticação JWT com senha criptografada (bcrypt)
- 📚 Banco de dados SQLite com SQLAlchemy e Alembic (migrações)
- 🔄 Cache local com `diskcache` configurado para 12h
- 🕷️ Web crawler assíncrono com `httpx` + `BeautifulSoup`
- 📊 Documentação automática Swagger e ReDoc
- 💡 Estrutura modular com suporte a múltiplos crawlers

---

## 🚀 Como rodar o projeto

### 1. Instale as dependências
```bash
poetry install
```

### 2. Configure variáveis de ambiente

Crie o arquivo `.env` na raiz com o conteúdo:

```env
DATABASE_URL=sqlite:///./api_vitivinicultura.db
SECRET_KEY=sua_chave_ultra_secreta
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### 3. Crie o banco de dados e rode as migrações

```bash
alembic upgrade head
```

### 4. Rode a API localmente

```bash
uvicorn src.api_vitivinicultura.main:app --reload
```

---

## 📘 Endpoints principais

### 🔑 Autenticação
| Método | Endpoint       | Descrição                  |
|--------|----------------|----------------------------|
| POST   | `/auth/login`  | Login com JWT (via JSON)   |
| POST   | `/users/`      | Criar novo usuário         |

### 🧑 Usuários
| Método | Endpoint      | Descrição            |
|--------|---------------|----------------------|
| GET    | `/users/`     | Listar usuários (JWT)|
| PUT    | `/users/{id}` | Atualizar usuário    |
| DELETE | `/users/{id}` | Deletar usuário      |

### 🍇 Crawler

| Método | Endpoint                    | Descrição                               |
|--------|-----------------------------|-----------------------------------------|
| GET    | `/crawler/producao`         | Listar dados de produção por ano        |
| GET    | `/crawler/processamentos`   | Listar dados de processamento por ano   |
| GET    | `/crawler/comercializacao`  | Listar dados de comercialização por ano |
| GET    | `/crawler/importacoes`      | Listar dados de importação por ano      |
| GET    | `/crawler/exportacoes`      | Listar dados de exportação por ano      |

---

## 🗂️ Estrutura do projeto

```
src/
├── api_vitivinicultura/
│   ├── main.py                 # App FastAPI
│   ├── core/                   # Config, segurança, database
│   ├── models/                 # SQLAlchemy models
│   ├── routers/                # Rotas organizadas
│   ├── schemas/                # Pydantic (v2)
│   ├── crawlers/               # Módulos de web scraping
│   └── services/               # Serviços auxiliares (ex: cache)
```

---

## 🧪 Testes

Em breve…

---

## 🧠 Créditos

Desenvolvido por Vladmir Carvalho com apoio da FIAP e dados abertos da Embrapa Uva e Vinho: http://vitibrasil.cnpuv.embrapa.br/.

---

## 🛡️ Licença

Este projeto é livre para uso educacional. O uso dos dados coletados deve respeitar os termos da Embrapa.