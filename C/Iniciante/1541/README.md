# Problema

A entrada é composta de vários casos de testes. Cada caso de teste é composto de três números inteiros A, B e C ( > 0 e ≤ 1000) separados por um espaço. Estes números representam as medidas da casa (A e B) e o percentual máximo liberado para construir nesse bairro (C). Um único valor igual a 0 indica o fim das entradas. Você deverá informar um número inteiro, o qual representa a medida do lado do terreno. Este valor deverá ser truncado caso necessário.

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/1541

# Resolução

Antes de iniciar o código, é preciso entender o que o enunciado do problema pede, visto que não está escrito de forma intuitiva. De forma resumida, o problema conta uma história sobre uma cidade onde só é permitido construir uma casa em uma porcentagem específica de terreno. O que temos de entrada são os lados da casa (formando a área da casa) e o percentual que é permitido. O desafio é descobrir qual deveria ser o tamanho mínimo do lado do terreno quadrado, aproximadamente, para que conseguisse construir toda a casa respeitando o percentual.

Para poder calcular o lado, iremos fazer a raiz quadrada da área da casa. Para conseguir realizar esta operação, utilizaremos a biblioteca `math.h`, que deve ser incluída no começo do código.

O primeiro passo é declarar as variáveis que serão utilizadas no exercício. Como todos os valores são inteiros, vamos utilizar o tipo `int`.
```c
    int a,b,c,d,e;
```

Um dos grandes desafios deste problema é não exceder o tempo limite. Desta forma, usaremos uma forma não convencional da estrutura `while`, para que consigamos concluir o exercício sem exceder o tempo.
Desta forma, colocaremos nossa estrutura `while` com um loop infinito (isto é, com um valor 1 que, em booleano, simboliza `TRUE` - verdadeiro). Visto que sabemos o critério de parada (a inseção de um `A == 0`), iremos quebrar o loop quando este valor for lido pela estrutura `scanf`.
```c
while(1)
{
	scanf("%d", &a);
    
    if(a==0) 
            break;
``` 

Caso o valor lido pelo `scanf` não seja 0, podemos considerar a entrada como válida para realizar as operações. Assim, faremos a leitura das variáveis `B` e `C`.
```c
    else
    {
    	scanf("%d%d", &b,&c);
```

Tendo os valores dos lados, podemos calcular a área da casa.
```c
	    area = a*b;
```

Tendo a área, podemos calcular o lado do terreno, que é a raiz quadrada do valor da área levando em consideração a porcentagem permitida. A raiz quadrada será calculada pela função `sqrt`, presente na biblioteca `math.h`.
```c
        lado = sqrt((area*100)/c);
```

Finalmente, podemos exibir o lado do terreno com a função `printf`.
```c
        printf("%d\n", lado);
```

##### Mais sobre área e metros quadrados: [área](https://industriahoje.com.br/como-calcular-o-metro-quadrado-m%C2%B2)
##### Mais sobre a biblioteca math.h: [math.h](http://linguagemc.com.br/a-biblioteca-math-h/)
##### Mais sobre o uso de while(1) e loops infinitos: [while(1)](http://linguagemc.com.br/loop-infinito-em-c/)
##### Mais sobre o comando break: [break](http://linguagemc.com.br/o-comando-break/)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
* [Facebook](https://www.facebook.com/petbcc/),
* [Instagram](https://www.instagram.com/petbcc.ufscar/)
* ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com

