import numpy as np
import matplotlib.pyplot as plt

# Define a URL de um arquivo CSV contendo dados
url = 'https://raw.githubusercontent.com/alura-cursos/numpy/dados/apples_ts.csv'

# Carrega os dados do CSV a partir da URL fornecida
# 'delimiter' especifica que as colunas do CSV são separadas por vírgulas
# 'usecols' define as colunas a serem lidas (de 1 a 87, inclusive)
dado = np.loadtxt(url, delimiter=',', usecols=np.arange(1, 88, 1))

# Cria um array de datas de 1 a 87
datas = np.arange(1, 88, 1)

# Transpõe a matriz 'dado' (troca linhas por colunas)
dado_transposto = dado.T

# Extrai as colunas de 1 a 5 dos dados transpostos, que contêm os preços
precos = dado_transposto[:, 1:6]

# Extrai os preços de Moscow (primeira coluna de 'precos')
Moscow = precos[:, 0]

# Plota os preços de Moscow contra as datas
plt.plot(datas, Moscow)

# Mostra o gráfico
plt.show()

# Define a variável x como datas e y como 2*x + 80 (uma linha reta)
x = datas
y = 2 * x + 80

# Plota os preços de Moscow e a linha reta y contra as datas
plt.plot(datas, Moscow)
plt.plot(datas, y)

# Mostra o gráfico
plt.show()

# Calcula a raiz quadrada da soma dos quadrados das diferenças entre Moscow e y (erro quadrático)
print(np.sqrt(np.sum(np.power(Moscow - y, 2))))

# Redefine y como 0.52*x + 80 (outra linha reta)
y = 0.52 * x + 80
plt.plot(datas, Moscow)
plt.plot(datas, y)

# Mostra o gráfico
plt.show()

# Imprime as diferenças entre Moscow e a nova linha reta y
print(Moscow - y)

# Calcula a raiz quadrada da soma dos quadrados das diferenças entre Moscow e a nova linha reta y
print(np.sqrt(np.sum(np.power(Moscow - y, 2))))

# Calcula a norma (distância Euclidiana) entre Moscow e y
print(np.linalg.norm(Moscow - y))

# Define Y como Moscow e X como datas
Y = Moscow
X = datas
n = np.size(Moscow)  # Número de elementos em Moscow

# Imprime as formas (dimensões) de X e X**2
print(X.shape)
print((X**2).shape)

# Calcula a inclinação (a) e a interseção (b) da linha de melhor ajuste (regressão linear)
a = (n * np.sum(X * Y) - np.sum(X) * np.sum(Y)) / (n * np.sum(X**2) - np.sum(X)**2)
b = np.mean(Y) - a * np.mean(X)

# Calcula os valores de y usando a linha de melhor ajuste
y = a * X + b

# Calcula a norma (distância Euclidiana) entre Moscow e a linha de melhor ajuste y
print(np.linalg.norm(Moscow - y))

# Plota os preços de Moscow e a linha de melhor ajuste y contra as datas
plt.plot(datas, Moscow)
plt.plot(datas, y)

# Mostra o gráfico
plt.show()

# Plota os preços de Moscow e a linha de melhor ajuste y contra as datas
# Plota dois pontos destacados na linha de melhor ajuste: um em x=41.5 e outro em x=100
plt.plot(datas, Moscow)
plt.plot(datas, y)
plt.plot(41.5, a * 41.5 + b, '*r')  # Ponto em x=41.5
plt.plot(100, a * 100 + b, '*r')  # Ponto em x=100

# Mostra o gráfico
plt.show()
