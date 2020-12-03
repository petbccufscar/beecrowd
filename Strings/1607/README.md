# Problema:

É dado na entrada uma string A e outra B. Em uma operação você pode escolher uma letra da primeira string e avançar esta letra. Avançar uma letra significa transformá-la na próxima letra do alfabeto, veja que a próxima letra depois de z vem a letra a novamente!

Por exemplo, podemos transformar a string ab em bd em no mínimo 3 operações: ab -> bb -> bc -> bd. Podemos aplicar operações nas letras em qualquer ordem, outra possibilidade seria: ab -> ac -> bc -> bd.

Dadas as duas strings, calcule o mínimo número de operações necessárias para transformar a primeira na segunda.

**Problema Completo**: https://www.urionlinejudge.com.br/judge/pt/problems/view/1607

# Resolução:

Para a resolução deste problema utilizanos apenas biblioteca padrão `stdio.h`.

```c
#include <stdio.h>
```

Após informar a biblioteca, iniciamos o nosso algoritmo. Primeiramente, declaramos uma variável do tipo inteiro chamada `T`, pois é sugerido na entrada que a primeira linha terá um inteiro T (T ≤ 100) indicando o número de casos de teste. E em seguida fazemos a leitura do número de casos testes, armazenando nesta variável com o comando de leitura `scanf()`. Logo após, entramos na parte lógica do nosso código, que está explicada logo abaixo.

```c
int main()
{
    int T;

    scanf("%d", &T);

    /**
     * restante do código aqui (informado abaixo)
    **/

    return 0;
}
```

É necessário fazer uma estrutura `while()` para cada caso teste. Após, declaramos duas variáveis do tipo caractere chamadas `stringA[10001]` e `stringB[10001]` e em seguida fazemos a leitura desta variável com o comando `scanf()`. Também são declaradas as variáveis `*p1` e `*p2` do tipo caractere que serão utilizadas na parte lógica do problema, e a variável `operacoes` do tipo inteiro, para contabilizar o número de operações realizadas, sendo que inicialmente é atribuido para a variável `operacoes` o valor 0.

```c
while (T) {
        char stringA[10001], *p1;
        char stringB[10001], *p2;
        int operacoes = 0;

        scanf("%s%s", stringA, stringB);
    
    /**
     * restante do código aqui (informado abaixo)
    **/

        --T;
    }
```

Na sequência é feita uma estrutura `for` na qual é definida uma determinada condição na qual se avança as letras, e dentro desta estrutura é feita uma estrutura condicional de `if` e `else` que verifica e contabiliza o número de operações realizadas. Ao final, com o comando `printf()` é mostrado para cada caso o número mínimo de operações.

```c
        for (p1 = stringA, p2 = stringB; *p1 != '\0'; ++p1, ++p2) {
            if (*p2 >= *p1)
                operacoes += *p2 - *p1;
            else
                operacoes += ('z' - *p1) + (*p2 - 'a') + 1;
        }

        printf("%d\n", operacoes);
```

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/),
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
