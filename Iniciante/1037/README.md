# Problema:

Você deve fazer um programa que leia um valor qualquer e apresente uma mensagem dizendo em qual dos seguintes intervalos ([0,25], (25,50], (50,75], (75,100]) este valor se encontra. Obviamente se o valor não estiver em nenhum destes intervalos, deverá ser impressa a mensagem “Fora de intervalo”.

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/1037

# Resolução:

Sabemos que o programa somente irá receber uma informação (valor) do tipo **ponto flutuante**, portanto deveos reservar somente uma variavel do mesmo tipo:

```c
    float valor;
```

##### Para aprender um pouco mais sobre variáveis: [Variáveis](http://linguagemc.com.br/variaveis-em-linguagem-c/)

##### Para aprender um pouco mais sobre tipos de variáveis: [Tipos de Variáveis](http://linguagemc.com.br/tipos-de-dados-em-c/)

Para lermos o um valor do tipo **float** usamos a função **scanf()** e e usamos %f para indicar que será lido um valor tipo **float**:

```c
    scanf("%f", &valor);
```

##### Para aprender um pouco mais operacoes sobre entrada e saida de dados: [Entrada e saída](http://linguagemc.com.br/operacoes-de-entrada-e-saida-de-dados-em-linguagem-c/)

Em seguida faremos uma série de comparações para descobrir o valor esta em algum intervalo valido e se estiver em qual está. Para isso iremos utilizar as funções **if()** e **else** (respectivamente **se** e **senão**) somadas aos operadores relacionais (exemplos **>,>=,=<,<**) e logicos (exemplos **&&, ||**).

Obs: Quando a função **if()** receber o verdadeiro seu trecho que codigo referente será executado e o do **else** não e vice-versa.

Os operadore relacionais retornam se a respectivas comparações são verdadeiras(1) ou falsas(0). Os operadores lógicos faz a correlação dos termos logicos, ou seja, faz a correlação de verdadeiro e falso.

##### Para aprender um pouco mais operacoes sobre entrada e saida de dados: [Operadores relacionais](http://linguagemc.com.br/operadores-relacionais/)

##### Para aprender um pouco mais operacoes sobre entrada e saida de dados: [Operadores logicos](http://linguagemc.com.br/operadores-logicos-em-c/)

Caso não esteja em nenhum intervalo temos que imprimir que o valor esta fora do intervalo, mas caso esteja devemos imprimir qual o intervalo:

```c
if (valor >= 0 && valor <= 25)
  printf("Intervalo [0,25]\n");
else if (valor > 25 && valor <= 50)
  printf("Intervalo (25,50]\n");
else if (valor > 50 && valor <= 75)
  printf("Intervlo (50,75]\n");
else if (valor > 75 && valor <= 100)
  printf("Intervalo (75,100]\n");
else
  printf("Fora de intervalo\n");
```

###### Todas as funções utlizadas estão contidas na biblioteca stdio.h, incluída na primeira linha do nosso programa.