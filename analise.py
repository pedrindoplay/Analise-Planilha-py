import pandas as pd

def analisar(pagina):
    while True:
        livrosPegados = []
        livrosDeixados = []
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

        return livrosDeixados, livrosPegados

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

    


