import unicodedata
from time import perf_counter
from statistics import median

from indice_invertido import construir_indice, buscar

def buscar_sem_indice(texto, palavra):
    palavra_buscada = []
    linhas = texto.split("\n")

    palavra = palavra.lower()

    for numero_linha, linha in enumerate(linhas, start=1):

        linha = "".join(
            " " if unicodedata.category(caractere).startswith("P") else caractere
            for caractere in linha
        )

        palavras = linha.lower().split()

        if palavra in palavras:
            palavra_buscada.append(numero_linha)

    return palavra_buscada

texto_base = """Python é uma linguagem de programação
Estruturas de dados são fundamentais
Python possui diversas estruturas de dados
Algoritmos utilizam boas estruturas"""

texto_grande = "\n".join(texto_base.split("\n") * 100)

consultas_base = [
    "python",
    "dados",
    "algoritmos",
    "programação",
    "javascript"
]

for quantidade in [1, 10, 100, 1000]:

    consultas = [
        consultas_base[i % len(consultas_base)]
        for i in range(quantidade)
    ]

    tempos_varredura = []
    tempos_construcao = []
    tempos_busca_indice = []

    for repeticao in range(3):

        # Busca sem índice
        inicio = perf_counter()

        for palavra in consultas:
            buscar_sem_indice(texto_grande, palavra)

        fim = perf_counter()
        tempos_varredura.append(fim - inicio)

        # Construção do índice
        inicio = perf_counter()
        indice = construir_indice(texto_grande)
        fim = perf_counter()

        tempos_construcao.append(fim - inicio)

        # Buscas utilizando o índice
        inicio = perf_counter()

        for palavra in consultas:
            buscar(indice, palavra)

        fim = perf_counter()
        tempos_busca_indice.append(fim - inicio)

    tempo_varredura = median(tempos_varredura)
    tempo_construcao = median(tempos_construcao)
    tempo_busca_indice = median(tempos_busca_indice)

    tempo_total_indice = tempo_construcao + tempo_busca_indice

    print(f"\nConsultas: {quantidade}")
    print(f"Busca sem índice: {tempo_varredura:.6f} segundos")
    print(f"Construção do índice: {tempo_construcao:.6f} segundos")
    print(f"Busca com índice: {tempo_busca_indice:.6f} segundos")
    print(f"Total com índice: {tempo_total_indice:.6f} segundos")