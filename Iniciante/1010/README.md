# Problema:

Neste problema, deve-se ler o código de uma peça 1, o número de peças 1, o valor unitário de cada peça 1, o código de uma peça 2, o número de peças 2 e o valor unitário de cada peça 2. Após, calcule e mostre o valor a ser pago.

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/1010

# Resolução:

Uma forma de resolver o problema é quebrá-lo em etapas menores. Como o valor total a ser pago é composto pela soma dos valores de cada peça comprada, podemos resolver o problema da seguinte maneira:**dividir o valor total em subtotais referentes a cada peça, calculá-los e em seguida somá-los, para obter-se o valor total.**

Para isso, é preciso ler os dados da peça 1: o código, o número de peças e o valor unitário, calcular o subtotal da peça 1 e adicioná-lo ao total. Em seguida, faz-se o mesmo com os dados da peça 2.

Para representar esses valores em nosso programa, fazemos: 

```c
        int codigo, numeroPecas;
        float valorPeca, valorTotal;
        valorTotal = 0;
```

Ao declarar uma variável, uma posição da memória será escolhida para tal e esta posição pode conter um valor desconhecido(lixo) já utilizado por outra aplicação. Por isso, `valorTotal` é iniciado com zero, pois será incrementado mais a frente no decorrer do código. Caso não seja inicializado, essa variável terá um valor aleatório e provavelmente irá levar a um resultado errado.

Para ler a entrada, usa-se `scanf`:

```c
        scanf("%d %d %f", &codigo, &numeroPecas, &valorPeca);
```

É possível inserir mais de um dado dentro de um mesmo `scanf` separando os %(variavel), lembrando que a ordem da variaveis inseridas entre as aspas deve corresponder com a ordem dos endereços de memoria indicados na função.

Após a leitura das variáveis, calcula-se o subtotal da peça em questão e incrementa-o no valor total. **O subtotal da peça é a multiplicação do número de peças pelo valor unitário**, sendo assim:

```c
        valorTotal = valorTotal + (valorPeca * numeroPecas);
```

Note que, para não se perder o subtotal obtido da peça 1, ao calcular o subtotal da peça 2, é necessário armazená-lo em uma outra variável antes de calcular o subtotal da peça 2. No caso acima, a variável utilizada para tal é `valorTotal`.

Em seguida, repete-se este método para a peça 2 e com isso, obtemos o valor total e escrevemos o resultado na tela utilizando a função `printf`:

```c
        printf("VALOR A PAGAR: R$ %.2f\n", valorTotal);
```

O `%.2f` será substituido pelo valor contido em `valorTotal`. O '.2' indica quantas casas decimais serão mostradas na tela, que no caso são duas.


##### Para revisar sobre variáveis: [Variáveis](http://linguagemc.com.br/variaveis-em-linguagem-c/)


Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou envie um e-mail com o assunto "URI" para petbcc.ufscar@gmail.com