# Problema

Escreva um programa que leia três valores com ponto flutuante de dupla precisão: A, B e C. Em seguida, calcule e mostre:

a) a área do triângulo retângulo que tem A por base e C por altura.

b) a área do círculo de raio C. (pi = 3.14159)

c) a área do trapézio que tem A e B por bases e C por altura.

d) a área do quadrado que tem lado B.

e) a área do retângulo que tem lados A e B. 

**Problema completo**: https://www.urionlinejudge.com.br/judge/pt/problems/view/1012

# Resolução

Neste problema, iremos declarar todas variáveis necessárias, calcular todas as áreas e, por último, exibi-las na tela.

Primeiro, deve-se declarar as variáveis a serem utilizadas. Neste problema, todas as variáveis serão de ponto flutuante de dupla precisão, ou seja `double`. 

```c
	double a, b, c, pi;
	double triangulo,circulo,trapezio,quadrado,retangulo;
```

Definimos as variáveis da segunda linha para armazenar o resultado das áreas que calcularmos para cada forma geométrica, como informado no enunciado.

No enunciado do problema, temos que `pi` já é definido com um valor fixo (3.14159). Podemos, então, já atribuir esse valor a nossa variável `pi`

```c
	pi = 3.14159;
```

Para leitura da entrada, utiliza-se a função `scanf()`, que lerá os 3 valores juntos, podendo ser diferenciados por um espaço ou a tecla enter (quebra de linha) durante a inserção.

```c
	scanf("%lf %lf %lf",&a,&b,&c);
```

Após a leitura, os respectivos valores encontram-se nas variáveis `a`, `b`, `c` e serão utilizados para os cálculos de área pedidos no problema.
    
```c
 	triangulo = (a*c)/2;
    circulo = pi*c*c;
    trapezio = ((a + b)*c)/2;
    quadrado = b*b;
    retangulo = a*b;
```

Para imprimir as saídas, é utilizada a função `printf()`. Utilizamos `%.3lf` ao invés de apenas `%lf`(que representa um valor `double`) para delimitarmos o número de casas exibidas após a virgula (precisão), como mostrado no exemplo de saída do problema.

```c	
	printf("TRIANGULO: %.3f\n", triangulo);
    printf("CIRCULO: %.3f\n", circulo);
    printf("TRAPEZIO: %.3f\n", trapezio);
    printf("QUADRADO: %.3f\n", quadrado);
    printf("RETANGULO: %.3f\n", retangulo);
```


##### Para aprender um pouco mais sobre variáveis: [Variáveis](http://linguagemc.com.br/variaveis-em-linguagem-c/)

##### Para entender sobre entradas e saídas: [Entrada e Saida](http://linguagemc.com.br/operacoes-de-entrada-e-saida-de-dados-em-linguagem-c/)