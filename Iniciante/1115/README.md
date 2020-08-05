# Problema:

Escreva um programa para ler as coordenadas (X,Y) de uma quantidade indeterminada de pontos no sistema cartesiano. Para cada ponto escrever o quadrante a que ele pertence. O algoritmo será encerrado quando pelo menos uma de duas coordenadas for NULA (nesta situação sem escrever mensagem alguma).

##### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/1115

# Resolução:

O objetivo desse exercício é ler duas coordenadas e escrever de qual quadrante esse ponto é no [plano cartesiano](https://brasilescola.uol.com.br/o-que-e/matematica/o-que-e-plano-cartesiano.htm).

Primeiro criamos duas variáveis do tipo `int`:
```c
    int X, Y;
```
`X` e `Y` representam as coordenadas de um ponto. Esses valores podem ser positivos ou negativos.

O enunciado pede para ler `X` e `Y` até que um dos pontos seja igual a 0. Aqui vamos usar o `do.. while`:
```c
    do {
      scanf("%d%d", &X, &Y);
```
Podemos ler mais de um valor dentro de um `scanf` usando mais de um `%d`. Depois de ler os dados, verificamos se os valores são positivos ou negativos. Separamos as verificações em dois casos:
```c
      if (X > 0) {
        if (Y > 0)
          printf("primeiro\n");
        else if (Y < 0)
          printf("quarto\n");
      }
```
Se `X` for positivo (`X > 0`), verificamos `Y`. Se `Y` for positivo (`Y > 0`), o ponto pertence ao primeiro quadrante e mostramos na tela a mensagem `primeiro`, Se `Y` for negativo (`Y < 0`), o ponto pertence ao quarto quadrante e mostramos na tela a mensagem `quarto`.
```c
      else if (X < 0) {
        if (Y > 0)
          printf("segundo\n");
        else if (Y < 0)
          printf("terceiro\n");
      }
    } while (X != 0 && Y != 0);
```
O segundo caso é se `X` for negativo (`X < 0`), então novamente verificamos `Y`. Se `Y` for positivo (`Y > 0`), o ponto pertence ao segundo quadrante e mostramos na tela a mensagem `segundo`, Se `Y` for negativo (`Y < 0`), o ponto pertence ao terceiro quadrante e mostramos na tela a mensagem `terceiro`.

O programa se repete caso `X` e `Y` sejam diferentes de 0 (`X != 0 && Y != 0`). Senão, o programa encerra.

##### Para aprender um pouco mais sobre a estrutura do... while: [Do... while](http://linguagemc.com.br/comando-do-while/)
##### Para aprender um pouco mais sobre if e else: [Estruturas de decisão](http://linguagemc.com.br/estrutura-de-decisao-if-em-linguagem-c/)
##### Para aprender um pouco mais sobre operadores lógicos: [Operadores lógicos](http://linguagemc.com.br/operadores-logicos-em-c/)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
