# Problema

Dizemos que uma sequência de números é uma escadinha, se a diferença entre números consecutivos é sempre a mesma. Por exemplo, “2, 3, 4, 5” e “10, 7, 4” são escadinhas. Note que qualquer sequência com apenas um ou dois números também é uma escadinha! Neste problema estamos procurando escadinhas em uma sequência maior de números. Dada uma sequência de números, queremos determinar quantas escadinhas existem. Mas só estamos interessados em escadinhas tão longas quanto possível. Por isso, se uma escadinha é um pedaço de outra, consideramos somente a maior. Por exemplo, na sequência “1, 1, 1, 3, 5, 4, 8, 12” temos 4 escadinhas diferentes: “1, 1, 1”, “1, 3, 5”, “5, 4” e “4, 8, 12”.
**Problema completo **: [https://www.urionlinejudge.com.br/judge/pt/problems/view/2782]

# Resolução 

De início declaramos as variáveis que usaremos, nesse caso: `tamanho_sequencia` que assumirá o valor  da quantidade de elementos da sequência; `sequencia` o vetor que vai receber os valores da sequência; `i` para auxiliar nos futuros loops. Ademais, declaramos inicialmente `tamanho_sequencia` com valor de 1000, pois assim já o usamos a variável no vetor `sequencia`, e declaramos `escadinha` = 1, porque um único número é uma escadinha.
``` c
    int tamanho_sequencia = 1000, sequencia[tamanho_sequencia], escadinhas = 1, i;
``` 

Agora, com a função `scanf`, lemos o tamanho da sequência.
``` c
    scanf("%d", &tamanho_sequencia);
```

Dando continuidade, fazemos um loop `for`, com a variável auxiliar `i`, para receber os valores da sequência a ser analisada e armazená-los em `sequencia`. 
``` c
    for (i = 0; i < tamanho_sequencia; i++) {
        scanf("%d", &sequencia[i]);
    }
```

Agora, para contarmos as escadinhas seguimos a seguinte lógica: com a ajuda da variável `i` analisamos sempre 3 números seguidos que estão em `sequencia` (`i`, `i+1` e `i+2`), fazemos as diferenças entre eles, na ordem. Se `(sequencia[i] - sequencia [i + 1]` for diferente de `(sequencia[i + 1] - sequencia[i + 2])`, significa que uma escadinha foi terminada, pois um e dois número(s) apenas são uma escadinha, logo os resultados das diferenças entre mais de 2 números serem diferentes indica que não há a continuação de uma escadinha e, portanto, uma nova se inícia. Dessa forma, usamos um loop `for` para percorrer todos os elementos de `sequencia` e com uma estrutura condicional `if`, utilizando o operador lógico `!=` (diferente), verificamos a lógica descrita acima. Quando, a a condição for atendida aumentamos em 1 o valor de `escadinhas` 
``` c
    for (i = 0; i < (tamanho_sequencia - 2); i++) {
        if ( (sequencia[i] - sequencia [i + 1]) != (sequencia[i + 1] - sequencia[i + 2]) ) {
            escadinhas = escadinhas + 1;
        }
    }
``` 
Por fim, escrevemos o valor de `escadinha` com a função `printf`.
``` c
    printf("%d\n", escadinhas);
```