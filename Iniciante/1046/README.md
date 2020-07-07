# Problema: 1046

Leia a hora inicial e a hora final de um jogo. A seguir calcule a duração do jogo, sabendo que o mesmo pode começar em um dia e terminar em outro, tendo uma duração mínima de 1 hora e máxima de 24 horas.

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/1046

# Resolução

Nesse problema fiz o uso de uma biblioteca chamada [math.h](http://linguagemc.com.br/a-biblioteca-math-h/), que possui funções matemáticas prontas e a função utilizada foi a "abs" que faz o papel do módulo(retorna valores positivos):
```c
        #include <math.h>
```
Iremos trabalhar com horas, portanto temos que ler dois valores inteiros sendo eles hora inicial e hora final:
```c
        int h_inicio, h_fim;
        scanf("%d%d", &h_inicio, &h_fim);
```
No problema há a possibilidade do jogo começar em um dia e terminar no outro:
```c
        if (h_inicio>12 && h_fim<12)
        {
            printf("O JOGO DUROU %d HORA(S)\n", abs(abs(h_inicio-12)-(h_fim+12)));
        }
```
No if irá ser testado o caso do horário inicial passar das 12h e o final passar das 00h.
Precisamos do abs, pois estamos trabalhando com horas, portanto só valores possitivos.
Temos a possibilidade do jogo se inicar antes das 12h e acabar após as 12h:

```c
        if (h_inicio<12&&h_fim>12)
        {
            printf("O JOGO DUROU %d HORA(S)\n", abs((h_inicio+12)-abs(h_fim+12)));
        }
```
E para finalizar pode ocorrer do jogo durar 24h e para isso fazemos:
```c
        if (h_inicio==0&&h_fim==0 || h_inicio==h_fim)
        {
            printf("O JOGO DUROU 24 HORA(S)\n");
        }
```
Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para petbcc.ufscar@gmail.com

##### Para aprender um pouco mais sobre:
[Operadores Lógicos em C](http://linguagemc.com.br/operadores-logicos-em-c/#:~:text=Os%20operadores%20lógicos%20são%20utilizados,condições%20simples%20em%20expressões%20lógicas.)



