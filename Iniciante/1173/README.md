# Problema

Leia um valor e faça um programa que coloque o valor lido na primeira posição de um vetor N[10]. Em cada posição subsequente, coloque o dobro do valor da posição anterior. Por exemplo, se o valor lido for 1, os valores do vetor devem ser 1,2,4,8 e assim sucessivamente. Mostre o vetor em seguida.

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/1173

# Solução

Para resolver o problema, vamos ler o valor, alocá-lo e multiplicá-lo por 2 subsequentemente em cada posição do vetor.

Começamos declarando nossas variáveis a serem utilizadas no problema. Todas serão do tipo `int`, por seremos números inteiros.
Serão `n[10]` o vetor de 10 posições pedido pelo exercício, `i` o contador de loops da estrutura de repetição e `v` o valor a ser colocado em cada posição do vetor.

    int n[10], i, v;

Em seguida, iremos ler o valor da primeira posição e alocá-lo na variável `v` com a estrutura `scanf`.

    scanf("%d", &v);

A seguir, faremos a estrutura de repetição `for`.
A variável `i` será nosso contador da estrutura, para contabilizar quantas vezes a repetição ocorre. 
Primeiro, ela começa com o valor = 0. Os valores que ela poderá obter são menores ou iguais a 9, visto que o vetor tem 10 posições e inicia-se em 0. Para que mude de valor, `i` será incrementada toda vez que uma repetição ocorrer, que faremos com `i++` (que funciona de forma similar a `i = i + 1`. Cada uma dessas condições é representada dentro da estrutura `for`.

	for (i = 0; i <= 9; i++)

Alocamos o valor da variável `v` na posição em que `i` representa por seu valor no vetor `n`.

	n[i] = v;

Exibimos o valor da posição `i` na tela conforme o exercício pede, utilizando a estrutura `printf`. Lembre-se de utilizar o `\n` no final, pois o URI costuma ser bem exigente com a saída da resolução do problema.

        printf("N[%d] = %d\n",i,v);

A seguir, multiplicamos o valor atual de `v` para que seja o dobro. Assim, na próxima iteração do `for`, este valor será o dobro do anterior e será salvo na próxima posição do vetor `n`.

        v=v*2;

Essa repetição termina, `i` é incrementado e o `for` executa esses passos novamente, até que `i` chegue em 9, e termina a execução.


##### Mais sobre vetores: [vetor](http://linguagemc.com.br/vetores-ou-arrays-em-linguagem-c/)
##### Mais sobre a estrutura de repetição for: [for](http://linguagemc.com.br/a-estrutura-de-repeticao-for-em-c/)
##### Mais sobre operadores de auto incremento e auto decremento: [Auto Incremento](http://linguagemc.com.br/operadores-de-auto-incremento-e-auto-decremento/)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
* [Facebook](https://www.facebook.com/petbcc/),
* [Instagram](https://www.instagram.com/petbcc.ufscar/)
* ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com