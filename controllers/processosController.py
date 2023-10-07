from flask import Blueprint
from flask import request, make_response, jsonify

from infra.configs.connection import DBConnectionHandler
from infra.repositories.processos_judiciais_repository import ProcessosJudiciaisRepository


processos_controller = Blueprint('user_controller', __name__)
processoRepository = ProcessosJudiciaisRepository(DBConnectionHandler)

@processos_controller.route("/processos",methods=["GET"])
def getProcessos():
  return make_response(
    jsonify(
      mensagem='Lista de Processos',
      dados=processoRepository.select()
    )
  )


@processos_controller.route("/processos/<int:id>",methods=["GET"])
def getProcessosById(id):
  processo = processoRepository.selectJoinAdvogadosById(id)
  return make_response(
    jsonify(processo)
  )

@processos_controller.route("/processos", methods=["POST"])
def criarProcessos():
  processo = request.json
  processoRepository.insert(processo=processo)
  
  return make_response(
    jsonify(processo)
  )

@processos_controller.route("/processos/<int:id>", methods=["PUT"])
def editarProcessos(id):
  processoOriginal = processoRepository.selectById(id)
  processoModificado = request.json
  processo = processoOriginal.update(processoModificado)
  return make_response(
    jsonify(processo)
  )
      
@processos_controller.route("/processos/<int:id>", methods=["DELETE"])
def apagarProcesso(idProcesso):
  processoRepository.delete(id=idProcesso)
  return make_response(
    jsonify(message="Processo apagado com sucesso")
  )