# Problema:

Neste problema, deve-se ler o código de uma peça 1, o número de peças 1, o valor unitário de cada peça 1, o código de uma peça 2, o número de peças 2 e o valor unitário de cada peça 2. Após, calcule e mostre o valor a ser pago.

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/1010

# Resolução:

Uma forma de resolver o problema é quebrá-los em etapas menores. Com base no enunciado, podemos dividir o problema da seguinte maneira: dividir o valor total em subvalores de cada peça e somá-los.

Para isso, é preciso ler os dados da peça 1: código, número de peças, valor unitário, calcular o subvalor total da peça 1 e adicioná-lo ao total. Em seguida, faz-se o mesmo com os dados da peça 2.

Para representar esses valores em nosso programa, fazemos: 

```c
        int codigo, numeroPecas;
        float valorPeca, valorTotal;
        valorTotal = 0;
```

Note que, para não se perder o subvalor obtido da peça 1, ao calcular o subvalor da peça 2, é necessário armazená-lo em uma outra variável antes de calcular o subvalor da peça 2, neste caso a variável utilizada para tal é valorTotal, que precisa ser iniciado com zero, pois será incrementádo mais a frente.

##### Para aprender um pouco mais sobre variáveis: [Variáveis](http://linguagemc.com.br/variaveis-em-linguagem-c/)

Para ler as variáveis, usa-se scanf:

```c
        scanf("%d %d %f", &codigo, &numeroPecas, &valorPeca);
```

É possível inserir mais de um dado dentro de um mesmo scanf separando os %(variavel), lembrando que a ordem da variaveis inseridas no "" deve corresponder com a ordem dos endereços de memoria indicados na função. Durante a execução do programa, usamos . para separar o valor decimal do inteiro.

Após a leitura das variáveis, calcula-se o subvalor da peça em questão e incrementa-o no valor total. O subvalor da peça a multiplicação do número de peças pelo valor unitário, sendo assim:

```c
        valorTotal = valorTotal + (valorPeca * numeroPecas);
```

Em seguida, repete-se este método para a peça 2 e com isso, obtemos o valor total e escrevemos o resultado na tela utilizando a função printf:

```c
        printf("VALOR A PAGAR: R$ %.2f\n", valorTotal);
```

O '%0.2lf' será substituido pelo valor contido em valorTotal. O '.2' indica quantas casas decimais serão mostradas na tela, que no caso são duas.

##### Para aprender um pouco mais sobre tipos de variáveis: [Tipos de Variáveis](http://linguagemc.com.br/tipos-de-dados-em-c/)

###### Todas as funções utlizadas estão contidas na biblioteca stdio.h, incluída na primeira linha do nosso programa.

###### Adento 1:
		
Como não se utiliza o valor de código em momento algum, uma solução que utilizaria uma variável a menos seria da seguinte forma:
```c
        int numeroPecas;
        float valorPeca, valorTotal;
        valorTotal = 0;

        scanf("%d %d %f", &numeroPecas, &numeroPecas, &valorPeca);
        ...
```

