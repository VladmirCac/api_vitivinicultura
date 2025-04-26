from sqlalchemy import Column, Integer, String
from ..core.database import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    obs = Column(String, nullable=True)