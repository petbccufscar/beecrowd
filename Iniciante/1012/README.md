# Problema

Escreva um programa que leia três valores com ponto flutuante de dupla precisão: A, B e C. Em seguida, calcule e mostre:
a) a área do triângulo retângulo que tem A por base e C por altura.
b) a área do círculo de raio C. (pi = 3.14159)
c) a área do trapézio que tem A e B por bases e C por altura.
d) a área do quadrado que tem lado B.
e) a área do retângulo que tem lados A e B. 

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/1012

# Resolução

Primeiro, deve-se declarar as variáveis a serem utilizadas. Neste exercício, todas as variáveis serão de ponto flutuante de bupla precisão, ou seja "double". declararemos váriaveis auxiliares para armazenar o resultado dos cálculos das áreas. 

###### Modelo: TipoDaVariavel NomeDaVariavel;

	double a,b,c;

##### Mais sobre variáveis neste link (http://linguagemc.com.br/variaveis-em-linguagem-c/)

## Entrada

Para leitura da entrada, utiliza-se a função scanf(), que lerá os 3 valores juntos, podendo ser diferenciados por um espaço ou a tecla enter (quebra de linha)

###### Modelo: scanf("%TipoDaVariavel", &NomeDaVariavel);

	scanf("%lf %lf %lf", &a,&b,&c);

##### Mais sobre leitura de dados e a estrutura scanf neste link (http://linguagemc.com.br/operacoes-de-entrada-e-saida-de-dados-em-linguagem-c/)

Após a leitura, os respectivos valores encontram-se nas variáveis A, B, C e serão utilizados para os cálculos de área pedidos no exercício.
    
## Saída

Para imprimir uma saída, exibindo-a na tela, é utilizada a função printf(). Utilizamos %.3lf ao invés de %lf para delimitarmos o número de casas exibidas após a virgula (precisão).

###### Modelo: printf("Texto a ser exibido e/ou %TipoDaVariavel", NomeDaVariavel);
	
	printf("TRIANGULO: %.3lf\n",triangulo);

##### Mais sobre escrita de dados e a estrutura printf neste link (http://linguagemc.com.br/operacoes-de-entrada-e-saida-de-dados-em-linguagem-c/)
