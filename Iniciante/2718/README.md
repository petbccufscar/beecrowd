# Problema:
Giovanna adora o Natal. Porém, esse ano a pequena Gio ficou triste ao perceber que seu jogo de luzes está quebrado. Algumas luzes ainda funcionam, outras não. Giovanna quer consertar seu objeto preferido mas não tem lâmpadas o suficiente pra substituir todas as queimadas então resolveu fazer o seguinte: dividir o pisca pisca em grupos ordenados de 50 lâmpadas e em cada grupo só consertar a maior quantidade de lâmpadas consecutivas queimadas.

Por serem muitos grupos, Giovanna observou a semelhança dos grupos com representação binária de números quando imaginava lâmpadas queimadas como 1's e lâmpadas funcionais como 0's, decidiu pensar neles efetivamente como números e escreveu as representações decimais desses binários então tentou descobrir a quantidade de lâmpadas a serem trocadas a partir dessas anotações.

Diga quantas lâmpadas serão trocadas em cada grupo.

##### Link do problema: https://www.urionlinejudge.com.br/judge/pt/problems/view/2718

# Resolução:
O exercício consiste em ler o número de grupos, ler um inteiro equivalente a cada grupo e com base nesses números, imprimir a maior sequência de lâmpadas consecutivas queimadas em cada grupo .

Primeiro instanciamos as variáveis necessárias, sendo elas: 1 `unsigned long long` (precisamos dele pois é necessário no mínimo 50 bits para comportar um grupo inteiro, no caso, esse comporta 64 bits) e 3 `int` (`seq` para armazenar o tamanho da sequência atual; `max` para armazenar o tamanho da maior sequência de um grupo; `N` para o número de grupos).
Começamos lendo o número de grupos.

Obs: Como vamos ler um `unsigned long long`, iremos ler utilizando `%llu`.

```c
    unsigned long long X;
    int max, seq, N;
    scanf("%d", &N);
```
 
Agora iremos utilizar um `while(N--)` para passar por todos os grupos. Dentro dele iremos ler o valor de `X` e zerar os valores de `seq` e `max` para utilizá los. Após isso iremos utilizar outro `while`.

```c
    while(N--) {
        scanf("%llu", &X);
        max = 0;
        seq = 0;

        //while (X > 0)

    }
```

Nesse `while(X > 0)` verificamos se o bit mais à direita é 1 (logo indicando que a lâmpada esteja queimada), caso verdadeiro incrementamos `seq` e se `seq > max` colocamos o conteúdo de `seq` em `max`, caso contrário zeramos `seq`. Ao final do `while` damos um shift para a direita em `X`, o shift transloca todos os bits um bit para a direita e o bit mais à esquerda se torna `0`, os operadores de shift são conhecidos como bitwise.  
**Obs:** Esse `while` so vai terminar quando todos os bits do `X` forem 0, ou seja, quando ele armazenar o 0, por isso `X > 0`.

```c
    while (X > 0) {
        if ((X & 1) == 1) {
            seq++;
            if (seq > max) {
                max = seq;
            }
        } else {
            seq = 0;
        }
        X >>= 1;
    }
```

Ao final do `while` externo imprimimos o valor de `max` (que é a maior sequência de lâmpadas queimadas do grupo referente) antes de o reiniciar.

```c
    printf("%d\n", max);
```

##### Para aprender um pouco mais sobre a estrutura While: [While](http://linguagemc.com.br/o-comando-while-em-c/)
##### Para aprender um pouco mais sobre a estrutura Bitwise: [Bitwise](https://en.wikipedia.org/wiki/Bitwise_operations_in_C)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
