
from pathlib import Path

from indice_invertido import (
    construir_indice,
    buscar,
    buscar_e,
    buscar_ou
)


def carregar_texto():
    caminho = Path(__file__).parent / "texto.txt"

    with open(caminho, "r", encoding="utf-8") as arquivo:
        return arquivo.read()


def exibir_resultado(resultado):
    if resultado:
        print("Linhas encontradas:", resultado)
    else:
        print("Nenhuma ocorrência encontrada.")


def main():
    try:
        texto = carregar_texto()
    except FileNotFoundError:
        print("Erro: arquivo texto.txt não encontrado.")
        return

    indice = construir_indice(texto)

    while True:
        print("\n===== ÍNDICE INVERTIDO =====")
        print("1 - Buscar uma palavra")
        print("2 - Buscar com E")
        print("3 - Buscar com OU")
        print("4 - Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            palavra = input("Digite a palavra: ")
            resultado = buscar(indice, palavra)
            exibir_resultado(resultado)

        elif opcao == "2":
            palavras = input("Digite as palavras separadas por espaço: ")
            palavras = palavras.split()

            if not palavras:
                print("Informe pelo menos uma palavra.")
                continue

            resultado = buscar_e(indice, palavras)
            exibir_resultado(resultado)

        elif opcao == "3":
            palavras = input("Digite as palavras separadas por espaço: ")
            palavras = palavras.split()

            if not palavras:
                print("Informe pelo menos uma palavra.")
                continue

            resultado = buscar_ou(indice, palavras)
            exibir_resultado(resultado)

        elif opcao == "4":
            print("Encerrando o programa. Até mais!")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
