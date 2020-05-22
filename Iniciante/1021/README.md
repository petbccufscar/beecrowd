# Problema:

Leia um valor de ponto flutuante com duas casas decimais. Este valor representa um valor monetário. A seguir, calcule o menor número de notas e moedas possíveis no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2. As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01. A seguir mostre a relação de notas necessárias.

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/1021

# Resolução:

Na função main(), iremos declarar uma variável para armazenar o valor monetário a ser inserido pelo usuário. Como o enunciado exige um valor de **ponto flutuante**, utilizaremos o tipo de variável `double`.
Devemos declarar, também, variáveis para guardar a quantidade necessária de cada nota e moeda. Visto que só é possível termos quantidades inteiras (não existindo 0,5 nota ou moeda), estas serão do tipo `int`, inicializadas com valor igual a zero.

```c
        double N;
        int notas100=0, notas50=0, notas20=0, notas10=0, notas5=0, notas2=0;
        int moedas1r=0, moedas50=0, moedas25=0, moedas10=0, moedas5=0, moedas1c=0;
```

##### Para aprender mais sobre variáveis de ponto flutuante: [Os tipos float e double](https://www.cprogressivo.net/2012/12/Os-tipos-float-e-double-numeros-decimais-reais-em-C.html)

##### Para aprender mais sobre variáveis do tipo inteiro: [O tipo inteiro](https://www.cprogressivo.net/2012/12/O-tipo-inteiroint-na-linguagem-C.html)

Em seguida, faremos a leitura do valor monetário utilizando a função `scanf()`, a qual deve conter o argumento `%lf`, representando que trata-se de uma variável do tipo `double`.
Além disso, para que o exercício apresente a solução correta, precisaremos acrescentar 0.001 no valor da entrada, garantindo que o valor das 2 primeiras casas decimais (o enunciado solicita apenas esta precisão) não serão arredondadas.

```c
        scanf("%lf", &N);
        N = N + 0.001;
```

Iremos inserir uma estrutura `if` para cumprir a exigência de que o valor de entrada deve ser 0≤N≤1000000.00. Dentro deste estarão contidos a lógica do exercício e impressão das saídas resultantes. Ademais, é importante iniciarmos pelos maiores valores de notas/moedas, prezando, assim, pela menor quantidade possível destas ao final.
Tendo a entrada armazenada em `N`, verificamos se seu valor é maior ou igual ao maior valor existente (no caso, a nota de R$100,00), pois somente neste cenário conseguiremos utilizá-la. Em caso afirmativo, deve-se armazenar na variável `notas100` a quantidade máxima que podemos usufruir, sendo que este cálculo resulta da divisão do valor total pelo valor atual (neste caso: `N/100`). Como o valor de `N` pode conter parte decimal, o resultado desta divisão também tem possibilidade de apresentar-se do mesmo modo. Todavia, queremos apenas a parte inteira do resultado, a qual representa quantas notas de 100 reais precisaremos usar. Para que isto ocorra, é necessário inserir `(int)` anteriormente à conta.
Posteriormente, o valor da entrada tem de ser atualizado, subtraindo deste o valor de todas as notas de 100 utilizadas, ou seja, [valor da nota] * [quantidade de notas]. E, por fim, será feito o uso da função `printf()` para exibir a quantidade de notas R$100,00 necessárias, cujo valor está armazenado na variável de tipo `int`, fazendo com que o argumento desta função seja `%d`.

```c
    if(0<=N<=1000000.00){
      printf("NOTAS:\n");

      if(N>=100){
        notas100 = (int)(N/100);
        N = N - (100*notas100);
      }
      printf("%d nota(s) de R$ 100.00\n", notas100);
    }
```

Este mesmo procedimento deve ser realizado para as demais notas e moedas contidas no enunciado do problema, mantendo dentro do primeiro `if`.

##### Para aprender mais sobre a estrutura condicional: [O teste condicional if else](https://www.cprogressivo.net/2013/01/O-testecondicional-IF-ELSE.html)

##### Para aprender mais sobre formatação de saída: [A printf format reference page](https://alvinalexander.com/programming/printf-format-cheat-sheet/)
