import numpy as np

# Define a URL de um arquivo CSV contendo dados
url = 'https://raw.githubusercontent.com/alura-cursos/numpy/dados/apples_ts.csv'

# Carrega os dados do CSV a partir da URL fornecida
# 'delimiter' especifica que as colunas do CSV são separadas por vírgulas
# 'usecols' define as colunas a serem lidas (de 1 a 87, inclusive)
dado = np.loadtxt(url, delimiter=',', usecols=np.arange(1, 88, 1))

# Transpõe a matriz 'dado' (troca linhas por colunas)
dado_transposto = dado.T

# Extrai a primeira coluna dos dados transpostos, que contém as datas
datas = dado_transposto[:, 0]
print(datas)

# Extrai as colunas de 1 a 5 dos dados transpostos, que contêm os preços
precos = dado_transposto[:, 1:6]
print(precos)

import matplotlib.pyplot as plt

# Plota os preços da primeira coluna contra as datas
plt.plot(datas, precos[:, 0])

# Mostra o gráfico
plt.show()

# Redefine as datas como um array de valores de 1 a 87 (inclusive)
datas = np.arange(1, 88, 1)
print(datas)

# Plota os preços da primeira coluna contra as novas datas
plt.plot(datas, precos[:, 0])

# Mostra o gráfico
plt.show()

# Extrai os preços de diferentes cidades
Moscow = precos[:, 0]
Kaliningrad = precos[:, 1]
Petersburg = precos[:, 2]
Krasnodar = precos[:, 3]
Ekaterinburg = precos[:, 4]

# Imprime a forma do array 'Moscow'
print(Moscow.shape)

# Divide os preços de Moscow em quatro anos (cada ano com 12 meses)
Moscow_ano1 = Moscow[0:12]
Moscow_ano2 = Moscow[12:24]
Moscow_ano3 = Moscow[24:36]
Moscow_ano4 = Moscow[36:48]

# Plota os preços de Moscow para cada ano
plt.plot(np.arange(1, 13, 1), Moscow_ano1)
plt.plot(np.arange(1, 13, 1), Moscow_ano2)
plt.plot(np.arange(1, 13, 1), Moscow_ano3)
plt.plot(np.arange(1, 13, 1), Moscow_ano4)
plt.legend(['ano1', 'ano2', 'ano3', 'ano4'])

# Mostra o gráfico
plt.show()

# Compara os preços de Moscow no terceiro e quarto anos para verificar se são iguais
print(np.array_equal(Moscow_ano3, Moscow_ano4))
print(np.allclose(Moscow_ano3, Moscow_ano4, 10))

# Plota os preços de Kaliningrad contra as datas
plt.plot(datas, Kaliningrad)

# Mostra o gráfico
plt.show()

# Verifica se há valores NaN (Not a Number) em 'Kaliningrad'
print(np.isnan(Kaliningrad))
print(Kaliningrad)

# Conta o número de valores NaN em 'Kaliningrad'
print(sum(np.isnan(Kaliningrad)))

# Calcula a média dos preços de Kaliningrad nos índices 3 e 5
print((Kaliningrad[3] + Kaliningrad[5]) / 2)
print(np.mean([Kaliningrad[3], Kaliningrad[5]]))

# Substitui o valor NaN no índice 4 pela média dos valores nos índices 3 e 5
Kaliningrad[4] = np.mean([Kaliningrad[3], Kaliningrad[5]])

# Calcula a média dos preços de Moscow
print(np.mean(Moscow))

# Calcula a média dos preços de Kaliningrad
print(np.mean(Kaliningrad))
