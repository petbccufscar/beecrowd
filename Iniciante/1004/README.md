# Problema

Leia dois valores inteiros. A seguir, calcule o produto entre estes dois valores e atribua esta operação à variável PROD. A seguir mostre a variável PROD com mensagem correspondente.

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/1004

# Resolução

Primeiro, deve-se declarar as variáveis inteiras a serem utilizadas. O exercício não estipulou nomes específicos para variáveis de entrada, permitindo nomenclaturas de nossa preferência. Neste caso, usaremos "A" e "B". Porém, determinou que a variável contendo a saída (resultado final) deve ser "PROD"

```c
				int A, B, PROD;
```

Para leitura da entrada, utiliza-se a função `scanf()`. Visto que serão inseridas duas entradas, armazenadas em variáveis diferentes, a função ocorrerá duas vezes, uma logo abaixo da outra.

```c
				scanf("%d", &A);
				scanf("%d", &B);
```

Após a leitura, os respectivos valores encontram-se nas variáveis A e B. Então, deve-se calcular o valor a ser guardado na variável de saída PROD, equivalente a multiplicação de A e B:

```c
				PROD = A * B;
```

Para imprimir uma saída, exibindo-a na tela, é utilizada a função `printf()`. Então, por fim, o resultado inserido na variável PROD deve ser impresso através da seguinte estrutura:

```c
				printf("PROD = %d\n",PROD);
```

##### Para aprender um pouco mais sobre variáveis: [Variáveis](http://linguagemc.com.br/variaveis-em-linguagem-c/)
##### Para aprender um pouco mais sobre leitura de dados e a estrutura scanf: [Scanf](http://linguagemc.com.br/operacoes-de-entrada-e-saida-de-dados-em-linguagem-c/)
##### Para aprender um pouco mais sobre escrita de dados e a estrutura printf: [Printf](http://linguagemc.com.br/operacoes-de-entrada-e-saida-de-dados-em-linguagem-c/)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou envie um e-mail com o assunto "URI" para petbcc.ufscar@gmail.com
