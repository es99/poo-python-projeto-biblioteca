class Biblioteca:
    """Classe que simula uma biblioteca."""
    
    def __init__(self):
        self.livros = []
        self.membros = []
        
    def adiciona_livro(self, livro):
        livro.status = True
        self.livros.append(livro)
        
    def adiciona_membro(self, membro):
        self.membros.append(membro)
        
    def emprestar_livro(self, livro, membro):
        if livro in self.livros and livro.status == True and membro in self.membros:
            membro.livros_emprestados.append(livro)
            livro.status = False
            return True
        else:
            return False
        
    def devolver_livro(self, livro, membro):
        if livro not in self.livros or membro not in self.membros or livro.status == True:
            print("Erro ao devolver livro!")
            return False
        else:
            membro.livros_emprestados.remove(livro)
            livro.status = True
            print("Livro devolvido.")
            return True
            
        