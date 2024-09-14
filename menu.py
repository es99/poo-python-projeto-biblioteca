from endereco import Endereco
from pessoa import Membro
from livro import Livro
from biblioteca import Biblioteca

biblioteca = Biblioteca()

def decora_linha():
    print("*" * 30)
    
def cadastrar_endereco():
    rua = input("Rua: ")
    numero = int(input("Num: "))
    bairro = input("Bairro: ")
    cidade = input("Cidade: ")
    estado = input("Estado: ")
    cep = input("Cep: ")
    
    endereco = Endereco(rua, numero, bairro, cidade, estado, cep)
    
    return endereco

def cadastrar_membro(endereco):
    nome = input("nome: ")
    sobrenome = input("sobrenome: ")
    idade = int(input("idade: "))
    cpf = input("cpf: ")
    
    membro = Membro(nome, sobrenome, idade, cpf, endereco)
    
    return membro

def cadastrar_livro():
    id = int(input("Id: "))
    titulo = input("Titulo: ")
    autor = input("Autor: ")
    ano = input("Ano: ")
    
    livro = Livro(id, titulo, autor, ano)
    
    return livro

def mostra_livros():
    if len(biblioteca.livros) > 0:
        for i, livro in enumerate(biblioteca.livros):
            print(f"{i+1}. {livro}")
    else:
        print("\nA biblioteca ainda não possui livros em seu acervo.")
        
def mostra_membros():
    if len(biblioteca.membros) > 0:
        for i, membro in enumerate(biblioteca.membros):
            print(f"{i+1}. {membro}")
    else:
        print("\nA biblioteca ainda não possui membros cadastrados!")
        
def emprestimo_de_livro():
    if len(biblioteca.livros) == 0 or len(biblioteca.membros) == 0:
        print("\nA biblioteca ainda não possui livros no acervo ou membros cadastrados!")
    else:
        index_livro = input("informe o index do livro: ")
        index_membro = input("informe o index do membro: ")
        livro = biblioteca.livros[int(index_livro) - 1]
        membro = biblioteca.membros[int(index_membro) -1]
        if biblioteca.emprestar_livro(livro, membro):
            print(f"Livro {livro} emprestado com sucesso ao membro {membro}")
        else:
            print("Livro não pôde ser emprestado.")
        
def mostrar_livros_emprestados_por_membro():
    index_usuario = input("Informe o index do usuário: ")
    membro = biblioteca.membros[int(index_usuario) - 1]
    if membro.livros_emprestados == 0:
        print(f"O usuário {membro} não possui livros emprestados.")
    else:
        print("\nDados do usuário: ")
        membro.describe_pessoa()
        for livro in membro.livros_emprestados:
            print(livro)
        
def devolucao_de_livro():
    if len(biblioteca.livros) > 0 and len(biblioteca.membros) > 0:
        index_livro = input("informe o index do livro: ")
        index_membro = input("informe o index do membro: ")
        livro = biblioteca.livros[int(index_livro) - 1]
        membro = biblioteca.membros[int(index_membro) - 1]
        if biblioteca.devolver_livro(livro, membro):
            print(f"{livro} devolvido pelo usuário {membro}")
        else:
            print("Por algum motivo o livro não pôde ser devolvido.")
    else:
        print("A biblioteca não tem livros no acervo ou membros cadastrados!")
        
def mostrar_livros_emprestados_da_biblioteca():
    emprestados = []
    if len(biblioteca.livros) == 0:
        print("Não existem livros cadastrados na biblioteca!")
    else:
        for livro in biblioteca.livros:
            if livro.status == False:
                emprestados.append(livro)
            else:
                continue
    
    if len(emprestados) > 0:
        print("\nLivros do acervo que estão emprestados:")
        for livro_emprestado in emprestados:
            print(livro_emprestado)

while(True):
    opcao = input("\nEscolha uma das opções: \n1.Cadastrar membro\n2.Cadastrar livro\n3.Visualizar acervo\n4.Visualizar membros cadastrados\n" \
        + "5.Empréstimo de livro\n6.Devolução de livro\n7.Mostrar livros emprestados do usuário\n8.Livros emprestados\n\n")
    
    if int(opcao) == 1:
        endereco = cadastrar_endereco()
        membro = cadastrar_membro(endereco)
        biblioteca.adiciona_membro(membro)
        print("{} cadastrado com sucesso!".format(membro))
    elif int(opcao) == 2:
        livro = cadastrar_livro()
        biblioteca.adiciona_livro(livro)
        print("{} cadastrado com sucesso!".format(livro))
    elif int(opcao) == 3:
        mostra_livros()
    elif int(opcao) == 4:
        mostra_membros()
    elif int(opcao) == 5:
        emprestimo_de_livro()
    elif int(opcao) == 6:
        devolucao_de_livro()
    elif int(opcao) == 7:
        mostrar_livros_emprestados_por_membro()
    elif int(opcao) == 8:
        mostrar_livros_emprestados_da_biblioteca()
    else:
        print("Opção inválida, voltando para o menu inicial...")
    
            