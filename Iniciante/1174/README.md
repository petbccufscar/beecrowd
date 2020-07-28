# Problema

Faça um programa que leia um vetor A[100]. No final, mostre todas as posições do vetor que armazenam um valor menor ou igual a 10 e o valor armazenado em cada uma das posições.

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/1174

# Solução 

Para resolver o problema, iremos ler todos os valores, alocá-los no vetor e, ao verificar se o valor é menor ou igual a 10, exibir a posição que ele se encontra e este valor.

Começamos declarando nossas variáveis a serem utilizadas no problema. 
O vetor `a[100]` de 100 posições será do tipo `double`, visto que os valores armazenados nele serão reais.

    double A[100];

A outra variável será o contador de loops da estrutura de repetição.

    int i;

A seguir, faremos a primeira estrutura de repetição `for`.
A variável `i` será nosso contador da estrutura, para contabilizar quantas vezes a repetição ocorre. 
Primeiro, ela começa com o valor = 0. Os valores que ela poderá obter são menores que 100, visto que o vetor tem 100 posições e inicia-se em 0. Para que mude de valor, `i` será incrementada toda vez que uma repetição ocorrer, que faremos com `i++` (que funciona de forma similar a `i = i + 1`. Cada uma dessas condições é representada dentro da estrutura `for`.

    for(i=0; i<100; i++)

Em seguida, iremos ler os 100 valores e alocaremos em cada posição do vetor representada por `i` com a estrutura `scanf`.

    scanf("%lf", &A[i]);

Essa repetição termina, `i` é incrementado e o `for` executa esses passos novamente, até que `i` chegue em 100, e termina a execução.

Faremos, então, nossa segunda estrutura `for`. Terá as mesmas condições da primeira, assim como os mesmos valores iniciais e limite e a mesma variável `i`.

    for(i=0; i<100; i++)

A seguir, faremos a verificação dos valores alocados no vetor `A`, utilizando a estrutura `if`, para verificar se a posição `i` do vetor é menor ou igual a 10.0.

    if(A[i]<=10.0)

Caso seja, será exibida a posição que está e seu respectivo valor conforme o exercício pede, utilizando a estrutura `printf`. Lembre-se de utilizar o `\n` no final, pois o URI costuma ser bem exigente com a saída da resolução do problema.

    printf("A[%d] = %.1lf\n",i, A[i]);

Essa repetição termina, `i` é incrementado e o `for` executa esses passos novamente, até que `i` chegue em 9, e termina a execução.

##### Mais sobre vetores: [vetor](http://linguagemc.com.br/vetores-ou-arrays-em-linguagem-c/)
##### Mais sobre a estrutura de repetição for: [for](http://linguagemc.com.br/a-estrutura-de-repeticao-for-em-c/)
##### Mais sobre operadores de auto incremento e auto decremento: [Auto Incremento](http://linguagemc.com.br/operadores-de-auto-incremento-e-auto-decremento/)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
* [Facebook](https://www.facebook.com/petbcc/),
* [Instagram](https://www.instagram.com/petbcc.ufscar/)
* ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
