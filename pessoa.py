class Pessoa:
    """Classe que buscar modelar, de forma simples, uma pessoa padrão."""
    
    def __init__(self, nome, sobrenome, idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        
    def describe_pessoa(self):
        return "Nome:\t{}\nSobrenome:\t{}\nIdade:\t{}".format(
            self.nome, self.sobrenome, self.idade
            )
        
    def retorna_maioridade(self):
        if self.idade >= 18:
            print("Maior de idade.")
        else:
            print("Menor de idade.")
    
class Membro(Pessoa):
    """Classe que herda de Pessoa e modela o membro/usuário de uma biblioteca."""
    
    def __init__(self, nome, sobrenome, idade, cpf, endereco):
        super().__init__(nome, sobrenome, idade)
        self.cpf = cpf
        self.livros_emprestados = []
        self.endereco = endereco
        
    def __str__(self):
        return "{} - {}".format(self.cpf, self.nome)
    
    def __repr__(self):
        return "{} - {}".format(self.cpf, self.nome)
        
    def describe_pessoa(self):
        print("Nome:\t{}\nSobrenome:\t{}\nIdade:\t{}\nCPF:\t{}".format(
            self.nome, self.sobrenome, self.idade, self.cpf
        ))