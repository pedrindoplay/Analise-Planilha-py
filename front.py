from analise import pesquisa, todos, analisar

paginas = int(input("Quantas pagians possui o arquivo?:  "))

while True:
    menu = int(input("Oque você quer fazer?\nAnalisar a planilha?(1)\nVer todos os livros?(2)\nPesquisar um livro?(3)\nsair(4)\n"))
    if menu == 1:
        a = int(input("Qual pagina você quer ver?  "))
        deixados, levados = analisar(a)
        print(f"\nOs livros deixados são:\n{deixados}\n\nOs livros que foram levados são\n{levados}\n\n")


    elif menu == 2:
        deixados, levados, todos = todos(paginas)
        print(f"\nOs livros deixados são:\n{deixados}\n\nOs livros que foram levados são\n{levados}")
    
    
    elif menu == 3:
        livro = input("\nQual livro você quer procurar?:  ")
        print(pesquisa(todos(paginas)[2], livro))
    
    else:
        print("Saindo...")
        break