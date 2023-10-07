from unittest import mock
from mock_alchemy.mocking import  UnifiedAlchemyMagicMock
from infra.entities.advogados import Advogado
from infra.repositories.advogados_repository import AdvogadoRepository


class ConnectionHandlerMock:
  def __init__(self) -> None:
    self.session = UnifiedAlchemyMagicMock(
      data = [
        (
          [
            mock.call.query(Advogado)
          ],
          [Advogado(id = 1, nome = "Gabriel", cpf = "00011122233", oab =  "1234567")]
        )
      ]
    )

  def __enter__(self):
    return self
  
  def __exit__(self, exc_type, exc_val, exc_tb):
    self.session.close()

def teste_select():
  repository = AdvogadoRepository(ConnectionHandlerMock)
  response = repository.select()
  print()
  print(response)
  assert isinstance(response, list)
  assert isinstance(response[0], Advogado)