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

# Define Y como Moscow e X como datas
Y = Moscow
X = datas
n = np.size(Moscow)  # Número de elementos em Moscow

# Calcula a inclinação (a) e a interseção (b) da linha de melhor ajuste (regressão linear)
a = (n * np.sum(X * Y) - np.sum(X) * np.sum(Y)) / (n * np.sum(X**2) - np.sum(X)**2)
b = np.mean(Y) - a * np.mean(X)

# Calcula os valores de y usando a linha de melhor ajuste
y = a * X + b

# Gera um array de 100 números inteiros aleatórios entre 40 e 100
print(np.random.randint(low=40, high=100, size=100))

# Gera um array de 100 coeficientes angulares aleatórios entre 0.10 e 0.90
coef_angulares = np.random.uniform(low=0.10, high=0.90, size=100)

# Imprime o valor da interseção 'b'
print(b)

# Inicializa um array vazio para armazenar as normas
norma = np.array([])

# Calcula a norma (distância Euclidiana) entre Moscow e as linhas geradas por coeficientes angulares aleatórios
for i in range(100):
    norma = np.append(norma, np.linalg.norm(Moscow - (coef_angulares[i] * X + b)))

# Imprime as normas calculadas
print(norma)

# Imprime o quarto coeficiente angular do array (índice 3)
print(coef_angulares[3])

# Gera outro array de 100 coeficientes angulares aleatórios entre 0.10 e 0.90 e imprime
print(np.random.uniform(low=0.10, high=0.90, size=100))

# Define uma semente aleatória para reprodutibilidade
np.random.seed(16)
# Gera novamente um array de 100 coeficientes angulares aleatórios entre 0.10 e 0.90 e imprime
print(np.random.uniform(low=0.10, high=0.90, size=100))

# Inicializa um array vazio para armazenar as normas novamente
norma = np.array([])

# Define uma semente aleatória diferente para reprodutibilidade
np.random.seed(84)
# Gera novamente um array de 100 coeficientes angulares aleatórios entre 0.10 e 0.90
coef_angulares = np.random.uniform(low=0.10, high=0.90, size=100)

# Calcula novamente a norma entre Moscow e as linhas geradas pelos novos coeficientes angulares aleatórios
for i in range(100):
    norma = np.append(norma, np.linalg.norm(Moscow - (coef_angulares[i] * X + b)))

# Combina as normas e coeficientes angulares em uma única matriz com 2 colunas
dados = np.column_stack([norma, coef_angulares])

# Imprime a forma (dimensões) da matriz 'dados'
print(dados.shape)

# Salva a matriz 'dados' em um arquivo CSV
np.savetxt('dados.csv', dados, delimiter=',')
