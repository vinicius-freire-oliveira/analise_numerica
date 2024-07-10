import numpy as np
import matplotlib.pyplot as plt

# Define a URL de um arquivo CSV contendo dados
url = 'https://raw.githubusercontent.com/allanspadini/numpy/dados/citrus.csv'

# Carrega os dados do CSV a partir da URL fornecida
# 'delimiter' especifica que as colunas do CSV são separadas por vírgulas
# 'usecols' define as colunas a serem lidas (de 1 a 5, inclusive)
# 'skiprows' pula a primeira linha (cabeçalho)
dado = np.loadtxt(url, delimiter=',', usecols=np.arange(1, 6, 1), skiprows=1)

# Imprime os dados carregados para verificação
print(dado)

# Divide os dados em dois grupos: laranjas e toranjas
diametro_laranja = dado[:5000, 0]  # Diâmetro das laranjas (primeira coluna, primeiras 5000 linhas)
diametro_toranja = dado[5000:, 0]  # Diâmetro das toranjas (primeira coluna, linhas restantes)
peso_laranja = dado[:5000, 1]  # Peso das laranjas (segunda coluna, primeiras 5000 linhas)
peso_toranja = dado[5000:, 1]  # Peso das toranjas (segunda coluna, linhas restantes)

# Plota o diâmetro vs. peso para laranjas e toranjas
plt.plot(diametro_laranja, peso_laranja)
plt.plot(diametro_toranja, peso_toranja)

# Mostra o gráfico
plt.show()

# Regressão linear para as laranjas
Y = peso_laranja
X = diametro_laranja
n = np.size(X)  # Número de elementos em X

# Calcula a inclinação (a) da linha de melhor ajuste para as laranjas
a = (n * np.sum(X * Y) - np.sum(X) * np.sum(Y)) / (n * np.sum(X**2) - np.sum(X)**2)
print(a)

# Calcula a interseção (b) da linha de melhor ajuste para as laranjas
b = np.mean(Y) - a * np.mean(X)
print(b)

# Regressão linear para as toranjas
Y = peso_toranja
X = diametro_toranja
n = np.size(X)  # Número de elementos em X

# Calcula a inclinação (a) da linha de melhor ajuste para as toranjas
a = (n * np.sum(X * Y) - np.sum(X) * np.sum(Y)) / (n * np.sum(X**2) - np.sum(X)**2)
print(a)

# Calcula a interseção (b) da linha de melhor ajuste para as toranjas
b = np.mean(Y) - a * np.mean(X)
print(b)

# Define a interseção 'b' manualmente como 17
b = 17

# Inicializa um array vazio para armazenar as normas
norma = np.array([])

# Define uma semente aleatória para reprodutibilidade
np.random.seed(84)

# Gera um array de 100 coeficientes angulares aleatórios entre 0.0 e 30.0
coef_angulares = np.random.uniform(low=0.0, high=30.0, size=100)

# Calcula a norma (distância Euclidiana) entre peso_toranja e as linhas geradas por coeficientes angulares aleatórios
for i in range(100):
    norma = np.append(norma, np.linalg.norm(Y - (coef_angulares[i] * X + b)))

# Imprime as normas calculadas
print(norma)

# Imprime a menor norma encontrada
print(np.min(norma))

# Imprime o coeficiente angular correspondente à menor norma
print(coef_angulares[norma == np.min(norma)])
