from flask_restful import Resource
from flask import request

from AmDev.dao.cadastro_dao import CadastroDao

class CadastroController(Resource):
    def __init__(self):
        self.dao = CadastroDao()

    def get(self, id=None):
        if id:
            return self.dao.get_by_id(id)
        return self.dao.list_all()
