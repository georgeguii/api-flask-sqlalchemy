from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from infra.entities.advogados import Advogado

class AdvogadoSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Advogado
