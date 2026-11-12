# Relatório — Mini-projeto de Hashing

## 1. Objetivo

O objetivo deste mini-projeto foi implementar um índice invertido para realizar buscas textuais de maneira eficiente, utilizando dicionários (`dict`) e conjuntos (`set`) presentes na linguagem Python.

Também foi realizado um experimento comparando o desempenho das duas estratégias de busca utilizadas, que foram: a busca por varredura completa do texto (a busca sem índice) e a busca utilizando o índice invertido implementado com os dicionários. Com a finalidade de observar os diferentes desempenhos de cada estratégia, analisando o tempo de execução para diferentes quantidades de consultas, considerando também o custo necessário para construir o índice invertido.

## 2. Metodologia

Foram implementadas quatro funções principais:

- `construir_indice(texto)`: percorre todo o texto e constrói um dicionário que relaciona cada palavra às linhas em que aparece.
- `buscar(indice, palavra)`: retorna as linhas em que a palavra escolhida aparece.
- `buscar_e(indice, palavras)`: retorna apenas as linhas que contêm todas as palavras pesquisadas, utilizando a operação de interseção de conjuntos.
- `buscar_ou(indice, palavras)`: retorna as linhas que contêm pelo menos uma das palavras pesquisadas, utilizando a operação de união de conjuntos.

O texto foi normalizado para desconsiderar diferenças entre letras maiúsculas e minúsculas e remover sinais de pontuação, preservando os acentos.

Para comparar o desempenho, foram utilizadas duas estratégias:

1. **Busca sem índice:** percorre todas as linhas do texto a cada consulta, verificando a presença da palavra.
2. **Busca com índice:** utiliza o dicionário previamente construído para localizar as ocorrências.

O experimento utilizou um texto de 400 linhas, gerado pela repetição de um conjunto de quatro linhas por 100 vezes.

Foram realizadas 1, 10, 100 e 1.000 consultas, utilizando as mesmas palavras nas duas estratégias. Cada experimento foi repetido três vezes, considerando a mediana dos tempos obtidos.

A medição foi realizada com a função `perf_counter()`, incluindo o tempo de construção do índice e o tempo das consultas.

## 3. Resultados obtidos

Os resultados foram os seguintes:

| Quantidade de consultas | Busca sem índice (s) | Construção do índice (s) | Busca com índice (s) | Total com índice (s) |
|---:|---:|---:|---:|---:|
| 1 | 0,002130 | 0,002436 | 0,000009 | 0,002446 |
| 10 | 0,019942 | 0,002253 | 0,000019 | 0,002272 |
| 100 | 0,200927 | 0,002263 | 0,000143 | 0,002406 |
| 1.000 | 2,053643 | 0,002383 | 0,001422 | 0,003805 |

O tempo total da estratégia com índice corresponde à soma do tempo de construção e do tempo das consultas.

## 4. Análise dos resultados

Os resultados demonstraram que a busca sem índice apresenta um aumento gradual significativo no tempo de execução conforme a quantidade de consultas cresce, pois o texto precisa ser percorrido novamente a cada pesquisa.

Já na busca com índice invertido, existe um custo de tempo inicial para construir a estrutura, mas as consultas posteriores são muito mais rápidas, pois utilizam o dicionário para localizar diretamente as ocorrências.

Com apenas uma consulta, a varredura completa foi ligeiramente mais rápida. Entretanto, com dez consultas, o índice invertido já apresentou vantagem.

Essa diferença ficou ainda mais evidente com 100 e 1.000 consultas. No último cenário, a busca sem índice levou aproximadamente 2,05 segundos, enquanto a estratégia com índice levou aproximadamente 0,0038 segundo, incluindo sua construção.

Portanto, neste experimento, foi possível observar que o índice invertido compensa seu custo inicial quando existe um volume maior de consultas. O ponto exato de compensação pode variar conforme o tamanho do texto, o computador utilizado e as características das consultas.

## 5. Questões teóricas

### 5.1. Qual estratégia de busca apresentou melhor desempenho?

A busca utilizando o índice invertido apresentou melhor desempenho após o aumento da quantidade de consultas. Isso acontece porque o dicionário permite localizar as ocorrências sem precisar percorrer novamente todas as linhas do texto.

A varredura completa pode ser vantajosa quando existe apenas uma consulta ou quando o custo de construção do índice não compensa.

### 5.2. A partir de quantas consultas a construção do índice compensa?

No experimento realizado, a construção do índice já compensou a partir de dez consultas. Com apenas uma consulta, a varredura completa apresentou um tempo ligeiramente menor.

Esse resultado pode variar de acordo com o tamanho do texto e as condições de execução.

### 5.3. Qual a vantagem de utilizar conjuntos (`set`) em vez de listas (`list`)?

Os conjuntos não armazenam elementos duplicados e permitem realizar operações de união e interseção diretamente.

Além disso, a verificação de pertencimento em um conjunto apresenta complexidade média O(1), enquanto em uma lista essa operação possui complexidade O(n).

Isso torna os conjuntos adequados para armazenar as linhas em que cada palavra aparece, evitando repetições e facilitando as consultas E e OU.

### 5.4. Qual a complexidade média de busca em um dicionário Python?

A busca por uma chave em um dicionário Python apresenta complexidade média O(1), pois utiliza hashing para localizar os elementos.

Entretanto, em situações desfavoráveis de colisões, o desempenho pode ser pior.

### 5.5. Qual a complexidade da construção do índice e das operações de união e interseção?

Considerando n como a quantidade de palavras processadas no texto, a construção do índice apresenta custo médio O(n), pois cada palavra é processada e inserida na estrutura.

As operações de união e interseção de conjuntos dependem da quantidade de elementos envolvidos. Em condições médias, essas operações possuem custo proporcional ao tamanho dos conjuntos percorridos.

### 5.6. Qual a principal desvantagem de utilizar um índice invertido?

A principal desvantagem é o consumo adicional de memória, pois é necessário armazenar o dicionário, suas palavras e os conjuntos contendo os números das linhas.

Além disso, existe um custo inicial de processamento para construir o índice.

## 6. Observações

Os 400 registros foram criados pela repetição de quatro linhas, portanto não representam um texto real de 400 linhas diferentes.

O ponto de compensação foi observado entre 1 e 10 consultas. Não podemos afirmar que exatamente 10 é o mínimo.

A complexidade O(1) do dicionário é uma média esperada, não uma garantia para todos os casos.

## 7. Conclusão

O desenvolvimento do projeto permitiu compreender na prática como o hashing pode melhorar a eficiência de buscas textuais.

A utilização de dicionários e conjuntos possibilitou implementar um índice invertido capaz de localizar rapidamente as linhas em que determinadas palavras aparecem.

Os experimentos demonstraram que, embora a construção do índice apresente um custo inicial, essa estratégia se torna muito mais eficiente quando várias consultas são realizadas sobre o mesmo texto.

Assim, foi possível observar a importância da escolha adequada das estruturas de dados e como elas influenciam o desempenho de um programa.