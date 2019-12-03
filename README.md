# TrabalhoPOOII


# descrição Classes

A tabela abaixo descreve cada classe criada

| Classe    | Descrição |
| ------    | ------    |
| main      | Classe principal de execução do código |
| Pessoa    | Classe Pai |
| Aluno     | Classe filha, herda nome e sobrenome, possui Matricula |
| Professor | Classe filha, herda nome e sobrenome, possui Codigo|

### Classe Pessoa:
- ### Atributos
    * [Nome]- Atributo do tipo String que recebe o nome de [Pessoa]
    * [Sobrenome] - Atributo do tipo String que recebe o sobrenome de [Pessoa]
- ### Metodos
    * [getNome]- Metodo que retorna o valor inserido em [self._nome]
    * [getSobrenome] - Metodo que retorna o valor inserido em [self._sobrenome]
    * [setNome]- Metodo que insere valor em [self._nome]
    * [setSobrenome] - Metodo que insere valor em [self._sobrenome]

A classe [Pessoa] é a classe pai contendo nome e sobrenome que são atributos comuns para [Aluno] e [Professor]

### Classe Aluno:
- ### Atributos
    * [Nome]- Atributo do tipo String que recebe o nome de [Aluno], herdado de [Pessoa]
    * [Sobrenome] - Atributo do tipo String que recebe o sobrenome de [Aluno], herdado de [Pessoa]
    * [Matricula] - Atributo do tipo Integer que recebe o numero da matrícula de [Aluno], herdado de [Pessoa]
- ### Metodos
    * [getMatricula]- Metodo que retorna o valor inserido em [self._matricula], herdado de [Pessoa]
    * [setMatricula] - Metodo que insere valor em [self._matricula], herdado de [Pessoa]

A classe [Aluno] é uma das classes filhas que herdam os atributos de [Pessoa], possui [Matricula]

### Classe Professor:
- ### Atributos
    * [Nome]- Atributo do tipo String que recebe o nome de [Professor], herdado de [Pessoa]
    * [Sobrenome] - Atributo do tipo String que recebe o sobrenome de [Professor], herdado de [Pessoa]
    * [Codigo] - Atributo do tipo Integer que recebe o numero do Código de [Professor], herdado de [Pessoa]
- ### Metodos
    * [getCodigo]- Metodo que retorna o valor inserido em [self._codigo], herdado de [Pessoa]
    * [setCodigo] - Metodo que insere valor em [self._codigo], herdado de [Pessoa]

A classe [Professor] é uma das classes filhas que herdam os atributos de [Pessoa], possui [Codigo]


### Equipe
|                                         | Integrante|
| ------                                  | ------    |
| Nome                                    | Lenon Tadeu Lopes Leal|
| Matrícula                               | 21605424 |
| Curso                                   | Sistemas de informação |
| Principais responsabilidades no projeto | Projeto em sua totalidade|



