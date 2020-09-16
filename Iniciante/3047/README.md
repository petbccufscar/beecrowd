# Problema:
Dona Mônica é mãe de três filhos que têm idades diferentes. Ela notou que, neste ano, a soma das idades dos seus três filhos é igual à idade dela. Neste problema, dada a idade de dona Mônica e as idades de dois dos filhos, seu programa deve computar e imprimir a idade do filho mais velho. Por exemplo, se sabemos que dona Mônica tem 52 anos e as idades conhecidas de dois dos filhos são 14 e 18 anos, então a idade do outro filho, que não era conhecida, tem que ser 20 anos, pois a soma das três idades tem que ser 52. Portanto, a idade do filho mais velho é 20. Em mais um exemplo, se dona Mônica tem 47 anos e as idades de dois dos filhos são 21 e 9 anos, então o outro filho tem que ter 17 anos e, portanto, a idade do filho mais velho é 21.

##### Link do problema: https://www.urionlinejudge.com.br/judge/pt/problems/view/3047
 
# Resolução:

O exercício consiste em ler a idade da Dona Mônica e de dois dos seus filhos, assim encontrar a idade do terceiro filho e imprimir a idade do filho mais velho.


Primeiro instanciamos as variáveis necessárias, sendo elas: 4 `int` (`M` para a idade da Mônica; `A` para um filho; `B` para o outro filho; `X` para o ultimo filho).
Começamos lendo as idades de Mônica e de dois filhos.

```c
    int M, A, B, X;

    scanf("%d %d %d", &M, &A, &B);
```

Para descobrirmos a idade do ultimo filho basta subtrairmos as idades dos filhos que ja conhecemos da idade da Mônica, como explicado no enunciado.

```c
    X = M - A - B;
```

Agora só resta descobrirmos qual filho é o mais velho, iremos utilizar `if` e `else` para descobrir, primeiro verificamos se `X` é maior que `A` e `B`, se for verdadeiro imprimimos `X` senão verificamos se `A` é maior que `X` e `B`, se for verdadeiro imprimimos `A`, caso contrario imprimimos `B`.

```c
    if (X > A && X > B)
        printf("%d\n", X);
    else if (A > B && A > X)
        printf("%d\n", A);
    else
        printf("%d\n", B);
```

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
