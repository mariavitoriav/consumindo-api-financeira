# Lista de exercícios - Consumindo api financeira
1. Crie um programa em Python que consuma os dados de moedas (currencies) da [API Financeira da HG Brasil](https://hgbrasil.com/status/finance). Seu Programa deverá ler do usuário um valor financeiro qualquer fornecido sempre em reais (R$), e convertê-lo para Euro (EUR) e Dólares (USD); a partir dos dados fornecidos pela API. 

2. Pesquise sobre o [SGBD SQLite](https://www.sqlite.org/index.html) e a [biblioteca Python](https://docs.python.org/3/library/sqlite3.html) Em seguida, faça: 
    - Usando a Ferramenta [DB Browser](https://sqlitebrowser.org/) crie um esquema de banco de dados chamado: **cotacoes**; dentro da pasta raiz **data/cotacoes.db** do projeto do exercício anterior. Em seguida, crie uma tabela chamada Cotacao, para armazenar o valor da cotação do Dólar, Euro e a data e hora da consulta.
    - Implemente a funcionalidade de persistência de dados no exercício anterior, para que toda vez que o programa for  executado as informações de cotações do Dólar e Euro, bem como a data e hora da consulta, sejam armazenadas no banco de dados.
