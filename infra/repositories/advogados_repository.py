from sqlalchemy.orm.exc import NoResultFound

from infra.entities.advogados import Advogado
from infra.schemas.advogado_schema import AdvogadoSchema

class AdvogadoRepository:

  def __init__(self, ConnectionHandler) -> None:
    self.__ConnectionHandler = ConnectionHandler
    
  def select(self):
    with self.__ConnectionHandler() as db:
      try:
        advogados = db.session.query(Advogado).all()
        advogado_schema = AdvogadoSchema(many=True)
        result = advogado_schema.dump(advogados)
        return result
      except Exception as exception:
        db.session.rollback()
        raise exception
      
  def selectById(self, idAdvogado):
    with self.__ConnectionHandler() as db:
      try:
        advogado = db.session.query(Advogado).filter_by(id = idAdvogado).one()
        advogado_schema = AdvogadoSchema()
        return advogado_schema.dump(advogado)
      except NoResultFound:
        return None
        
  def insert(self, advogado_data):
    with self.__ConnectionHandler() as db:
      try:
        advogado = Advogado(
          nome=advogado_data["nome"],
          cpf=advogado_data["cpf"],
          oab=advogado_data["oab"]
        )
        db.session.add(advogado)
        db.session.commit()

        advogado_schema = AdvogadoSchema()
        serialized_advogado = advogado_schema.dump(advogado)

        return serialized_advogado
      except Exception as exception:
        db.session.rollback()
        raise exception

  def delete(self, id):
    with self.__ConnectionHandler() as db:
      try:
        db.session.query(Advogado).filter(Advogado.id == id).delete()
        db.session.commit()
      except Exception as exception:
        db.session.rollback()
        raise exception

  def update(self, id, advogado):
    with self.__ConnectionHandler() as db:
      try:
        db.session.query(Advogado).filter(Advogado.id == id).update({ "nome": advogado.nome})
        db.session.commit()
      except Exception as exception:
        db.session.rollback()
        raise exception


