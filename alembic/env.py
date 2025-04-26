from logging.config import fileConfig
import sys
import os

from sqlalchemy import pool
from alembic import context

# Adicionar o src/ ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

# Agora podemos importar normalmente
from api_vitivinicultura.core.database import engine, Base
import api_vitivinicultura.models # importa os modelo do models.__init__ para registrar

# Config do Alembic
config = context.config

# Logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Definir o target_metadata
target_metadata = Base.metadata

def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")  # ainda precisa pegar para offline
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    connectable = engine  # Usa o engine diretamente (não usa engine_from_config)

    with connectable.connect() as connection:
        context.configure(
            connection=connection, 
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

# Escolhe se offline ou online
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
