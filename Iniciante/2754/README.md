# Problema:

O seu professor de programação gostaria que você fizesse um programa com as seguintes características:

1. Crie duas variáveis reais de dupla precisão;
2. Atribua a primeira o valor 234.345 e a segunda o valor 45.698;
3. Imprima as duas variáveis com seis casas decimais;
4. Imprima as duas variáveis com sem nenhuma casa decimal;
5. Imprima as duas variáveis com com uma casa decimal;
6. Imprima as duas variáveis com com duas casa decimal;
7. Imprima as duas variáveis com com três casa decimal;
8. Imprima as duas variáveis com notação cientifica com 'e';
9. Imprima as duas variáveis com notação cientifica com 'E';
10. Imprima as duas variáveis com use a representação mais curta, com 'e' ou 'E' ou sem;
11. Imprima as duas variáveis com use a representação mais curta, com 'e' ou 'E' ou sem;

Para imprimir, separe os valores com um espaço em branco, um traço (-) e um espaço em branco.

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/2754

# Resolução:

O objetivo deste problema é mostrar como podemos exibir um número real de diversas formas com parâmetros do `printf`.

Para começar, criamos duas váriaveis reais do tipo `double` e iniciamos elas com os valores passados no enunciado do problema.
```c
double real1, real2;

real1 = 234.345;
real2 = 45.698;
```

Depois, começamos exibindo as variáveis com 6 casas decimais através do parâmetro `%.6lf` passado no `printf`.
```c
printf("%.6lf - %.6lf\n", real1, real2);
```

Exibimos mais 4 vezes as variáveis com 0, 1, 2 e 3 casas decimais, respectivamente. Para isso, utilizamos o parâmetro `%.Nlf` no `printf`, onde `N` representa o número de casas decimais que queremos.
```c
printf("%.0lf - %.0lf\n", real1, real2);
printf("%.1lf - %.1lf\n", real1, real2);
printf("%.2lf - %.2lf\n", real1, real2);
printf("%.3lf - %.3lf\n", real1, real2);
```

Em seguida, utilizamos os parâmetros `%e` e `%E` no `printf` para exibirmos as variáveis com notaçao cientifica 'e' e 'E', respectivamente.
```c
printf("%e - %.e\n", real1, real2);
printf("%E - %.E\n", real1, real2);
```

Por fim, utilizamos o parâmetro `%g` duas vezes no `printf` para mostrar os valores das variáveis da forma mais precisa e curta, seja ela com a notação 'e' ou 'E' ou sem nenhuma delas.
```c
printf("%g - %g\n", real1, real2);
printf("%g - %g\n", real1, real2);
```

##### Para aprender um pouco mais sobre saída de dados com `printf` : [printf](https://programacaopratica.com.br/2019/09/17/entendendo-a-funcao-printf-da-linguagem-c/)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
 * [Facebook](https://www.facebook.com/petbcc/),
 * [Instagram](https://www.instagram.com/petbcc.ufscar/)
 * ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com 