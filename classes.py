class Pessoa: 

    def __init__(self, name, age, res):
        # inicializar os atributos da classe
        self.nome = name
        self.idade = age
        self.residencia = res

obj_pessoa = Pessoa("Joao", 20, "SP")

print(obj_pessoa.nome)