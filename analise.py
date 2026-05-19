import pandas as pd
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

while True:
    menu = int(input(f"Foram levados {len(livrosPegados)}\nForam deixados {len(livrosDeixados)}\nQuer saber quais livros foram deixados?(1)\nQuer saber quais livros foram levados?(2)\n"))
    if menu == 1:
        print(livrosDeixados)
        escolha = int(input("Voltar ao menu(1), sair(2)"))
        if escolha == 2: break
    elif menu == 2:
        print(livrosPegados)
        escolha = int(input("Voltar ao menu(1), sair(2)"))
        if escolha == 2: break
    else:
        break
        