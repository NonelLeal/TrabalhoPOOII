#código de importação da Classe pai
from pessoa import Pessoa

#classe pessoa ja contendo os dois atributos importados, nome e sobrenome, porém contendo m novo atributo, matricula
class Aluno(Pessoa):
    def __init__(self, matricula, nome, sobrenome):
        super().__init__(nome, sobrenome)
        self.matricula = matricula

    #set, ou seja, metodo de inserção de valor
    def setMatricula(self, matricula):
        self.matricula = matricula
    
    #get, ou seja, metodo de retrno de valor
    def getMatricula(self):
        return self.matricula