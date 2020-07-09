Guia do README

# Problema:    
Cópia da parte lógica do problema do site do URI, que descreve o problema em língua natural.

Caso a entrada/saída seja vital na explicação do problema, pode-se citá-la como “conforme a entrada/saída exemplificada no exercício [exemplo da entrada/saída] (...)”. Caso contrário, deve ser omitida.

**Problema Completo**: link_do_problema


# Resolução:
A resolução deve começar com uma explicação resumida do enunciado do problema, caso a interpretação não seja objetiva, e da lógica de resolução. Exemplo: “O exercício pede para calcular se 3 retas formariam um triângulo, para resolvê-lo, deve-se criar ler os valores e calcular com a fórmula (...)”

Definir e explicar o uso de bibliotecas não triviais do C, como `<math.h>` e semelhantes.

Declaração de variáveis: preferencialmente com as variáveis que serão utilizadas na resolução do problema, com nomes intuitivos. 
Exemplo: “Utilizamos uma variável inteira para a soma, uma variável de ponto flutuante para o valor (...)
```c
int soma;
float valor;
```

Lógica do problema com trechos do código. Buscar explicar todos os trechos do código completo com passo a passo, incluindo a saída do problema formatada para o URI.

Para conceitos-chave da lógica do problema, inserir um link de explicação no texto, dando preferência para explicações em português.
Exemplo: “(...) calcularemos a [área do triângulo](link)”

Para conceitos base e anteriores ao problema, deixar links de explicação no final da resolução. Evitar conceitos que já sejam presumíveis para o nível do exercício, como declaração de variáveis em exercícios de nível médio/avançado.
Exemplo: ##### Para revisar sobre [variáveis de ponto flutuante](link)
    
“Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC (facebook, twitter, etc)”

**Guia do código**

 - Sem comentários, todo o código deve ser explicado no README

 - Atentar-se com o fluxo de leitura do código, respeitando a indentação

 - Busque deixar seu código o mais modularizado possível, para facilitar o entendimento no README.
 Exemplo: definir uma função para ordenação de listas (caso necessária) fora da função main.

 - **TESTA NO URI ANTES DE ENVIAR PELO AMOR DE ALAN TURING**
