# Problema:
    
Leia um valor inteiro N. Este valor será a quantidade de valores que serão lidos em seguida. Para cada valor lido(*X*), mostre uma mensagem em inglês dizendo se este valor lido é par (EVEN), ímpar (ODD), positivo (POSITIVE) ou negativo (NEGATIVE). No caso do valor ser igual a zero (0), embora a descrição correta seja (EVEN NULL), pois por definição zero é par, seu programa deverá imprimir apenas NULL.
 
##### Link do problema: https://www.urionlinejudge.com.br/judge/pt/problems/view/1074
 
# Resolução:
 
Inicialmente instanciamos as variáveis necessárias, três inteiros, sendo eles `N`(quantidade de valores lidos), `X`(valor a ser lido) e `cont`(contador do `for()`).
 
```c
    int N, X, cont;
```
 
Lemos o valor de `N`.
 
```c
 
    scanf ("%d", &N);
```
 
Agora nos iremos utilizar o `for()` para analizar numero por numero. No começo do `for()` vamos ler `X`, depois iremos fazer uma série de comparações para identificar a qual grupo esse `X` esta. Após identificarmos imprimimos na tela sua classificação (par ou ímpar; positivo, negativo ou nulo) com base no que foi pedido.
 
```c
    for (cont = 1; cont <= N; cont++)
    {
        scanf("%d", &X);
        if (X == 0)
            printf("NULL\n");
        else if (X <= 0 && X % 2 == 0)
            printf("EVEN NEGATIVE\n");
        else if (X <= 0 && X % 2 == -1)
            printf("ODD NEGATIVE\n");
        else if (X >= 0 && X % 2 == 0)
            printf("EVEN POSITIVE\n");
        else if (X >= 0 && X % 2 == 1)
            printf("ODD POSITIVE\n");
    }
```
 
##### Para aprender um pouco mais sobre o laço de repetição for: [For](http://linguagemc.com.br/a-estrutura-de-repeticao-for-em-c/)
 
Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
 

