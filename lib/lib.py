import os
import csv
from gdown import download
import numpy as np

'''
Faz o download de um arquivo a partir de um link do Google Drive.

Parâmetros:
- link (str): URL do arquivo no Google Drive.
- filename (str): Nome do arquivo a ser salvo localmente.

Retorno:
- Nenhum.

Dependências:
- Necessita do pacote `gdown` para realizar o download.

Exemplo de uso:
download_dataset("https://drive.google.com/uc?id=EXEMPLO", "dataset.txt")
'''

def download_dataset(link, filename):
    download(link, output=filename, quiet=False, fuzzy=True)

'''
Lê um arquivo de entrada contendo informações sobre contratos e preenche uma matriz tridimensional.

Parâmetros:
- nome_arquivo (str): Caminho para o arquivo de entrada.

Retorno:
- m (int): Quantidade de períodos (m).
- n (int): Número de fornecedores (n).
- t (float): Valor total (t) fornecido na primeira linha do arquivo.
- matriz (numpy.ndarray): Matriz tridimensional preenchida com os valores dos contratos.

Descrição:
- O arquivo deve ter a seguinte estrutura:
  Linha 1: m n t (separados por espaços).
  Linhas subsequentes: fornecedor, início, fim, valor.

- A matriz resultante é inicializada com valores `inf` e preenchida conforme os dados do arquivo.

Exemplo de uso:
m, n, t, matriz = preencher_matriz_contratos("dataset.txt")
'''

def preencher_matriz_contratos(nome_arquivo: str):

    with open(nome_arquivo, 'r') as file:
        lines = file.readlines()

    m, n, t = map(float, lines[0].split())
    m, n = int(m), int(n)

    matriz = np.full((n, m + 1, m + 1), float('inf'))

    for line in lines[1:]:
        fornecedor, inicio, fim, valor = map(float, line.strip().split())
        fornecedor, inicio, fim = int(fornecedor), int(inicio), int(fim)
        matriz[fornecedor - 1][inicio][fim] = valor

    return m, n, t, matriz

'''
Imprime uma matriz tridimensional no console.

Parâmetros:
- matriz (numpy.ndarray): Matriz tridimensional a ser impressa.
- k (int, opcional): Limite para o número de colunas a serem exibidas por fornecedor.

Retorno:
- Nenhum.

Descrição:
- A função exibe a matriz, organizando as informações por fornecedor. 
- Se `k` for fornecido, limita o número de colunas exibidas.

Exemplo de uso:
imprimir_matriz(matriz, k=5)
'''

def imprimir_matriz(matriz, k=None):
    for i, row in enumerate(matriz):
        if k is not None:
            row = row[:k]
        print(f"Fornecedor {i+1}: ")
        print(row)


'''
Exporta uma matriz bidimensional para um arquivo CSV.

Parâmetros:
- nome_arquivo (str): Nome do arquivo CSV a ser criado.
- matriz (numpy.ndarray): Matriz bidimensional a ser exportada.

Retorno:
- Nenhum.

Descrição:
- A matriz é gravada em um arquivo CSV, onde cada linha representa uma linha da matriz original.

Exemplo de uso:
exportar_csv("output.csv", matriz[0])
'''

def exportar_csv(nome_arquivo, matriz):
    with open(nome_arquivo, 'w', newline='') as file:
        writer = csv.writer(file)
        for row in matriz:
            writer.writerow(row)
