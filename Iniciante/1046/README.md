# Problema 

Leia a hora inicial e a hora final de um jogo. A seguir calcule a duração do jogo, sabendo que o mesmo pode começar em um dia e terminar em outro, tendo uma duração mínima de 1 hora e máxima de 24 horas.

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/1046

# Resolução
Lembrando de iniciar o código com as bibliotecas padrões:
```c
        #include <stdio.h>
        #include <stdlib.h>
```
Nesse problema fiz o uso de uma biblioteca chamada math, que possui funções matemáticas prontas:
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
        if (h_inicio>12 && h_fim<12) //Isso ocorre quando o horario inicial passa das 12h e o final passa das 00h
        {
            printf("O JOGO DUROU %d HORA(S)\n", abs(abs(h_inicio-12)-(h_fim+12))); //Abs eh uma funcao do math.h que retorna o valor absoluto(possitivo)
                                                                                   //se faz nescessario utilizar, pois estamos trabalhando com horas
        }
```
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
Sempre lembrando de finalizar o código:
```c
    return 0;
```

##### Para aprender mais sobre a biblioteca math.h: 
[Funções presentes na math.h](http://linguagemc.com.br/a-biblioteca-math-h/)


