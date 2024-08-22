Projeto: Sistema de Gerenciamento de Bibliotecas

Descrição:
Você vai desenvolver um sistema básico para gerenciar uma biblioteca. Esse sistema deve permitir o cadastro de livros, membros e o empréstimo de livros. A ideia é criar classes para representar os livros, membros da biblioteca e o próprio sistema de gerenciamento.

Requisitos:
Classe Livro:

Atributos: título, autor, ano de publicação, ISBN (ou outro identificador único), status de disponibilidade.
Métodos: exibir informações do livro, verificar se o livro está disponível, marcar como emprestado ou devolvido.
Classe Membro:

Atributos: nome, número de identificação, lista de livros emprestados.
Métodos: exibir informações do membro, adicionar um livro à lista de livros emprestados, devolver um livro.
Classe Biblioteca:

Atributos: lista de livros, lista de membros.
Métodos: adicionar novos livros à biblioteca, cadastrar novos membros, emprestar um livro a um membro, receber a devolução de um livro.
Herança e Composição:

Crie uma classe Pessoa que possa ser a base para a classe Membro, demonstrando o uso de herança.
Considere utilizar instâncias de Livro como atributos em outras classes para praticar a composição.
Importação de Classes:

Organize seu código em módulos separados para Livro, Membro, Biblioteca, e use a importação de classes para estruturar o programa principal.
Interação:

Implemente um menu simples no terminal que permita ao usuário interagir com o sistema, como adicionar livros, cadastrar membros, emprestar e devolver livros.
Esse projeto te permitirá consolidar o que você aprendeu sobre POO e classes em Python, aplicando conceitos de criação de classes, herança, composição, e importação de módulos.