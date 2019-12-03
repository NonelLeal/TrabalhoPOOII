#Criando classe pai, Pessoa, contendo os atributos nome e sobrenome
class Pessoa:
    
        #método de criar instancias vazias
    def __init__(self):
        super().__init__()
        pass

        #set, ou seja, metodo de inserção de valor
    def setNome(self,nome):
        self.nome = nome

        #set, ou seja, metodo de inserção de valor
    def setSobrenome(self,sobrenome):
        self.sobrenome = sobrenome

        #get, ou seja, metodo de retrno de valor
    def getNome(self):
            return self.nome

        #set, ou seja, metodo de retorno de valor
    def getSobrenome(self):
            return self.sobrenome