import pandas
import operacoes

# 1. Abrir o sistema.
operacoes.Open()

# 2. Fazer login.
operacoes.Login()

# 3. Abrir base de dados.
table = pandas.read_csv("./produtos.csv")

# 4. Cadastrar produtos.
for row in table.index:
  operacoes.registerProduct(table, row)