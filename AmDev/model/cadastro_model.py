class CadastroModel:
    def __init__(self, nome, sobrenome, idade, sexo, id=None):
        self.id = id
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.sexo = sexo

