from analise import pesquisa, todos, analisar

while True:
    menu = int(input("Oque você quer fazer?\nAnalisar a planilha?(1)\nVer todos os livros?(2)\nPesquisar um livro?(3)\nsair(4)\n"))
    if menu == 1:
        print(analisar(int(input("\nQual página você quer analisar?\n"))))
    
    
    elif menu == 2:
        paginas = int(input("\nQuantas páginas tem na planilha?  "))
        deixados, levados, todos = todos(paginas)
        print(f"\nOs livros deixados são:\n{deixados}\nOs livros que foram levados são\n{levados}")
    
    
    elif menu == 3:
        paginas = int(input("quantas paginas tem o arquivo?:  "))
        livro = input("\nQual livro você quer procurar?:  ")
        print(pesquisa(todos(paginas)[2], livro))
    
    else:
        print("Saindo...")
        break