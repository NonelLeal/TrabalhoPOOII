#classes importadas, a fim de serem instanciadas
import pessoa
import aluno
import professor

#execução do código

#Classe pessoa instanciada, com objetos Pessoa1 escolhido, seus atributos discriminados através dos métodos de inserção e retorno
pessoa1 = pessoa.Pessoa('João','Miller')
print("Retornando as características de pessoa com nome e sobrenome:")
print("Nome da pessoa: {0} {1} ".format(pessoa1.getNome(),pessoa1.getSobrenome()))

#Classe aluno instanciada, com objeto aluno1 escolhido e seus atributos discriminados através dos métodos de inserção e retorno
aluno1 = aluno.Aluno(302010, 'Cesar','Vieira')
print("\nRetornando as características de aluno com nome,sobrenome e matrícula:")
print("Nome do aluno: {0} {1} ".format(aluno1.getNome(),aluno1.getSobrenome()),"\nMatrícula do aluno:{} ".format(aluno1.getMatricula()))

#Classe Professor instanciada, com objeto professor1 escolhido e seus atributos discriminados através dos métodos de inserção e retorno
professor1 = professor.Professor(102030, 'Alan','Paulo')
print("\nRetornando as características de professor com nome, sobrenome e código:")
print("Nome do professor: {0} {1}".format(professor1.getNome(),professor1.getSobrenome()),"\nCódigo do professor:{} ".format(professor1.getCodigo()))