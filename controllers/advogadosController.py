from flask import Blueprint
from flask import request, make_response, jsonify

from infra.configs.connection import DBConnectionHandler
from infra.repositories.advogados_repository import AdvogadoRepository


advogados_controller = Blueprint('advogados_controller', __name__)
advogadosRepository = AdvogadoRepository(DBConnectionHandler)

@advogados_controller.route("/advogados",methods=["GET"])
def getAdvogados():
  try:
    advogados = advogadosRepository.select()
    status_code = 200
    response_data = {
        "data": advogados,
        "message": 'Lista de Advogados',
    }
    return make_response(jsonify(response_data), status_code)
  except Exception as exception:
    status_code = 500
    detail = exception
    return make_response(jsonify(detail), status_code)

@advogados_controller.route("/advogados/<int:id>",methods=["GET"])
def getAdvogadosById(id):
  advogado = advogadosRepository.selectById(idAdvogado=id)
  status_code = 200
  if advogado is None:
    status_code = 404
  response_data = {
      "data": advogado,
      "message": 'Advogado',
  }
  return make_response(jsonify(response_data), status_code)

@advogados_controller.route("/advogados", methods=["POST"])
def criarAdvogados():
  try:
    advogado = request.get_json()
    advogadoCadastrado = advogadosRepository.insert(advogado_data=advogado)
    
    # Make response
    status_code = 201
    response_data = {
      "data": advogadoCadastrado,
      "message": 'Advogado inserido com sucesso',
    }

    return make_response(jsonify(response_data), status_code)
  except Exception as exception:
    status_code = 500
    detail = exception
    return make_response(jsonify(detail), status_code)

@advogados_controller.route("/advogados/<int:id>", methods=["PUT"])
def editarAdvogado(id):
  advogadoOriginal = advogadosRepository.selectById(id)
  advogadoModificado = request.json
  advogado = advogadoOriginal.update(advogadoModificado)
  return make_response(
    jsonify(advogado)
  )
      
@advogados_controller.route("/advogados/<int:id>", methods=["DELETE"])
def apagarProcesso(idAdvogado):
  advogadosRepository.delete(id=idAdvogado)
  return make_response(
    jsonify(message="Advogado apagado com sucesso")
  )