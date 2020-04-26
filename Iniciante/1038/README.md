# Problema:

Com base na tabela, escreva um programa que leia o código de um item e a quantidade deste item. A seguir, calcule e mostre o valor da conta a pagar.

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/1038

# Resolução:

Primeiro vamos instanciar a variaveis necessarias, dois inteiros (codigo do pedido e sua quantidade) e um double (para o valor **total**):

```c
    int cod, quant;
	double total;
```

Para ler as duas variáveis, usa-se scanf:

```c
    scanf("%d %d", &cod, &quant);
```
É possível ler mais de um dado dentro do mesmo scanf, como fazemos nesta linha com vários %d (de valores inteiros).

##### Para aprender um pouco mais sobre variáveis: [Variáveis](http://linguagemc.com.br/variaveis-em-linguagem-c/)

##### Para aprender um pouco mais sobre tipos de variáveis: [Tipos de Variáveis](http://linguagemc.com.br/tipos-de-dados-em-c/)

Para calcular o total vamos usar a função **switch()**. Seu funcionamento é selecionar o trecho de código que corresponde ao argumento passado à ele, ou seja, se o inicio for **switch(arg)** e existir um **case arg: code; break;**, code sera executado, caso contrario **default:** será executado.
Obs: Todos os **case** e o **default** devem terminar em **break** senão o programa pode seguir para o próximo caso.

```c
    switch (cod)
	{
	case 1:
		total = quant * 4;
		break;
	case 2:
		total = quant * 4.5;
		break;
	case 3:
		total = quant * 5;
		break;
	case 4:
		total = quant * 2;
		break;
	case 5:
		total = quant * 1.5;
		break;
	default:
		break;
	}
```
##### Para aprender um pouco mais sobre Switch: [Switch](http://linguagemc.com.br/o-comando-switch-case-em-c/)

Agora o que resta é imprimir o resultado utilizando **printf()**, pois o resultado ja está em total.

```c
    printf("Total: R$ %.2f\n", total);      
```

O '%0.2f' será substituido pelo valor contido em salariofinal. O '.2' indica quantas casas decimais serão mostradas na tela, que no caso são duas.

##### Para aprender um pouco mais sobre tipos de variáveis: [Tipos de Variáveis](http://linguagemc.com.br/tipos-de-dados-em-c/)

###### Todas as funções utlizadas estão contidas na biblioteca stdio.h, incluída na primeira linha do nosso programa.
