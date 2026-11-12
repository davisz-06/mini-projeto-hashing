# Diário de Bordo — Utilização de Inteligência Artificial

**Projeto:** Índice Invertido utilizando Hashing  
**Disciplina:** Estrutura de Dados  
**Ferramenta de IA utilizada:** ChatGPT (OpenAI)

## 1. Introdução

Durante o desenvolvimento do mini-projeto de hashing, foi utilizada a ferramenta ChatGPT como apoio ao processo de aprendizagem, planejamento, implementação e validação do código.

A utilização da inteligência artificial teve como principal objetivo auxiliar na compreensão dos conceitos envolvidos, esclarecer dúvidas, apresentar exemplos, propor exercícios e orientar a identificação e correção de possíveis falhas durante o desenvolvimento.

O projeto foi desenvolvido de maneira gradual, buscando compreender o funcionamento de cada estrutura e função implementada, em vez de simplesmente utilizar soluções prontas.

A IA foi utilizada como uma ferramenta de apoio, enquanto a implementação, execução dos testes, análise dos resultados e compreensão do funcionamento do programa fizeram parte das atividades realizadas pelo estudante.

## 2. Planejamento e preparação para o projeto

Inicialmente, foi solicitado auxílio para compreender o projeto proposto pelo professor e organizar uma sequência de aprendizagem que permitisse desenvolver a atividade mesmo sem conhecimento prévio aprofundado sobre hashing.

Foi elaborado um roteiro de estudos progressivo, começando pelos conceitos fundamentais e avançando gradualmente para a implementação do índice invertido.

O planejamento contemplou:

- Compreensão do funcionamento do hashing.
- Estudo dos dicionários (`dict`) em Python.
- Estudo dos conjuntos (`set`).
- Compreensão das operações de união e interseção.
- Entendimento da estrutura de um índice invertido.
- Implementação das funções exigidas pelo projeto.
- Realização de testes.
- Comparação de desempenho entre diferentes estratégias de busca.

A proposta foi dividir o projeto em pequenas etapas, permitindo compreender cada conceito antes de avançar para o seguinte.

## 3. Estudo dos conceitos fundamentais

Durante a preparação, foram utilizadas explicações teóricas, exemplos práticos e analogias para facilitar a compreensão dos conceitos relacionados ao hashing.

Foram abordados os seguintes assuntos:

### 3.1. Hashing

A IA explicou o conceito de hashing, seu funcionamento geral e sua utilização para localizar informações de maneira eficiente.

Também foi apresentada a relação entre hashing e estruturas como os dicionários Python, que utilizam esse mecanismo internamente.

### 3.2. Dicionários (`dict`)

Foram estudadas as estruturas de chave e valor, a inserção de elementos, a consulta por chaves e o método `.get()`.

A aprendizagem foi direcionada para compreender como os dicionários poderiam relacionar palavras às linhas em que aparecem no texto.

### 3.3. Conjuntos (`set`)

Foi introduzido o conceito de conjuntos, destacando a característica de não permitir elementos duplicados.

Foram realizados exemplos para compreender como essa propriedade seria útil no projeto, principalmente para evitar que uma mesma linha aparecesse repetidamente nas ocorrências de uma palavra.

### 3.4. União e interseção

Foram estudadas as operações:

- União (`|`): reúne os elementos presentes em pelo menos um dos conjuntos.
- Interseção (`&`): mantém apenas os elementos presentes em todos os conjuntos envolvidos.

Essas operações foram relacionadas diretamente às consultas OU e E exigidas pelo projeto.

## 4. Desenvolvimento do índice invertido

Após compreender os conceitos fundamentais, iniciou-se a implementação do arquivo `indice_invertido.py`.

O desenvolvimento foi realizado gradualmente, começando pela função `construir_indice(texto)`.

### 4.1. Construção do índice

A IA orientou a organização da função e explicou o funcionamento de recursos como:

- `split("\n")`, para separar o texto em linhas.
- `enumerate()`, para percorrer as linhas com numeração iniciada em 1.
- `lower()`, para padronizar as palavras.
- `set()`, para armazenar as ocorrências sem duplicação.
- `add()`, para inserir os números das linhas nos conjuntos.

A implementação foi testada com textos próprios, incluindo situações de palavras repetidas e linhas vazias.

Os resultados foram analisados para verificar se a numeração das linhas e o armazenamento das ocorrências estavam corretos.

### 4.2. Implementação da busca simples

Em seguida, foi desenvolvida a função `buscar(indice, palavra)`.

Foram utilizadas as operações de consulta ao dicionário e ordenação dos resultados com `sorted()`.

Também foram testadas pesquisas com letras maiúsculas, minúsculas e palavras inexistentes.

### 4.3. Implementação da busca E

Para a função `buscar_e(indice, palavras)`, foi estudada a utilização da interseção de conjuntos.

A IA explicou como iniciar o resultado com as ocorrências da primeira palavra e, posteriormente, realizar a interseção com os conjuntos das demais palavras.

Também foi discutida a importância de não modificar os conjuntos armazenados originalmente no índice.

### 4.4. Implementação da busca OU

Na função `buscar_ou(indice, palavras)`, foi utilizada a operação de união.

Durante essa etapa, foi discutido como reunir as ocorrências de diferentes palavras em um único conjunto, evitando duplicações e ordenando os resultados antes de retorná-los.

As funções foram organizadas de acordo com as assinaturas exigidas pelo professor.

## 5. Testes, identificação de falhas e melhorias

Durante o desenvolvimento, foram realizados testes progressivos para verificar o comportamento das funções.

A IA sugeriu casos de teste, explicou os resultados esperados e auxiliou na análise de possíveis problemas.

Entre as situações verificadas, destacam-se:

- Palavras repetidas na mesma linha.
- Diferenças entre letras maiúsculas e minúsculas.
- Palavras inexistentes no índice.
- Linhas vazias.
- Pontuação.
- Preservação de palavras acentuadas.
- Diferença entre palavras com e sem acento.

Foram utilizados comandos `assert` para verificar automaticamente se os resultados obtidos correspondiam aos esperados.

Também foi realizada uma melhoria no tratamento da pontuação. Inicialmente, foi utilizada a biblioteca `string`, mas posteriormente a implementação foi aprimorada com `unicodedata`, permitindo reconhecer diferentes categorias de pontuação e substituí-las por espaços.

Essa alteração também evitou que palavras separadas por sinais de pontuação fossem unidas indevidamente.

Todos os testes realizados nessa etapa foram aprovados.

## 6. Implementação da busca sem índice

Com as funções principais funcionando, iniciou-se a implementação de uma segunda estratégia de busca.

Foi criado o arquivo `experimentos.py`, contendo a função `buscar_sem_indice(texto, palavra)`.

A IA explicou a diferença entre consultar diretamente o índice invertido e percorrer todas as linhas do texto a cada pesquisa.

A função foi desenvolvida utilizando:

- Separação do texto em linhas.
- Percorrimento sequencial com `enumerate()`.
- Normalização das palavras.
- Verificação de pertencimento com `in`.
- Armazenamento das linhas encontradas em uma lista.

Foram realizados testes com palavras existentes e inexistentes.

Os resultados foram:

- Busca por Python: `[1, 3]`
- Busca por Java: `[2]`
- Busca por JavaScript: `[]`

Os resultados foram considerados corretos.

## 7. Experimentos e comparação de desempenho

Após implementar as duas estratégias, foi desenvolvido um experimento para comparar seus tempos de execução.

A IA auxiliou na utilização de `perf_counter()` para medir o tempo e de `median()` para calcular a mediana de três execuções.

Foi utilizado um texto de 400 linhas, gerado pela repetição de quatro linhas de exemplo.

Foram realizadas comparações com 1, 10, 100 e 1.000 consultas.

O experimento considerou:

- Tempo de busca sem índice.
- Tempo de construção do índice.
- Tempo de busca com índice.
- Tempo total da estratégia com índice.

Os resultados obtidos foram:

| Consultas | Sem índice (s) | Construção (s) | Com índice (s) | Total com índice (s) |
|---:|---:|---:|---:|---:|
| 1 | 0,002130 | 0,002436 | 0,000009 | 0,002446 |
| 10 | 0,019942 | 0,002253 | 0,000019 | 0,002272 |
| 100 | 0,200927 | 0,002263 | 0,000143 | 0,002406 |
| 1.000 | 2,053643 | 0,002383 | 0,001422 | 0,003805 |

A IA auxiliou na interpretação dos resultados, destacando a importância de considerar o custo inicial de construção do índice.

Foi observado que a busca sem índice apresentou aumento significativo no tempo conforme o número de consultas cresceu, enquanto a estratégia com índice apresentou melhor desempenho a partir de dez consultas no experimento realizado.

## 8. Elaboração do relatório

Após a realização dos experimentos, a IA auxiliou na organização dos resultados e na elaboração do relatório.

Foram abordados:

- Objetivo e metodologia do experimento.
- Apresentação dos resultados.
- Comparação entre as estratégias.
- Análise do ponto em que a construção do índice passa a compensar.
- Vantagens da utilização de conjuntos.
- Complexidade média de busca em dicionários.
- Complexidade da construção do índice e das operações entre conjuntos.
- Desvantagens relacionadas ao consumo de memória.

A análise foi baseada nos resultados efetivamente obtidos durante a execução do programa.

## 9. Forma de utilização da inteligência artificial

Ao longo do projeto, a inteligência artificial foi utilizada principalmente para:

- Organizar o roteiro de aprendizagem.
- Explicar conceitos teóricos.
- Apresentar exemplos e analogias.
- Elaborar questões de fixação.
- Orientar a implementação gradual das funções.
- Explicar comandos e estruturas da linguagem Python.
- Sugerir testes e situações especiais.
- Auxiliar na identificação e correção de falhas.
- Orientar a comparação de desempenho.
- Auxiliar na organização e interpretação do relatório.

A utilização ocorreu de maneira interativa. Em diversas etapas, foram apresentados códigos desenvolvidos pelo estudante para revisão, permitindo discutir sua lógica, identificar possíveis falhas e realizar melhorias.

As sugestões da IA foram verificadas por meio da execução do código e da análise dos resultados obtidos no ambiente de desenvolvimento.

## 10. Considerações finais

A utilização da inteligência artificial contribuiu para tornar o desenvolvimento do projeto mais organizado e gradual.

O principal benefício foi poder utilizar a ferramenta não apenas para obter respostas, mas também como apoio ao estudo e à compreensão dos conceitos envolvidos.

O processo permitiu avançar desde os fundamentos de hashing, dicionários e conjuntos até a implementação de um índice invertido funcional e a realização de experimentos de desempenho.

A experiência também demonstrou a importância de testar o código, compreender as operações utilizadas e analisar criticamente as soluções sugeridas pela IA.

O desenvolvimento do projeto proporcionou uma oportunidade de aplicar, na prática, conceitos estudados na disciplina de Estrutura de Dados.