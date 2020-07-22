# Problema

 Leia 1 valor inteiro N, que representa o número de casos de teste que vem a seguir. Cada caso de teste consiste de 3 valores reais, cada um deles com uma casa decimal. Apresente a média ponderada para cada um destes conjuntos de 3 valores, sendo que o primeiro valor tem peso 2, o segundo valor tem peso 3 e o terceiro valor tem peso 5.

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/1079

# Resolução

Para resolver o problema, 

Começamos declarando as variáveis que serão utilizadas no exercício.
Para declarar, usaremos o tipo float (número flutuante), pois o problema pede que sejam valores reais:

	float nota1, nota2, nota3, total, media;

Para declarar o número de casos e o contador da estrutura de repetição que utilizaremos a seguir, usaremos o tipo inteiro

	int cont, casos;

Para ler o número de casos de teste, utilizamos a estrutura scanf

	scanf("%d", &casos);

Para ler cada um dos casos e calcular as médias, utilizaremos a estrutura de repetição for.
A variável cont será nosso contador da estrutura, para contabilizar cada caso. 
Primeiro, ela começa com o valor = 1. Os valores que ela poderá obter são menores ou igual ao valor de casos. Para que mude de valor, cont será incrementada toda vez que uma repetição ocorrer, que fazemos com cont++ (que funciona de forma similar a cont = cont + 1). Cada uma dessas condições é representada dentro da estrutura for.

	for(cont=1; cont<=casos; cont++)

Lemos cada uma das notas com a estrutura scanf, desta vez com "%f" que representa uma variável float.

	scanf("%f%f%f", &nota1, &nota2, &nota3);

Calculamos qual será o valor da primeira soma com cada nota lida e seus respectivos pesos e salvamos na variavel 'total'

	total = nota1*2.0 + nota2*3.0 + nota3*5.0;

Por fim, dividimos a soma em 'total' por 10.0 para obter a média ponderada final

	media = total/10.0;

Exibimos a média ponderada final com a estrutura printf

	printf("%.1f\n", media);

Essa repetição termina, cont é incrementado e o for executa esses passos novamente, até que cont chegue em 1000, e termina a execução.

##### Mais sobre a média ponderada: https://brasilescola.uol.com.br/matematica/media-ponderada.htm
##### Mais sobre a estrutura de repetição for: http://linguagemc.com.br/a-estrutura-de-repeticao-for-em-c/
##### Mais sobre operadores de auto incremento e auto decremento: http://linguagemc.com.br/operadores-de-auto-incremento-e-auto-decremento/


Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
* [Facebook](https://www.facebook.com/petbcc/),
* [Instagram](https://www.instagram.com/petbcc.ufscar/)
* ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com