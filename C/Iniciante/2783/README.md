# Problema 

Em ano de Copa do Mundo de Futebol, o álbum de figurinhas oficial é sempre um grande sucesso entre crianças e também entre adultos. Para quem não conhece, o álbum contém espaços numerados de 1 a N para colar as figurinhas; cada figurinha, também numerada de 1 a N, é uma pequena foto de um jogador de uma das seleções que jogará a Copa do Mundo. O objetivo é colar todas as figurinhas nos respectivos espaços no álbum, de modo a completar o álbum (ou seja, não deixar nenhum espaço sem a correspondente figurinha).

Algumas figurinhas são carimbadas (efetivamente têm um carimbo impresso sobre a fotografia do jogador) e são mais raras, mais difíceis de conseguir. As figurinhas são vendidas em envelopes fechados, de forma que o comprador não sabe quais figurinhas está comprando, e pode ocorrer de comprar uma figurinha que ele já tenha colado no álbum.

Para ajudar os usuários, a empresa responsável pela venda do álbum e das figurinhas quer criar um aplicativo que permita gerenciar facilmente as figurinhas que faltam para completar o álbum.

Dados o número total de espaços e figurinhas do álbum (N), a lista das figurinhas carimbadas e uma lista das figurinhas já compradas (que pode conter figurinhas repetidas), sua tarefa é determinar quantas figurinhas carimbadas faltam para completar o álbum.
**Problema completo**: [https://www.urionlinejudge.com.br/judge/pt/problems/view/2783]

# Resolução

De início declaramos as variáveis que usaremos, nesse caso: `carimbadas` que será um ponteiro para criação de um vetor que irá armazenar os valores das figurinhas que são carimbadas; `compradas` que assumirá os valores das figurinhas compradas; `carimbadas_restantes` que assumirá os valores das figurinhas obtidas que são carimbadas; `n_figurinhas` que assumirá o valor da quantidade total de figurinhas presente no álbum; `c_carimbadas` que assumirá o valor da quantidade de figurinhas carimbadas presentes no álbum; `m_compradas` que assumirá o valor do total de figurinhas compradas; `i` e `j` que serão variáveis auxiliares em futuros loops.

``` c
    int *carimbadas, compradas, carimbadas_obtidas;
    int n_figurinhas, c_carimbadas, m_compradas, i, j;
```

Dando prosseguimento, iremos ler os valores de `n_figurinhas`, `c_carimbadas` e `m_compradas` com a função `scanf`. Ademais, atribuímos à variável `carimbadas_restantes` o valor de `c_carimbadas`, pois partimos do princípio que faltam todas as figurinhas carimbadas e, futuramente, conforme formos averiguando quais figuras carimbadas foram compradas, fazemos os descontos necessários desse valor para representar a quantidade ainda faltante.

``` c
    scanf("%d", &n_figurinhas);
    scanf("%d", &c_carimbadas );
    scanf("%d", &m_compradas);
    carimbadas_restantes = c_carimbadas;
```

Agora, trataremos de `carimbadas`, como, inicialmente, não sabíamos o valor da quantidade de figurinhas carimbadas utilizamos de um ponteiro, pois não era sabido a quantidade de bytes necessária. Dessa forma, com o valor obtido de `c_carimbadas` fazemos a alocação de memória necessária com a função `malloc`. Por se tratar de um vetor de inteiros multiplicamos a função `sizeof`, com o parâmetro `int`, pelo valor de `c_carimbadas` e obtemos os bytes que serão precisos para nosso vetor. Ademais, `malloc` retorna um ponteiro do tipo `void`, sendo assim, precisamos converte-lo para `int`, por isso usamos o comando de conversão explicíta `(int *)`.

``` c
    carimbadas = (int *) malloc(c_carimbadas   * sizeof(int));
```

Seguindo, fazemos a atribuição dos valores das figurinhas carimbadas para cada elemento do nosso vetor através de um loop `for` que, auxiliado por `i`, lerá N valores, sendo N = `c_carimbadas`. Para tal, fazemos `i` percorrer de 0 até `c_carimbadas` - 1, ao passo de um elemento.

``` c
    for (i = 0; i < c_carimbadas  ; i++) {
        scanf("%d", &carimbadas[i]);
    }
```

Em sequência, fazemos outro loop `for` com um ciclo de repetição de 0 até `m_compradas` - 1. Nesse loop iremos ler os valores das figurinhas compradas e, um por um, atribuíremos à `compradas` comparando o valor as figurinhas carimbadas do álbum. Sendo assim, dentro do primeiro loop faremos outro loop `for`, com auxilio de `j`, que percorerrá os elementos de `carimbadas`. Se o valor da figurinha comprada lido for igual a um valor presente no vetor das figurinhas carimbadas, subtraímos em 1 o valor de `carimbadas_restantes`, dando baixa na figurinha em questão. Entretanto, quando a condição anterior for atendida, temos que alterar o valor da figurinha carimbada, para evitar múltiplas baixas de uma mesma figurinha - tal processo é necessário, porque é possível comprar uma mesma figurinha diversas vezes. Para execução de tais processos, usamos a estrutura condicional `if` e dentro dela fazemos as atribuições e alterações necessárias. 

``` c
    for (i = 0; i < m_compradas; i++) {
        scanf("%d", &compradas);
        for (j = 0; j < c_carimbadas; j++) {
            if (compradas == carimbadas[j]) {
                carimbadas_restantes = (carimbadas_restantes - 1);
                carimbadas[j] = carimbadas[j] + n_figurinhas;  
            }
        }
    }
```

Por fim, basta imprimir o valors das figurinhas carimbadas que ainda faltam. Para tal, usamos da função `printf` e do valor de `carimbadas_restantes`.

``` c
    printf("%d\n", carimbadas_restantes);
```

#### Para mais informações sobre ponteiros: [https://www.treinaweb.com.br/blog/ponteiros-em-c-uma-abordagem-basica-e-inicial/]
#### Para mais informações sobre alocação dinâmica e funções auxiliares desse processo: [http://linguagemc.com.br/alocacao-dinamica-de-memoria-em-c/] [http://linguagemc.com.br/o-comando-syzeof/]

