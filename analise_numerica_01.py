import numpy as np

# Define a URL de um arquivo CSV contendo dados
url = 'https://raw.githubusercontent.com/alura-cursos/numpy/dados/apples_ts.csv'

# Gerar uma matriz (vetor) de valores de 1 a 87 (inclusive)
valores = np.arange(1, 88, 1)

# Imprimir a matriz de valores gerada
print(valores)

# Carregar os dados do CSV a partir da URL especificada.
# 'delimiter' define o delimitador usado no CSV (neste caso, uma vírgula).
# 'usecols' define as colunas a serem lidas (de 1 a 87, inclusive).
dado = np.loadtxt(url, delimiter=',', usecols=np.arange(1, 88, 1))

# Imprimir o número de dimensões da matriz carregada
print(dado.ndim)

# Imprimir o número total de elementos na matriz
print(dado.size)

# Imprimir a forma (dimensões) da matriz
print(dado.shape)

# Imprimir a transposta da matriz
print(dado.T)

# Imprimir a forma da matriz transposta
print(dado.T.shape)
