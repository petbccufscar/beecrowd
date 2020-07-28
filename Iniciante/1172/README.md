# Problema

Faça um programa que leia um vetor X[10]. Substitua a seguir, todos os valores nulos e negativos do vetor X por 1. Em seguida mostre o vetor X.

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/1172

# Solução

Para resolver o problema, vamos primeiro ler todos os valores, compará-los e listá-los conforme o modelo do exercício.

Começamos declarando nossas variáveis no tipo `int`, por serem números inteiros.
Nossas variáveis serão o vetor de dez posições `X[10]`, conforme pedido pelo exercício, e o contador de loops do nosso laço de repetição `i`.

	int X[10], i;

A seguir, faremos a primeira estrutura de repetição `for`.
A variável `i` será nosso contador da estrutura, para contabilizar quantas vezes a repetição ocorre. 
Primeiro, ela começa com o valor = 0. Os valores que ela poderá obter são menores a 10, visto que o vetor tem 10 posições e inicia-se em 0. Para que mude de valor, `i` será incrementada toda vez que uma repetição ocorrer, que faremos com `i++` (que funciona de forma similar a `i = i + 1`. Cada uma dessas condições é representada dentro da estrutura `for`.

	for (i = 0; i < 10; i++)

Lemos cada um dos valores com a estrutura `scanf` e salvamos este valor no vetor `x` na posição em que o contador `i` estiver.

	scanf("%d", &X[i]);

Essa repetição termina, `i` é incrementado e o `for` executa esses passos novamente, até que `i` chegue em 10, e termina a execução.

Terminando a repetição, faremos nossa segunda estrutura de repetição `for`. Terá as mesmas condições da primeira, assim como os mesmos valores iniciais e limite e a mesma variável `i`.

	for (i=0 ; i<10; i++)

Aqui faremos a verificação de números nulos ou negativos com a estrutura `if`. Caso o valor da posição `i` do vetor `x` seja 0 ou negativo, substituímos este valor com 1.

	if (X[i]<=0)
	    X[i] = 1;

Em seguida, exibimos esse valor na tela conforme o exercício pede, utilizando a estrutura `printf`. Lembre-se de utilizar o `\n` no final, pois o URI costuma ser bem exigente com a saída da resolução do problema.

        printf("X[%d] = %d\n", i, X[i]);

Essa repetição termina, `i` é incrementado e o `for` executa esses passos novamente, até que `i` chegue em 10, e termina a execução.

##### Mais sobre vetores: [vetor](http://linguagemc.com.br/vetores-ou-arrays-em-linguagem-c/)
##### Mais sobre a estrutura de repetição for: [for](http://linguagemc.com.br/a-estrutura-de-repeticao-for-em-c/)
##### Mais sobre operadores de auto incremento e auto decremento: [Auto Incremento](http://linguagemc.com.br/operadores-de-auto-incremento-e-auto-decremento/)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
* [Facebook](https://www.facebook.com/petbcc/),
* [Instagram](https://www.instagram.com/petbcc.ufscar/)
* ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com