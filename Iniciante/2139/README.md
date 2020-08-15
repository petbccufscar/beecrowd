# Problema

Pedrinho é um garoto que adora festas em família, principalmente o Natal, quando ganha presente dos pais e dos avós. Esse ano, seu pai lhe prometeu um PS4, mas somente se Pedrinho conseguir resolver alguns desafios ao longo do ano, sendo um deles, escrever um programa que calcule quantos dias faltam para o Natal.

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/2139

# Resolução

Para resolver o problema, iremos criar um vetor de meses com quantos dias cada um tem e trabalhar com a estrutura de verificação `if` para verificar qual caso encaixa-se cada entrada.

Começaremos declarando as variáveis. Todas são valores inteiros, categorizando o tipo `int`. Teremos variáveis para o mês, dia, total de dias faltantes e contador da estrutura de repetição.
```c
    int mes, dia, total, i;
```

Em seguida, declararemos o vetor de dias em cada mês. Como cada mês tem uma quantidade específica de dias, iremos colocá-las explicitamente no vetor em sua declaração. Consideraremos 28 dias para o 2º mês (fevereiro) por ser um ano bissexto e 25 dias para o 12º mês (dezembro) para encaixar-se nos critérios de véspera/dia de natal.
```c
    int dias_mes[12] = {31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 25};
```

Inicializamos nossa estrutura de repetição `while`. Como nosso critério de parada do programa é a leitura de um `End Of File (EOF)`, colocaremos a função de leitura `scanf` dentro desta área de condição do `while`. Assim, quando a leitura do `scanf` for `EOF`, nosso programa terminará.
```c
    while(scanf("%d%d", &mes, &dia) != EOF)
```

Caso seja o 12º mês e o dia 25, exibiremos a mensagem `"E natal!"` na tela com a estrutura `printf`.
```c
        if(mes == 12 && dia == 25) 
            printf("E natal!\n");
```

Caso seja um dia antes (24), exibiremos a mensagem de véspera.
```c
        else if(mes == 12 && dia == 24) 
            printf("E vespera de natal!\n");
```

Caso seja depois, porém ainda no mês de dezembro, exibiremos a mensagem `Ja passou!`
```c
        else if(mes == 12 && dia > 25) 
            printf("Ja passou!\n");
```

Caso não seja nenhuma das condições tratadas, temos que contabilizar quanto tempo falta para o natal.
Primeiro, contabilizamos quantos dias faltam para que o mês inserido termine. Para isso, iremos checar no vetor `dias_mes` quantos dias o mês têm no total e subtrair o dia inserido, salvando na variável `total`.
```c
        total = dias_mes[mes-1] - dia;
```
Utilizamos `mes-1` pois o vetor inicia com índice 0.

Em seguida, iremos somar todos os meses restantes (iniciando-se no mês inserido) para somar quantos dias faltam para o natal. Utilizaremos a estrutura de repetição `for`.
```c
            for(i = mes; i < 12; i++)
                total = total + dias_mes[i];
```

Finalmente, exibiremos a mensagem com o total de dias faltantes para o natal.
```c
        printf("Faltam %d dias para o natal!\n", total);
```

##### Para aprender um pouco mais sobre vetores: [vetores](http://linguagemc.com.br/vetores-ou-arrays-em-linguagem-c/)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
* [Facebook](https://www.facebook.com/petbcc/),
* [Instagram](https://www.instagram.com/petbcc.ufscar/)
* ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
