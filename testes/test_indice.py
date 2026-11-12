import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from indice_invertido import (
    construir_indice,
    buscar,
    buscar_e,
    buscar_ou
)

# Testes Básicos

texto = (
    "Python e dados\n"
    "Dados e algoritmos\n"
    "Python e algoritmos"
)

indice = construir_indice(texto)

assert indice["python"] == {1, 3}
assert indice["dados"] == {1, 2}
assert indice["algoritmos"] == {2, 3}

assert buscar(indice, "python") == [1, 3]
assert buscar(indice, "java") == []

assert buscar_e(indice, ["python", "dados"]) == [1]
assert buscar_ou(indice, ["python", "dados"]) == [1, 2, 3]

print("Todos os testes passaram!")

# Testes de situações especiais

# 1. Palavras repetidas
texto = "Python Python Python"
indice = construir_indice(texto)
assert indice["python"] == {1}

# 2. Maiúsculas e minúsculas
texto = "Python PYTHON python"
indice = construir_indice(texto)
assert indice["python"] == {1}

# 3. Pontuação
texto = "Python, é legal! Python."
indice = construir_indice(texto)
assert indice["python"] == {1}
assert indice["legal"] == {1}

# 4. Linhas vazias
texto = "Python\n\nJava"
indice = construir_indice(texto)
assert indice["python"] == {1}
assert indice["java"] == {3}

# 5. Palavras inexistentes
assert buscar(indice, "C++") == []
assert buscar_e(indice, ["python", "javascript"]) == []
assert buscar_ou(indice, ["javascript"]) == []

print("Todos os testes especiais passaram!")

# Teste de pontuação e acentuação

texto = "Python—Java… é legal!"
indice = construir_indice(texto)

assert indice["python"] == {1}
assert indice["java"] == {1}
assert indice["legal"] == {1}

# Os acentos devem ser preservados
texto = "A avó viu o avo"
indice = construir_indice(texto)

assert "avó" in indice
assert "avo" in indice

print("Testes de pontuação e acentuação passaram!")