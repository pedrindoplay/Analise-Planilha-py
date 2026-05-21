<h1 align="center"> Análise de Planilha </h1>
<img loading="Lazy" src="https://img.shields.io/badge/Status-Em%20desenvolvimento-green" />

### Para que serve?
Fiz esse código com a intenção de agilizar a contagens de livros que foram levados/deixados em uma troca de livros que ajudei a organizar na minha escola.

### Tecnologias utilizadas

- `Python`
- `Biblioteca Pandas`

### Como Funciona?
Para fazer uma organização melhor das trocas eu fiz uma planilha e nela fui marcando os livros que foram levados com um x do lado, com isso feito usei a biblioteca pandas para fazer um código que lê esse x e adiciona o livro em uma lista, se ele ler a célula e não tiver o x ele apenas adiciona o livro em outra lista.

***Estrutura da planilha***
<img width="1256" height="425" alt="image" src="https://github.com/user-attachments/assets/fee33177-b764-42f0-9efd-0a8cc0e6cdfd" />

### Como executar projeto
- Baixe a biblioteca Pandas
```bash
pip install pandas openpyxl
```
- Certifique que a planilha e o script estejam na mesma pasta
- Agora é só rodar
```bash
python analise.py
```

### Próximas etapas
Ajustar a pesquisa de itens, planejo colocar os livros em um dicionario em que a chave seja se ele foi ou não pegado, não sei se é uma boa ideia, mas ainda não pensei direito como vou fazer, ja que do jeito que está, o usuário teria que procurar manualmente se o livro pesquisado foi ou não levado.


