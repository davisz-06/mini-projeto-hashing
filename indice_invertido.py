import unicodedata

def construir_indice(texto):
    indice = {}

    linhas = texto.split("\n")

    for numero_linha, linha in enumerate(linhas, start=1):
        linha = "".join(
            " " if unicodedata.category(caractere).startswith("P") else caractere
            for caractere in linha
        )
        palavras = linha.split()

        for palavra in palavras:
            palavra = palavra.lower()
            if palavra not in indice:
                indice[palavra] = set()
            
            indice[palavra].add(numero_linha)

    return indice

def buscar(indice, palavra):
    palavra = palavra.lower()
    palavra_buscada = sorted(indice.get(palavra, set()))

    return palavra_buscada

def buscar_e(indice, palavras):
    if not palavras:
        return []

    resultado_busca_especifica = set(indice.get(palavras[0].lower(), set()))

    for palavra in palavras[1:]:
        resultado_busca_especifica = resultado_busca_especifica & indice.get(palavra.lower(), set())

    return sorted(resultado_busca_especifica)

def buscar_ou(indice, palavras):
    resultado_busca_geral = set()

    for palavra in palavras:
        resultado_busca_geral = resultado_busca_geral | indice.get(palavra.lower(), set())

    return sorted(resultado_busca_geral)