# Problema:

Leia 2 valores com uma casa decimal (x e y), que devem representar as coordenadas de um ponto em um plano. A seguir, determine qual o quadrante ao qual pertence o ponto, ou se está sobre um dos eixos cartesianos ou na origem (x = y = 0).

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/1041

# Resolução:

Primeiro, precisamos declarar as variáveis para representar as coordenadas x e y. Como esses valores tem casa decimal, utilizamos o `double`:

    double x, y;

Para leitura das coordenadas, utilizamos a função `scanf`. Usamos `%lf` para ler valores do tipo `double`. 

    scanf("%lf %lf", &x, &y);

Agora precisamos verificar se o ponto está em algum quadrante, eixo ou origem.
Vamos considerar os casos e, para representá-los no nosso programa, utilizaremos `if` e `else if` para cada caso e apresentaremos uma mensagem na tela de onde pertence com `printf`: 

### Caso 1: Origem 
#### Requisito: Ambos x e y sejam 0.

    if(x == 0 && y == 0)
        printf("Origem\n");

### Caso 2: Quadrante 1
#### Requisito: x > 0 e y > 0

    else if(x > 0 && y > 0)
        printf("Q1\n");

### Caso 3: Quadrante 4
#### Requisito: x > 0 e y < 0

    else if(x > 0 && y < 0)
        printf("Q4\n");

### Caso 4: Quadrante 2
#### Requisito: x < 0 e y > 0

    else if(x < 0 && y > 0)
        printf("Q2\n");

### Caso 5: Quadrante 3
#### Requisito: x < 0 e y < 0

    else if(x < 0 && y < 0)
        printf("Q3\n");

### Caso 6: Eixo Y
#### Requisito: x = 0

    else if(x == 0)
        printf("Eixo Y\n");

### Caso 7: Eixo X
#### Requisito: y = 0

    else if(y == 0)
        printf("Eixo X\n");


###### Todas as funções utlizadas estão contidas na biblioteca stdio.h, incluída na primeira linha do nosso programa.

##### Para aprender um pouco mais sobre variáveis: [Variáveis](http://linguagemc.com.br/variaveis-em-linguagem-c/)
##### Para relembrar os quadrantes do plano cartesiano: [Quadrantes](https://www.estudopratico.com.br/plano-cartesiano/) 

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
* [Facebook](https://www.facebook.com/petbcc/),
* [Instagram](https://www.instagram.com/petbcc.ufscar/)
* ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com