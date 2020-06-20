# Problema: 1007  
Leia quatro valores inteiros A, B, C e D. A seguir, calcule e mostre a diferença do produto de A e B pelo produto de C e D segundo a fórmula: DIFERENCA = (A * B - C * D).

##### Link do problema: https://www.urionlinejudge.com.br/judge/pt/problems/view/1007


# Resolução:
O exercício pede para que seja feita a leitura de 4 valores inteiros e em seguida seja calculado o valor utilizando a formula passada, e em seguida .

Iniciamos o código com a utilização da biblioteca `stdio.h` que será util para a utilização de funções de leitura e escrita, para isso faremos:
```c
#include <stdio.h>
```

Com a biblioteca inserida podemos utilizar algumas funções como exemplo as de leitura e escrita, sendo elas `scanf` e `printf`, respectivamente.
Para realizar a leitura dos 4 valores inteiros antes é preciso declarar algumas variaveis, onde serão armazenados os valores, para isso:
```c
int A, B, C, D, X;
```
No nosso caso, em "X" será armazenado o resultado que ao final será exibido na tela.

Em seguida realizaremos a leitura dos valores que serão passados, para isso usaremos a função `scanf`:
```c
scanf("%d %d %d %d",&A, &B, &C, &D);
```
Dessa forma realizamos a leitura de todos os valores. 

Após isso faremos uma atribuição a variável "X" com o valor resultante da diferença entre os produtos de AB e CD.
```c
X = (A * B - C * D);
```
E por fim, escrevemos o resultado na tela utilizando a função `printf`:
```c
printf("DIFERENCA = %d\n",X);
```
em `%d` será substituido pelo valor contido em X.


##### Para mais informações a respeito de [tipos de variáveis](http://linguagemc.com.br/variaveis-em-linguagem-c/)
    
“Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC (facebook, twitter, etc)”