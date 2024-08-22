class Livro:
    """Classe que busca representar os métodos e comportamentos de um livro,
    ou seja, um objeto da vida real."""
    
    def __init__(self, id, titulo, autor, ano):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
    
    def __str__(self):
        return "id{}. {}, {}".format(self.id, self.titulo, self.autor)
    
    def __repr__(self):
        return "id{}. {}, {}".format(self.id, self.titulo, self.autor)
        
    def describe_livro(self):
        print("Id:\t{}\nTítulo:\t{}\nAutor:\t{}\nAno:\t{}".format(
            self.id, self.titulo, self.autor, self.ano
            ))
    