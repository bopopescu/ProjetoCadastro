from flask import Flask
from flask_restful import Api

from AmDev.controller.cadastro_controller import CadastroController

app = Flask(__name__)
api = Api(app)

api.add_resource(CadastroController, '/api/cadastro', endpoint='cadastros')
api.add_resource(CadastroController, '/api/cadastro/<int:id>', endpoint='cadastro')

app.run(debug=True)