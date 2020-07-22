# Problema

Leia um valor inteiro N. Apresente todos os números entre 1 e 10000 que divididos por N dão resto igual a 2.

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/1075

# Resolução

Para resolver o problema, vamos receber o valor N e, ao testar dividindo todos os números de 1 a 10000 por N, verificaremos se o resto da divisão é 2.

Começamos declarando as variáveis que serão utilizadas no exercício.
Para declarar, usaremos o tipo inteiro:

	int cont, N;

Para a leitura do valor que nossa variável N terá, usaremos a estrutura scanf:

    scanf("%d", &N);

Para dividir todos os números de 1 a 10000 por N, usaremos a estrutura de repetição for.
A variável cont será nosso contador da estrutura, que também fará as divisões. 
Primeiro, ela começa com o valor = 1. Os valores que ela poderá obter são menores ou igual a 10000. Para que mude de valor, cont será incrementada toda vez que uma repetição ocorrer, que fazemos com cont++, que funciona de forma similar a cont = cont + 1. Cada uma dessas condições é representada dentro da estrutura for.

	for(cont=1; cont<=10000; cont++)

Para verificar se o resto da divisão é 2, utilizaremos o operador %. Este operador faz a divisão do contador com o número N, e verifica o resto da divisão.
Utilizando a estrutura if, verificamos se o resto da divisão de cont por N é igual a 2.

	if(cont%N == 2)

Caso seja, imprimimos esse número, pois é um valor dos pedidos pelo exercício.

	printf("%d\n", cont);

Essa repetição termina, cont é incrementado e o for executa esses passos novamente, até que cont chegue em 1000, e termina a execução.


##### Mais sobre a estrutura de repetição for: http://linguagemc.com.br/a-estrutura-de-repeticao-for-em-c/
##### Mais sobre operadores de auto incremento e auto decremento: http://linguagemc.com.br/operadores-de-auto-incremento-e-auto-decremento/
##### Mais sobre % e outros operadores aritméticos: http://linguagemc.com.br/operadores-aritmeticos-em-linguagem-c/


Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
* [Facebook](https://www.facebook.com/petbcc/),
* [Instagram](https://www.instagram.com/petbcc.ufscar/)
* ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
