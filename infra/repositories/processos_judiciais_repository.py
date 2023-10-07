from sqlalchemy.orm.exc import NoResultFound

from infra.entities.advogados import Advogado
from infra.entities.processosJudiciais import ProcessoJudicial

class ProcessosJudiciaisRepository:

  def __init__(self, ConnectionHandler) -> None:
    self.__ConnectionHandler = ConnectionHandler

  def select(self):
    with self.__ConnectionHandler() as db:
      try:
        return db.session.query(ProcessoJudicial).all()
      except NoResultFound as exception:
        return None
      except Exception as exception:
        db.session.rollback()
        raise exception
    
  def selectById(self, idProcesso):
    with self.__ConnectionHandler() as db:
      try:
        return db.session.query(ProcessoJudicial).filter_by(id = idProcesso).one()
      except NoResultFound as exception:
        return None
  
  # Forma 1
  def selectJoinAdvogados(self):
    with self.__ConnectionHandler() as db:
      return db.session.query(ProcessoJudicial, Advogado)\
        .with_entities(
          ProcessoJudicial.numeroProcesso,
          ProcessoJudicial.tema,
          ProcessoJudicial.valorDaCausa,
          Advogado.nome
        )\
        .all()
    
  # Forma 2
  def selectJoinAdvogadosById(self,idProcesso):
    with self.__ConnectionHandler() as db:
      return db.session.query(ProcessoJudicial)\
        .filter_by(id = idProcesso)\
        .join(Advogado, ProcessoJudicial.advogado_id == Advogado.id)\
        .with_entities(
          ProcessoJudicial.numeroProcesso,
          ProcessoJudicial.tema,
          ProcessoJudicial.valorDaCausa,
          Advogado.nome
        )\
        .one()
  
  def insert(self, processo):
    with self.__ConnectionHandler() as db:
      try:
        db.session.add(processo)
        db.session.commit()
      except Exception as exception:
        db.session.rollback()
        raise exception

  def delete(self, id):
    with self.__ConnectionHandler() as db:
      try:
        db.session.query(ProcessoJudicial).filter(ProcessoJudicial.id == id).delete()
        db.session.commit()
      except Exception as exception:
        db.session.rollback()
        raise exception

  def update(self, id, processo):
    with self.__ConnectionHandler() as db:
      try:
        db.session.query(ProcessoJudicial).filter(ProcessoJudicial.id == id).update({ "numeroProcesso": processo.numeroProcesso})
        db.session.commit()
      except Exception as exception:
        db.session.rollback()
        raise exception