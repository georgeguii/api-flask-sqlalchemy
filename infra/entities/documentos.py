from sqlalchemy import Column, String, Integer

from infra.configs.base import Base

class Documento(Base):
  __tablename__ = 'documentos'

  id = Column(Integer, primary_key=True)
  nomeArquivo = Column(String(100), nullable=False)
  caminho = Column(String(255), nullable=False)
  extensao = Column(String(5), nullable=False)
  processo_id = Column(Integer, nullable=False)

  # processo_id = Column(Integer, ForeignKey("processosJudiciais.id"))
  # processo = relationship('ProcessoJudicial', back_populates='documentos')