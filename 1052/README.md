# Problema:

Leia um valor inteiro entre 1 e 12, inclusive. Correspondente a este valor, deve ser apresentado como resposta o mês do ano por extenso, em inglês, com a primeira letra maiúscula.
Obs: Meses em Inglês.

Exemplo: 
	Entrada: 4 
	Saida: April

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/1052

# Resolução:

Para ler os 4 valores inteiros antes precisamos declará-los como variáveis, para isso fazemos:
```c
        int A, B, C, D, X;
```

No nosso caso, em "X" será armazenado o resultado que ao final será exibido na tela.

Para leitura, usamos a função scanf:
```c
        scanf("%d %d %d %d",&A, &B, &C, &D);
```
Dessa forma realizamos a leitura de todos os valores. 

Agora fazemos uma atribuição a variável "X" realizando a diferença entre os produtos de AB e CD.
```c
        X = (A * B - C * D);
```
E por fim, escrevemos o resultado na tela utilizando a função printf:
```c
        printf("DIFERENCA = %d\n",X);
```
%d será substituido pelo valor contido em X.

###### Todas as funções utlizadas estão contidas na biblioteca stdio.h, incluída na primeira linha do nosso programa.


