from analise import pesquisa, todos, analisar

paginas = int(input("Quantas pagians possui o arquivo?:  "))-1

while True:
    menu = int(input("Oque você quer fazer?\nAnalisar página?(1)\nVer todos os livros?(2)\nPesquisar um livro?(3)\nsair(4)\n"))
    if menu == 1:
        a = int(input("Qual pagina você quer ver?  "))
        deixados, levados = analisar(a)
        print(f"\nOs livros deixados são:\n{deixados}\n\nOs livros que foram levados são\n{levados}\n\n")


    elif menu == 2:
        deixados, levados, todos = todos(paginas)
        print(f"\nOs livros deixados são:\n{deixados}\n\nOs livros que foram levados são\n{levados}")
        print(f"\nNo total foram deixados: {len(deixados)}\n e foram levados: {len(levados)}")
    
    
    elif menu == 3:
        livro = input("\nQual livro você quer procurar?:  ")-1
        print(pesquisa(todos(paginas)[2], livro))
    
    else:
        print("Saindo...")
        break