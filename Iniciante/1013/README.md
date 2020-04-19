# Problema

Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido da mensagem “eh o maior”. Utilize a fórmula:

MaiorAB = (a+b+abs(a-b)) / 2

Obs: a fórmula apenas calcula o maior entre os dois primeiros (a e b). Um segundo passo, portanto é necessário para chegar no resultado esperado.

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/1013

# Resolução

Primeiro, deve-se declarar as variáveis a serem utilizadas. Neste exercício, todas as variáveis serão inteiras. declararemos uma variável maior para guardar o maior de dois números. 

###### Modelo: TipoDaVariavel NomeDaVariavel;

	int a,b,c,maior;

##### Mais sobre variáveis neste link (http://linguagemc.com.br/variaveis-em-linguagem-c/)

## Entrada

Para leitura da entrada, utiliza-se a função scanf(), que lerá os 3 valores juntos, podendo ser diferenciados por um espaço ou a tecla enter (quebra de linha)

###### Modelo: scanf("%TipoDaVariavel", &NomeDaVariavel);

	scanf("%d %d %d", &a,&b,&c);

##### Mais sobre leitura de dados e a estrutura scanf neste link (http://linguagemc.com.br/operacoes-de-entrada-e-saida-de-dados-em-linguagem-c/)

Para resolver esse problema de comparação, devemos utilizar a formula que o exercício nos passou e assim comparar dois números **a** e **b**. Obtendo o maior deles e salvando na variável **maior** e depois disso aplicamos a mesma fórmula em **maior** e **c** e guardamos novamente na variável maior, reutilizando a variável maior.

Lembre-se que a função abs utilizada na fórmula dada pelo exercício, pertence a biblioteca stdlib, importada na segunda linha do nosso código.

## Saída

Para imprimir uma saída, exibindo-a na tela, é utilizada a função printf().
###### Modelo: printf("Texto a ser exibido e/ou %TipoDaVariavel", NomeDaVariavel);
	
	printf("%d eh o maior",maior);

##### Mais sobre escrita de dados e a estrutura printf neste link (http://linguagemc.com.br/operacoes-de-entrada-e-saida-de-dados-em-linguagem-c/)
