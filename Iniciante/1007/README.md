# Problema: 1007  
Leia quatro valores inteiros A, B, C e D. A seguir, calcule e mostre a diferença do produto de A e B pelo produto de C e D segundo a fórmula: DIFERENCA = (A * B - C * D).

##### Link do problema: https://www.urionlinejudge.com.br/judge/pt/problems/view/1007


# Resolução:
O exercício pede para que seja feita a leitura de 4 valores inteiros, calculado o valor através da formula passada, e apresentado na tela.

Iniciaremos o código com a utilização da biblioteca `stdio.h` que será util para a utilização de algumas funções como exemplo as de leitura e escrita, sendo elas `scanf` e `printf`, respectivamente, para isso faremos:
```c
#include <stdio.h>
```

Com a biblioteca inserida podemos realizar a leitura dos 4 valores inteiros, mas antes é preciso declarar algumas variaveis, "A, B, C e D" onde serão armazenados os valores informados e uma variavel adicional "X" para armazenar o resultado final, o qual será apresentado na tela, para isso:
```c
int A, B, C, D, X;
```

Em seguida realizaremos a leitura dos valores que serão passados, utilizando a função `scanf` e colocando os termos em sequencia é possivel realizar a leitura de todos os valores:
```c
scanf("%d %d %d %d",&A, &B, &C, &D);
``` 

Após isso faremos uma atribuição a variável "X" com o valor resultante da diferença entre os produtos de AB e CD.
```c
X = (A * B - C * D);
```

E por fim, escrevemos o resultado na tela utilizando a função `printf`:
```c
printf("DIFERENCA = %d\n",X);
```


##### Para mais informações sobre [variáveis](http://linguagemc.com.br/variaveis-em-linguagem-c/)
    
“Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC (facebook, twitter, etc)”