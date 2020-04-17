# Problema:

Leia 2 valores com uma casa decimal (x e y), que devem representar as coordenadas de um ponto em um plano. A seguir, determine qual o quadrante ao qual pertence o ponto, ou se está sobre um dos eixos cartesianos ou na origem (x = y = 0).

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/1041

# Resolução:

Primeiro, precisamos declarar as variáveis para representar as coordenadas x e y:
```c
        double x, y;
```

Como esses valores tem casa decimal, utilizamos o double.

##### Para aprender um pouco mais sobre variáveis: [Variáveis](http://linguagemc.com.br/variaveis-em-linguagem-c/)

Para leitura das coordenadas, utilizamos a função scanf:
```c
        scanf("%lf %lf", &x, &y);
```
%lf é usado para ler valores do tipo double. 

Agora precisamos verificar se o ponto está em algum quadrante, eixo ou origem.

Vamos considerar os casos: 

### Caso 1: Origem 
#### Requisito: Ambos x e y sejam 0.

### Caso 2: Quadrante 1
#### Requisito: x > 0 e y > 0

### Caso 3: Quadrante 4
#### Requisito: x > 0 e y < 0

### Caso 4: Quadrante 2
#### Requisito: x < 0 e y > 0

### Caso 5: Quadrante 3
#### Requisito: x < 0 e y < 0

### Caso 6: Eixo Y
#### Requisito: x = 0

### Caso 7: Eixo X
#### Requisito: y = 0

Para representar estes casos no nosso programa, utilizaremos if e else if: 
```c
        if(x == 0 && y == 0)
            printf("Origem\n");
        else if(x > 0 && y > 0)
            printf("Q1\n");
        else if(x > 0 && y < 0)
            printf("Q4\n");
        else if(x < 0 && y > 0)
            printf("Q2\n");
        else if(x < 0 && y < 0)
            printf("Q3\n");
        else if(x == 0)
            printf("Eixo Y\n");
        else if(y == 0)
            printf("Eixo X\n");
```
##### Para relembrar os quadrantes do plano cartesiano: [Quadrantes](https://www.estudopratico.com.br/plano-cartesiano/) 


###### Todas as funções utlizadas estão contidas na biblioteca stdio.h, incluída na primeira linha do nosso programa.
