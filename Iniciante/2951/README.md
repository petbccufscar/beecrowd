# Problema 
Frodo e Sam estão prestes a conseguir jogar o anel na Montanha da Perdição, porém Gollum os atrapalha.
Uma pequena pausa na história. Senhor dos Anéis, além de ser um dos maiores clássicos literários e cinematográficos da humanidade, é uma história que deixa evidente o valor da amizade. Dê valor às boas amizades :) Despause.
Gollum é um ser infeliz e que não suporta a amizade. Para que Frodo e Sam consigam passar por ele, eles precisam recitar runas que entoam amizade. Cada runa é representada por uma letra do alfabeto, e indica uma quantidade de amizade que ela emite, podendo ser positiva ou negativa (sim, existem as runas que representam as más amizades). 
Dada a quantidade de amizade necessária para derrotar Gollum, uma lista de runas e seus respectivos valores de amizade e as runas que Sam e Frodo recitaram, dê o valor final de amizade que Frodo e Sam conseguiram e se foi possível ou não derrotar Gollum.
#### Problema completo: [https://www.urionlinejudge.com.br/judge/pt/problems/view/2951]

# Resolução
De início declaramos as variáveis que iremos usar: `runa_atual` que receberá o valor da runa que está sendo recitada; `letras_runas` nosso vetor que receberá as letras que representam cada runa existente; `runas_existentes` que receberá a quantidade de runas que existem; `amizade_necessaria` que receberá o valor de amizade necessário para superar Gollum; `valor_amizade` que receberá os valores de amizade recebidos pelas runas recitadas; `runas_recitadas` que receberá o valor da quantidade de runas recitadas; `valor_runas` nosso vetor que receberá o valor de cada runa existente; `i` e `j` que serão auxiliares.
``` c
    char runa_atual, letras_runas[100];
    int runas_existentes, amizade_necessaria, valor_amizade = 0, runas_recitadas, j, i, valor_runas[100];
```

Agora, leremos os valores de `runas_existentes` e `amizade_necessaria` através da função `scanf`.
``` c
    scanf("%d", &runas_existentes);
    scanf("%d", &amizade_necessaria);
```

Na sequência, através de um loop `for` com limite o valor de `runas_existentes` (intervalo de `i`=0 até `i`=`runas_existentes`-1), leremos a letra que representa a runa em questão e seu valor através da função `scanf`. Sendo assim, alocaremos os dados de letra e valor para `letras_runas` e `valor_runas`, respectivamente. Um detalhe muito importante aqui é: dentro de `scanf` os parâmetros DEVEM ser `(" %c%d", &letras_runas[i], &valor_runas[i])`, esse espaço antes de "%c" faz com que a leitura de caractere da função ignore espaços em brancos, evitando problemas com as demais `scanf`.
``` c
    for (i=0; i<runas_existentes; i++) {
        scanf(" %c%d", &letras_runas[i], &valor_runas[i]);
    }
```

Dando continuidade, leremos o valor de `runas_recitadas` com mais uma função `scanf`. Ademais, dentro de um loop `for` com limite o valor de `runas_recitadas` (intervalo de `i`=0 até `i`=`runas_recitadas`), leremos as runas que foram recitadas, uma a uma, e atribuíremos à `runa_atual`. Desse modo, dentro do primeiro loop, conseguiremos através de outro loop `for`, com limite o valor de `runas_existentes` (intervalo de `j`=0 até `j`=`runas_existentes-1`), percorrer todos as letras que representam as runas que existem e compara-las com `runa_atual`. Logo, por meio de um estrutura condicional `if` comparamos as runas e atribuímos o valor delas à `valor_amizade`. 
``` c
    scanf("%d", &runas_recitadas);
    for (i=0; i<runas_recitadas; i++) {
        scanf(" %c", &runa_atual);
        for (j=0; j<runas_existentes; j++) {
            if (runa_atual == letras_runas[j]) {
                valor_amizade += valor_runas[j];
            }
        }
    }
```
Por fim, imprimimos o valor de amizade obtido com a função `printf`. Por meio de uma estrutura condicional `if` comparamos o valor da amizade que é preciso para derrotar Gollum com o valor obtido, se a amizade obtida for maior ou igual imprimimos "You shall pass!", caso não for, imprimimos "My precioooous".
``` c
    printf("%d\n", valor_amizade);
    if (valor_amizade >= amizade_necessaria) {
        printf("You shall pass!\n");
    }
    else {
        printf("My precioooous\n");
    }
```