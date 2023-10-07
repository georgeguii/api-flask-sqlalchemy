from sqlalchemy import Column, String, Integer
#from sqlalchemy.orm import relationship
from infra.configs.base import Base

class Cliente(Base):
  __tablename__ = 'clientes'

  id = Column(Integer, primary_key=True)
  nome = Column(String(255), nullable=False)
  cpf = Column(String(11), nullable=False)
  # "Relação reversa"
  # processosJudicias = relationship("ProcessoJudicial", backref="processosJudiciais", lazy="subquery")