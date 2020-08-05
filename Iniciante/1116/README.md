# Problema:

Escreva um algoritmo que leia 2 números e imprima o resultado da divisão do primeiro pelo segundo. Caso não for possível mostre a mensagem “divisao impossivel” para os valores em questão.

##### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/1116

# Resolução:

O objetivo desse exercício é ler dois valores N vezes, efetuar a divisão caso seja possível e mostrar o resultado na tela.

Para começar criamos quatro variáveis do tipo `int`:
```c
    int x, y, N, i;
```
`x` e `y` representam os valores do dividendo e divisor, respectivamente. `N` representa o número de cálculos que serão feitos, `i` é uma variável auxiliar que será usada no `for`.

Temos que saber quantos casos serão feitos, para isso lemos `N` usando `scanf`:
```c
    scanf("%d", &N);
```
Com a variável lida, fazemos um laço de repetição usando `for`. Igualamos `i` a 0 (`i=0`) e incrementamos o valor dessa variável (`i++`) a cada repetição até que `i` seja igual a N-1 (`i<N`), que é o menor valor inteiro antes de `N`:
```c
    for(i=0;i<N;i++) {
      scanf("%d%d", &x, &y);
```
Dentro do laço temos que ler `x` e `y` para poder fazer a divisão. Podemos escrever mais de um valor dentro de um `scanf` usando vários `%d`. Em seguida temos que verificar se a divisão é possivel:
```c
      if (y == 0)        
        printf("divisao impossivel\n");
```
A divisão será impossível se `y` for igual a 0 (`y == 0`), pois não existe divisão por zero. Caso aconteça, escrevemos na tela a mensagem `divisao impossivel` com o comando `printf`. Senão fazemos a divisão e mostramos o resultado na tela:
```c
      else
        printf("%0.1lf\n", (double)x/y);
    }
```
Aqui nós não mencionamos uma variável para ser escrita no `printf`, mas sim uma operação (`x/y`). Além disso precisamos inserir o `(double)` antes da divisão para mudar o tipo de variável de `int` para `double`, isso é mencionado no enunciado do exercício como "cast" e, ao mudar o tipo, devemos trocar `%d` por `%lf` para mostrar o valor na tela. O `0.1` indica quantas casas decimais serão apresentadas, que no caso é uma. 

##### Para aprender um pouco mais sobre a estrutura for: [For](http://linguagemc.com.br/a-estrutura-de-repeticao-for-em-c/)
##### Para aprender um pouco mais sobre if e else: [Estruturas de decisão](http://linguagemc.com.br/estrutura-de-decisao-if-em-linguagem-c/)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
