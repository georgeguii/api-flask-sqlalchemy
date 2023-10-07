from sqlalchemy import Column, String, Integer, DECIMAL, ForeignKey

from infra.configs.base import Base

class ProcessoJudicial(Base):
  __tablename__ = 'processosJudiciais'

  id = Column(Integer, primary_key=True)
  numeroProcesso = Column(String(12), nullable=False)
  tema = Column(String(255))
  valorDaCausa = Column(DECIMAL)
  advogado_id = Column(Integer, nullable=True)
  # Adicionar futuramente no arquivo para gerar o banco
  # cliente_id = Column(Integer, nullable=True)

  def __repr__(self):
    return f"Numero Processo = {self.numeroProcesso}, Tema = {self.tema}, Valor da Causa = {self.valorDaCausa}, Advogado = {self.advogado_id}"

  # o Banco de dados que estou usando 'planet scale' não suporta chaves estrangeiras lógicamente, então o relacionamento só é garantido via código
  # Caso esteja usando um banco normal :), deverá ser implantando seguindo o padrão abaixo

  # advogado_id = Column(Integer, ForeignKey("advogados.id"))
  # advogado = relationship('Advogado', back_populates='advogados')

  # cliente_id = Column(Integer, ForeignKey("clientes.id"))


  # documentos = relationship('Documento', back_populates='processo')