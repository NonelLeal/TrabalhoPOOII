#código de importação da Classe pai, pessoa
from pessoa import Pessoa

#classe pessoa ja contendo os dois atributos importados, nome e sobrenome, porém contendo m novo atributo, codigo.
class Professor(Pessoa):
    def __init__(self,codigo, nome, sobrenome):
        super().__init__(nome, sobrenome)
        self.codigo = codigo

    #set, ou seja, metodo de inserção de valor
    def setCodigo(self, codigo):
        self.codigo = codigo

    #get, ou seja, metodo de retrno de valor
    def getCodigo(self):
        return self.codigo