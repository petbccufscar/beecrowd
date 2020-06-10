# Problema:

Pedrinho está organizando um evento em sua Universidade. O evento deverá ser no mês de Abril, iniciando e terminando dentro do mês. O problema é que Pedrinho quer calcular o tempo que o evento vai durar, uma vez que ele sabe quando inicia e quando termina o evento.

Sabendo que o evento pode durar de poucos segundos a vários dias, você deverá ajudar Pedrinho a calcular a duração deste evento.

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/1061

# Resolução:

Primeiro, precisamos declarar as variáveis que representam as entradas: Dia, horas, minutos e segundos do início e final do evento.
```c
        int diaInicial, horasInicial, minutosInicial, segundosInicial;
        int diaFinal, horasFinal, minutosFinal, segundosFinal;
        int diaResposta, horasResposta, minutosResposta, segundosResposta;
```
Note que também foi criado as variáveis que terminam com Resposta, que representarão a saída.

##### Para aprender um pouco mais sobre variáveis: [Variáveis](http://linguagemc.com.br/variaveis-em-linguagem-c/)

Para leitura das notas, utilizamos a função **scanf**:
```c
        scanf("Dia %d %d : %d : %d ", &diaInicial, &horasInicial, &minutosInicial, &segundosInicial);
        scanf("Dia %d %d : %d : %d", &diaFinal, &horasFinal, &minutosFinal, &segundosFinal);
```
Note que precisamos colocar o formato exato dos dados que serão recebidos de entrada para que nosso programa saiba o que esperar.

##### Para entender melhor a função scanf e o porquê ela precisa receber o formato exato dos dados: [scanf](https://www.tutorialspoint.com/c_standard_library/c_function_scanf.htm)

Agora precisamos calcular a diferença de tempo entre o começo e o final do evento, para saber sua duração:
```c
        segundosResposta = segundosFinal - segundosInicial;
        minutosResposta = minutosFinal - minutosInicial;
        horasResposta = horasFinal - horasInicial;
        diaResposta = diaFinal - diaInicial;
```
Note que somente isso não resolve o problema, no casos do segundosResposta, minutosResposta e horasResposta, estes valores podem ter ficados negativos, então precisamos considerar que: 
- Tempo negativo não existe, precisamos corrigir o valor;
- Precisamos propagar a conta entre os valores.

Ou seja, os segundos afetam os minutos, que afetam as horas, que afetam os dias.

Para fazer essa correção e propagação, fazemos:

```c
        if(segundosResposta < 0){
            segundosResposta += 60;
            minutosResposta--;
        }

        if(minutosResposta < 0){
            minutosResposta += 60;
            horasResposta--;
        }

        if(horasResposta < 0){
            horasResposta += 24;
            diaResposta--;
        }
```

Note que, por exemplo, a expressão segundosResposta += 60 é equivalente a segundosResposta = segundosResposta + 60. Ou seja, essa operação soma 60 na variável segundosResposta. Isso é feito pois, se segundosResposta for menor que 0, precisamos consertar o valor. Adicional a isso, fazemos minutosResposta-- que é equivalente a minutosResposta = minutosResposta - 1, pois se os segundos ficaram negativos, isso afeta os minutos. 
O mesmo citado acima vale para minutosResposta < 0 e horasResposta < 0, com a diferença que em horasResposta é feito horasResposta += 24, pois um dia tem 24 horas.

Com os valores agora devidamente corrigidos, basta apresentar na tela a duração do evento com a função **printf**
```c
        printf("%d dia(s)\n", diaResposta);
        printf("%d hora(s)\n", horasResposta);
        printf("%d minuto(s)\n", minutosResposta);
        printf("%d segundo(s)\n", segundosResposta);
```

###### Todas as funções utlizadas estão contidas na biblioteca stdio.h, incluída na primeira linha do nosso programa.
