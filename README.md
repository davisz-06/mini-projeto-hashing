# Mini-projeto: Índice Invertido com Hashing

Projeto desenvolvido para a disciplina de Estrutura de Dados, com o objetivo de implementar um índice invertido utilizando tabelas hash em Python.

## Funcionalidades

- Construção de índice invertido a partir de um texto.
- Busca simples de palavras.
- Busca com operador E (interseção).
- Busca com operador OU (união).
- Desconsideração de maiúsculas, minúsculas e pontuação.
- Preservação dos acentos.
- Identificação das linhas em que cada palavra aparece.

## Arquivos

- `indice_invertido.py`: implementação das funções principais.
- `main.py`: interface interativa no terminal.
- `texto.txt`: texto utilizado como entrada (Dom Casmurro).
- `experimentos.py`: comparação entre busca sequencial e busca com índice.
- `relatorio.md`: resultados e análise dos experimentos.
- `testes/`: testes de validação da implementação.
- `diario_de_bordo.md`: registro do desenvolvimento e da utilização de IA.

## Como executar

1. Certifique-se de ter Python instalado.
2. Execute `main.py`:

```bash
python main.py
```

3. Utilize o menu para realizar as buscas.

Para executar os experimentos:

```bash
python experimentos.py
```