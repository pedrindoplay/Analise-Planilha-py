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
def pesquisa(dados, termo):
    resultados = []
    for item in dados:
        if termo.lower() in item.lower():
            resultados.append(item)
    return resultados

def todos(pagina):
    livrosPegados = []
    livrosDeixados = []
    Todos = []
    i = 0
    while i <= pagina-1:
        dados = pd.read_excel("Livros.xlsx", sheet_name=i)
        h = dados.index[-1]
        a = 1
        while a <= h:
            celula = dados.iloc[a, 0]
            Todos.append(str(dados.iloc[a,2]).lower())
            if celula in ['x', 'X']:
                livrosPegados.append(str(dados.iloc[a, 2]).lower())
            else:
                livrosDeixados.append(str(dados.iloc[a, 2]).lower())
            a+=1
        i += 1
    return livrosDeixados, livrosPegados, Todos

    


