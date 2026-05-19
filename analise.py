import pandas as pd

def analisar():
    while True:
        livrosPegados = []
        livrosDeixados = []
        pagina = int(input("Qual página do arquivo você quer analisar?\n"))
        dados = pd.read_excel("Livros.xlsx", sheet_name=pagina-1)
        h = dados.index[-1]
        a = 1

        while a <= h:
            celula = dados.iloc[a, 0]
            if celula in ['x', 'X']:
                livrosPegados.append(dados.iloc[a, 2])
            else:
                livrosDeixados.append(dados.iloc[a, 2])
            a+=1

        menu = int(input(f"Foram levados {len(livrosPegados)}\nForam deixados {len(livrosDeixados)}\nQuer saber quais livros foram deixados?(1)\nQuer saber quais livros foram levados?(2)\n"))
        if menu == 1:
            print(livrosDeixados)
            escolha = int(input("Voltar ao menu(1), sair(2)"))
            livrosPegados = []
            livrosDeixados = []
            if escolha == 2: break

        elif menu == 2:
            print(livrosPegados)
            escolha = int(input("Voltar ao menu(1), sair(2)"))
            livrosPegados = []
            livrosDeixados = []
            if escolha == 2: break

        else:
            break

def procurar():
    livrosPegados = []
    livrosDeixados = []
    pagina = int(input("Quantas páginas tem no excel?\n"))-1

   
    i = 0
    while i <= pagina:
        dados = pd.read_excel("Livros.xlsx", sheet_name=i)
        h = dados.index[-1]
        a = 1
        while a <= h:
            celula = dados.iloc[a, 0]
            if celula in ['x', 'X']:
                livrosPegados.append(str(dados.iloc[a, 2]).lower())
            else:
                livrosDeixados.append(str(dados.iloc[a, 2]).lower())
            a+=1
        i += 1
    Todos = [livrosDeixados, livrosPegados]
    print(total)
    livro = input("Qual livro você quer procurar?")
    if livro in Todos and livro in livrosPegados: print(f"O livro {livro} foi levado")
    elif livro in Todos and livro in livrosDeixados: print(f"O Livro {livro} foi deixado na escola")
    else: print("Livro não encontrado")

    print(f"Total de livro {len(livrosDeixados) + len(livrosPegados)}")
    print("Livros Deixados: ",  len(livrosDeixados))
    print("Livros Levados: ", len(livrosPegados))
    


escolha = int(input("Você deseja:\nAnalisar planilha(1)\nProcurar livro(2)\nVer totais de livros(3)\n"))
if escolha == 1: analisar()
elif escolha == 2: procurar()