class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def setNome(self,nome):
        self.nome = nome

    def setSobrenome(self,sobrenome):
        self.sobrenome = sobrenome

    def getNome(self):
            return self.nome

    def getSobrenome(self):
            return self.sobrenome