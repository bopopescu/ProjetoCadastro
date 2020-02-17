from AmDev.model.cadastro_model import CadastroModel

class CadastroDao:
    def __init__(self):
        self.arquivo = open('C:/Users/900146/Documents/git/TrabalhosPython/AmDev/Amdev.txt', 'r')


    def list_all(self):
        lista = []
        for p in self.arquivo:
            p = p.strip().split(';')
            model = CadastroModel(p[1], p[2], p[3], p[4], p[0])
            lista.append(model.__dict__)
        return lista

    def get_by_id(self, id):
        for p in self.arquivo:
            p = p.strip().split(';')
            model = CadastroModel(p[1], p[2], p[3], p[4], p[0])
            if id == int(p[0]):
                return model.__dict__
