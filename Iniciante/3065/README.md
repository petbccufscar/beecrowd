# Problema:
A disseminação dos computadores se deve principalmente à capacidade de eles se comportarem como outras máquinas, vindo a substituir muitas destas. Esta flexibilidade é possível porque podemos alterar a funcionalidade de um computador, de modo que ele opere da forma que desejarmos: essa é a base do que chamamos programação.
Sua tarefa é escrever um programa que faça com que o computador opere como uma calculadora simples. O seu programa deve ler expressões aritméticas e produzir como saída o valor dessas expressões, como uma calculadora faria. O programa deve implementar apenas um subconjunto reduzido das operações disponíveis em uma calculadora: somas e subtrações.

**Problema Completo**: https://www.urionlinejudge.com.br/judge/pt/problems/view/3065


# Resolução:

De início, declaramos as variáveis que usaremos, todas do tipo `int`: `operandos` que receberá a quantidade de operandos de cada expressão e servirá como controle de teste; `expressao` que receberá cada operanda presente na expressão que estiver sendo calculada no momento; `i` que servirá comoa auxiliar em loops; `teste` que assumirá o valor representante do teste que está sendo feito no momento; `resultado` que receberá os valores do resultado da expressão que estiver sendo calculada.
``` c
    int operandos, expressao, i, teste = 0, resultado;
```

Agora, por meio de uma função `scanf` leremos o valor de `operandos`. Ademais, com um loop `while` conferiremos os valores de entrada de cada teste, sendo que, se `operandos` for igual a zero significa que os testes se encerraram e se for igual X!=0 temos a quantidade de membros da expressão. Além disso, iniciamos os procedimentos para cada expressão. Dessa forma, atribuímos à `resultado` o valor de 0 e à `teste` somamos um - este procedimento é necessário no início de cada teste (as demais linhas de códgio do loop foram omitidas para futuras explicações).
``` c
    scanf("%d", &operandos);
    while (operandos != 0) {
        resultado = 0;
        teste += 1;
    /* código omitido */
    }

Continuando, abrimos um loop for com o auxílio de `i` e limite máximo sendo o valor de `operandos`, caracterizando o intervalo de `i`=1 até `i`=`operandos`. Assim sendo, dentro do loop leremos, por meio de `scanf`, o valor de cada número da expressão e atribuímos a `expressão`. Após isso, somamos o valor do membro em questão ao valor de `resultado`. Como a linguagem C interpreta número com sinais de + e - como valores e não uma expressão, não é preciso se preocupar em ler a operação que estiver sendo feita. 
``` c
        for (i=1; i<=operandos; i++) {
            scanf("%d", &expressao);
            resultado += expressao;
        }
```

Por fim, através de `printf`, imprimimos na tela a mensagem "Teste " com o valor de `teste` e, na linha de baixo, o valor de `resultado`. Ademais, lemos o novo valor de `operandos` para que o próximo teste se inicie.
``` c
        printf("Teste %d\n", teste);
        printf("%d\n\n", resultado);
        scanf("%d", &operandos);
```
Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com