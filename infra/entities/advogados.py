from sqlalchemy import Column, String, Integer

from infra.configs.base import Base

class Advogado(Base):
  __tablename__ = 'advogados'

  id = Column(Integer, primary_key=True)
  nome = Column(String(255), nullable=False)
  cpf = Column(String(11), nullable=False)
  oab = Column(String(7), nullable=False)

  def __init__(self, nome, cpf, oab):
    self.nome = nome
    self.cpf = cpf
    self.oab = oab

  def __repr__(self):
    return f"Nome = {self.nome}, CPF = {self.cpf}"
    