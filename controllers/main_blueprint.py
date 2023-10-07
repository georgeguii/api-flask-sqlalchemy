from flask import Blueprint

# Crie o Blueprint principal
main_blueprint = Blueprint('main', __name__)

from controllers.processosController import processos_controller
from controllers.advogadosController import advogados_controller

main_blueprint.register_blueprint(processos_controller)
main_blueprint.register_blueprint(advogados_controller)
