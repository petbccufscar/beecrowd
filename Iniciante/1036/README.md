# Problema:

Leia 3 valores de ponto flutuante e efetue o cálculo das raízes da equação de Bhaskara. Se não for possível calcular as raízes, mostre a mensagem correspondente “Impossivel calcular”, caso haja uma divisão por 0 ou raiz de numero negativo.

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/1036

# Resolução:
É solicitado que, ao ler 3 valores do tipo ponto flutuante, seja executada a equação de [Bhaskara](https://www.todamateria.com.br/formula-de-bhaskara/) com estes (que representam os coeficientes). Em cenários com **divisão por 0** ou **raiz de número negativo**, é impossível calcular as raízes da equação e isto deve ser exibido ao usuário.


Como a equação de Bhaskara requer a potência B<sup>2</sup>, utilizaremos a função `pow()`, que realiza potenciações. Do mesmo modo, a fórmula deve calcular a raiz quadrada de delta e, para isto, usufruímos da função `sqrt()`. Para utilizar ambas funções, devemos importar no início de nosso código (externamente à main) a biblioteca que as contém, chamada `math.h`.

```c
    #include <math.h>
```

Uma vez que foram fornecidos os nomes das variáveis a serem utilizados, declaramos A, B e C. Na instrução de entrada, é informado que estas possuem valor de ponto flutuante e, portanto, utilizaremos o tipo de variável `double` e o argumento `%lf` para ler/escrever. Além disso, precisaremos também de variáveis deste mesmo tipo para armazenar o valor de Δ e das duas raízes resultantes, respectivamente `delta`, `R1` e `R2`.

```c
    double A, B, C;
  	double delta, R1, R2;

  	scanf("%lf %lf %lf", &A, &B, &C);
```


Caso o valor de A seja equivalente a zero, a equação de Bhaskara não poderá ser efetuada. Desse modo, utilizamos a estrutura condicional `if` para conter este cenário e, assim, exibir na tela "Impossivel calcular".

```c
        if(A == 0)
      		printf("Impossivel calcular\n");
```

Porém, se A não contiver valor zero, a estrutura `else` indicará o que deve ser feito. Neste caso, iniciaremos realizando o cálculo de Δ, o qual equivale a B<sup>2</sup> subtraindo o valor da operação 4*A*C. A função `pow()` contém dois argumentos, sendo que o primeiro corresponde a base e o segundo, a potência.

```c
        delta = pow(B,2) - (4*A*C);
```


Para que seja possível prosseguir com a equação, é necessário verificar se o valor resultante de delta é maior ou igual a zero, por meio da estrutura `if-else`. Em caso positivo, calcula-se, então, as duas raízes existentes, exigindo a utilização da função `sqrt()`, cujo único argumento corresponde ao valor que estará dentro da raiz quadrada. Após isto, realizamos a escrita do resultado obtido, que, de acordo com a instrução de saída [imprima o resultado das raízes com 5 dígitos após o ponto, com uma mensagem correspondente conforme exemplo abaixo.], deve conter 5 dígitos após o ponto. Isto será efetuado no texto contido na função `printf()`, através da estrutura `%.5lf`.

Em caso negativo, a condicional `else`, novamente, conterá a escrita da mensagem "Impossivel calcular".

```c
        if(delta>=0){
    			R1 = (-B +sqrt(delta)) / (2*A);
    			R2 = (-B -sqrt(delta)) / (2*A);

    			printf("R1 = %.5lf\n", R1);
    			printf("R2 = %.5lf\n", R2);
    		}

    		else
    			printf("Impossivel calcular\n");
```

##### Para revisar sobre a biblioteca math.h: [Biblioteca math.h](http://linguagemc.com.br/a-biblioteca-math-h/)
##### Para revisar sobre variáveis de ponto flutuante: [Tipos Float e Double](https://www.cprogressivo.net/2012/12/Os-tipos-float-e-double-numeros-decimais-reais-em-C.html)
##### Para revisar sobre a estrutura condicional: [If e Else](https://www.cprogressivo.net/2013/01/O-testecondicional-IF-ELSE.html)
##### Para revisar sobre formatação de saída: [Printf](https://alvinalexander.com/programming/printf-format-cheat-sheet/)


Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou envie um e-mail com o assunto "URI" para petbcc.ufscar@gmail.com
