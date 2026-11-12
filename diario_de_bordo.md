# Diário de Bordo — Mini-projeto: Índice Invertido com Hashing

**Professor:** Ricardo Rubens 
**Aluno:** Davi Lima de Oliveira 
**Disciplina:** Estrutura de Dados   
**Curso:** Bacharelado em Sistemas de Informação  
**Instituição:** Instituto Federal de Alagoas (IFAL)
**Tecnologia utilizada:** Python  
**Período de desenvolvimento:** 10 a 12 de novembro de 2026  
**Recurso de apoio:** Inteligência Artificial (ChatGPT)

---

## 1. Apresentação

Este diário registra o processo de desenvolvimento do mini-projeto de implementação de um índice invertido utilizando hashing em Python.

O projeto teve como objetivo desenvolver um mecanismo de busca textual capaz de identificar as linhas em que determinadas palavras aparecem, utilizando dicionários e conjuntos para otimizar as consultas.

A inteligência artificial foi utilizada como ferramenta de apoio durante o desenvolvimento, principalmente para explicar conceitos, propor exercícios, esclarecer dúvidas, auxiliar na identificação de erros e sugerir testes. As orientações foram verificadas por meio da implementação e da execução dos códigos no computador.

## 2. Registro cronológico

### 10/11/2026 — Início do projeto e aprendizagem dos conceitos

O desenvolvimento começou com a criação da pasta do projeto, denominada `Mini-projeto Hashing`, e do arquivo `indice_invertido.py`.

Como ainda não havia familiaridade suficiente com a aplicação prática de hashing nesse contexto, o primeiro passo foi estudar os conceitos necessários.

Com o auxílio da IA, foi elaborado um roteiro de aprendizagem progressivo, abordando:

- O conceito de hashing e sua aplicação em buscas.
- A utilização de dicionários Python como tabelas hash.
- O armazenamento de valores em conjuntos (`set`).
- A utilização de `split()` para separar palavras.
- A utilização de `enumerate()` para percorrer linhas e identificar seus números.
- A importância de transformar palavras para letras minúsculas.

Após compreender os conceitos iniciais, começou a implementação da função `construir_indice(texto)`.

A função foi desenvolvida gradualmente, permitindo compreender como cada palavra é associada a um conjunto de números de linha. Também foram discutidas as vantagens de utilizar conjuntos para evitar ocorrências duplicadas.

### 11/11/2026 — Implementação das buscas e testes

Nesta etapa, o desenvolvimento avançou para as funções de consulta:

- `buscar(indice, palavra)`: realiza a busca de uma palavra.
- `buscar_e(indice, palavras)`: utiliza a interseção de conjuntos para encontrar linhas que contenham todas as palavras pesquisadas.
- `buscar_ou(indice, palavras)`: utiliza a união de conjuntos para encontrar linhas que contenham pelo menos uma das palavras pesquisadas.

Durante a implementação, foram realizadas explicações e revisões sobre o funcionamento das operações com conjuntos.

Também foram executados testes para verificar o comportamento das funções em diferentes situações.

**Testes realizados:**

1. Testes básicos fornecidos pelo professor.
2. Palavras repetidas na mesma linha.
3. Diferenças entre letras maiúsculas e minúsculas.
4. Buscas por palavras inexistentes.
5. Linhas vazias e preservação da numeração original.
6. Acentuação, verificando que palavras como `avó` e `avo` permanecem distintas.
7. Pontuação, incluindo sinais como travessões e reticências.

Durante os testes, foi identificada a necessidade de melhorar o tratamento da pontuação. Inicialmente, foi utilizada a biblioteca `string`, mas a implementação foi aprimorada com `unicodedata`, permitindo identificar diferentes categorias de sinais de pontuação Unicode.

Essa alteração também evitou que palavras separadas por pontuação fossem acidentalmente unidas.

Após os ajustes, os testes foram executados novamente e apresentaram os resultados esperados.

### 11/11/2026 — Comparação entre busca sequencial e busca indexada

Com as funções principais implementadas, iniciou-se a parte experimental do projeto.

Foi criada a função `buscar_sem_indice(texto, palavra)`, responsável por percorrer o texto linha por linha e verificar a ocorrência de uma palavra sem utilizar o índice invertido.

Em seguida, foi preparado um experimento utilizando um texto de 400 linhas, construído pela repetição de quatro linhas de exemplo.

As duas estratégias foram comparadas utilizando as mesmas consultas.

Foram utilizadas as ferramentas:

- `time.perf_counter()` para medir os tempos de execução.
- `median()` da biblioteca `statistics` para calcular a mediana.
- Três execuções para cada quantidade de consultas.

As quantidades avaliadas foram 1, 10, 100 e 1.000 consultas.

Os resultados demonstraram que a busca sem índice apresentou vantagem na primeira consulta, devido ao custo inicial de construção do índice. Entretanto, conforme a quantidade de consultas aumentou, a estratégia indexada passou a apresentar desempenho superior, mesmo considerando o tempo de construção.

A partir dos resultados, foi possível compreender na prática a importância de analisar não apenas o custo de uma consulta isolada, mas também o custo total de utilização de uma estrutura de dados.

### 11/11/2026 — Elaboração do relatório

Com os experimentos concluídos, foi elaborado o relatório do projeto.

O documento reuniu:

- Objetivo e metodologia.
- Resultados das medições.
- Comparação entre as estratégias.
- Análise do ponto em que a indexação passa a ser vantajosa.
- Discussão sobre conjuntos, dicionários e complexidade.
- Considerações sobre o consumo de memória.

Os resultados registrados foram:

| Consultas | Busca sem índice (s) | Construção do índice (s) | Busca indexada (s) | Total indexado (s) |
|---:|---:|---:|---:|---:|
| 1 | 0,002130 | 0,002436 | 0,000009 | 0,002446 |
| 10 | 0,019942 | 0,002253 | 0,000019 | 0,002272 |
| 100 | 0,200927 | 0,002263 | 0,000143 | 0,002406 |
| 1.000 | 2,053643 | 0,002383 | 0,001422 | 0,003805 |

Os resultados indicaram que, nesse experimento, o custo de construção do índice já foi compensado entre 1 e 10 consultas.

### 12/11/2026 — Desenvolvimento da interface principal

Nesta etapa, foi desenvolvido o arquivo `main.py`, responsável por permitir a utilização do projeto por meio de um menu interativo no terminal.

Foram implementadas as seguintes opções:

1. Buscar uma palavra.
2. Buscar utilizando o operador E.
3. Buscar utilizando o operador OU.
4. Encerrar o programa.

Também foram organizadas funções auxiliares para carregar o texto do arquivo `texto.txt` e apresentar os resultados das consultas.

Foi incluído tratamento para situações como arquivo não encontrado, opção inválida e consulta sem palavras informadas.

Após a implementação, o programa foi executado e testado.

Foram verificadas buscas simples, consultas combinadas e pesquisas por palavras inexistentes. Todos os testes realizados apresentaram os resultados esperados.

### 12/11/2026 — Utilização de Dom Casmurro

Para trabalhar com um texto literário real, foi utilizado o livro *Dom Casmurro*, de Machado de Assis, disponibilizado em domínio público.

O conteúdo foi colocado no arquivo `texto.txt`, substituindo o pequeno texto utilizado inicialmente para validar o programa.

Essa mudança permitiu utilizar uma obra extensa como entrada para o mecanismo de busca, tornando a demonstração mais próxima de uma aplicação real.

### 12/11/2026 — Organização e publicação no GitHub

Após a conclusão da implementação e dos testes, iniciou-se a preparação do projeto para entrega.

Foi criado o arquivo `README.md`, contendo a apresentação do projeto, suas funcionalidades, a organização dos arquivos e as instruções de execução.

Também foi criada a pasta `testes`, separando os testes das funções principais.

Em seguida, foi instalado e configurado o Git no computador. Durante essa etapa, foram aprendidos comandos importantes:

- `git init`: inicializa um repositório.
- `git add .`: prepara os arquivos para registro.
- `git status`: verifica a situação dos arquivos.
- `git commit`: registra uma versão do projeto.
- `git remote`: configura o repositório remoto.
- `git push`: envia os commits ao GitHub.

Durante a organização, foi identificado que arquivos temporários da pasta `__pycache__` não deveriam ser publicados. Para evitar isso, foi criado o arquivo `.gitignore`.

O projeto foi então enviado ao repositório:

**https://github.com/davisz-06/mini-projeto-hashing**

Durante a primeira tentativa de publicação, o GitHub bloqueou o envio porque o commit continha um endereço de e-mail marcado como privado.

O problema foi resolvido configurando o endereço `noreply` fornecido pelo próprio GitHub no Git e atualizando a identificação do commit.

Após uma nova tentativa, o envio foi concluído. A publicação foi conferida no navegador, verificando que os arquivos estavam disponíveis no repositório.

## 3. Utilização da inteligência artificial

A inteligência artificial foi utilizada durante diferentes etapas do desenvolvimento, funcionando como uma ferramenta de apoio ao aprendizado.

As principais formas de utilização foram:

- Explicação de conceitos de hashing, dicionários e conjuntos.
- Organização de um roteiro de aprendizagem progressivo.
- Apresentação de exemplos e exercícios para fixação.
- Orientação durante a implementação das funções.
- Revisão de trechos de código e identificação de possíveis erros.
- Sugestão de casos de teste, incluindo situações especiais.
- Explicação dos resultados dos experimentos.
- Apoio na organização do relatório, README e diário de bordo.
- Orientação na utilização do Git e na publicação do projeto.

É importante destacar que as sugestões da IA não foram consideradas automaticamente corretas. Os códigos foram executados, testados e ajustados conforme os resultados obtidos.

Durante o processo, houve participação ativa na escrita e adaptação dos códigos, na execução dos testes, na identificação de problemas e na compreensão das soluções apresentadas.

## 4. Aprendizados e dificuldades

O desenvolvimento do projeto proporcionou contato prático com conceitos que inicialmente pareciam abstratos.

Uma das principais dificuldades foi compreender como transformar um texto em uma estrutura de dados capaz de realizar buscas eficientes.

Com a implementação gradual, tornou-se mais claro como os dicionários permitem associar palavras aos seus conjuntos de ocorrências e como as operações de união e interseção facilitam as consultas combinadas.

Outra dificuldade foi lidar com detalhes que não apareciam nos exemplos mais simples, como acentuação, pontuação e linhas vazias.

Também foi necessário aprender a utilizar ferramentas que ainda não faziam parte da rotina de desenvolvimento, especialmente Git e GitHub.

A etapa de experimentação foi importante para perceber que uma estrutura de dados pode exigir um custo inicial maior, mas oferecer vantagens quando utilizada repetidamente.

Por fim, o projeto também proporcionou uma primeira experiência de organização e publicação de um projeto de programação em um repositório público.

## 5. Considerações finais

O mini-projeto foi desenvolvido de forma progressiva, começando pelo estudo dos conceitos fundamentais e avançando para a implementação, testes, experimentos, documentação e publicação.

Além de cumprir o objetivo de construir um índice invertido utilizando hashing, o desenvolvimento permitiu praticar Python, trabalhar com estruturas de dados, analisar desempenho e utilizar ferramentas de versionamento.

A utilização da inteligência artificial contribuiu para tornar o processo de aprendizagem mais orientado, permitindo esclarecer dúvidas e compreender erros ao longo do desenvolvimento.

O resultado final foi um projeto funcional, testado e publicado no GitHub, representando uma experiência importante de aprendizagem prática na disciplina de Estrutura de Dados.