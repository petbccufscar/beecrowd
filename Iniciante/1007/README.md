# Problema: 1007

Leia quatro valores inteiros A, B, C e D. A seguir, calcule e mostre a diferença do produto de A e B pelo produto de C e D segundo a fórmula: DIFERENCA = (A * B - C * D).

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/1007

# Resolução:

Para ler os 4 valores inteiros antes precisamos declará-los como variáveis, para isso fazemos:
```c
        int A, B, C, D, X;
```

No nosso caso, em "X" será armazenado o resultado que ao final será exibido na tela.

Para leitura, usamos a função `scanf`:
```c
        scanf("%d %d %d %d",&A, &B, &C, &D);
```
Dessa forma realizamos a leitura de todos os valores. 

Agora fazemos uma atribuição a variável "X" realizando a diferença entre os produtos de AB e CD.
```c
        X = (A * B - C * D);
```
E por fim, escrevemos o resultado na tela utilizando a função `printf`:
```c
        printf("DIFERENCA = %d\n",X);
```
%d será substituido pelo valor contido em X.

###### Todas as funções utlizadas estão contidas na biblioteca stdio.h, incluída na primeira linha do nosso programa.


Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para petbcc.ufscar@gmail.com

