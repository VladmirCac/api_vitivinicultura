from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from api_vitivinicultura.core.config import settings

# URL do SQLite
DATABASE_URL = settings.DATABASE_URL

# Cria o engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Cria uma sessão local
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Cria a base para os modelos
Base = declarative_base()

# Função para pegar uma sessão
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()