from lib import download_dataset
from lib import preencher_matriz_contratos
from lib import imprimir_matriz
from lib import exportar_csv

def main():
    

    link_txt = "https://drive.google.com/uc?id=1YjPaHv8aAVsXNzhHxum5gyUDFfY5iw1_"
    file_txt = 'dataset/entrada.txt'

    download_dataset(link_txt,file_txt)

    m, n, t, matriz = preencher_matriz_contratos(file_txt)

    print(m, n, t, "\n")

    imprimir_matriz(matriz)

    file_csv = "resultados/contratos.csv"
    
    exportar_csv(file_csv, matriz)
    
if __name__ == "__main__":
    main()