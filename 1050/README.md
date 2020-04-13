# Problema:

Leia um número inteiro que representa um código de DDD para discagem interurbana. Em seguida, informe à qual cidade o DDD pertence, considerando a tabela abaixo:

	61 - Brasilia
	71 - Salvador
	11 - Sao Paulo
	21 - Rio de Janeiro
	32 - Juiz de Fora
	19 - Campinas
	27 - Vitoria
	31 - Belo Horizonte
	Outro - "DDD nao cadastrado"

Se a entrada for qualquer outro DDD que não esteja presente na tabela acima, o programa deverá informar:
DDD nao cadastrado

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/1050

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


