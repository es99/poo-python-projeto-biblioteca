class Endereco:
    """Classe responsável pelos atributos de endereço que serão atrelados a uma pessoa."""
    
    def __init__(self, rua, numero, bairro, cidade, estado, cep):
        self.rua = rua
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.cep = cep
        
    def describe_endereco(self):
        print("Rua:\t{}\nNum:\t{}\nBairro:\t{}\nCidade:\t{}\nEstado:\t{}\nCep:\t{}".format(
            self.rua, self.numero, self.bairro, self.cidade, self.estado, self.cep
        ))
        