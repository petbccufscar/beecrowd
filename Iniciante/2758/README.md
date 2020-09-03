# Problema:

O seu professor gostaria de fazer um programa com as seguintes características:

    1. Crie duas variáveis para armazenar números reais de precisão simples;
    2. Crie duas variáveis para armazenar números reais de precisão dupla;
    3. Leia o primeiro número de precisão simples que sempre terá uma casa decimal;
    4. Leia o segundo número de precisão simples que sempre terá duas casas decimais;
    5. Leia o primeiro número de precisão dupla que sempre terá três casas decimais;
    6. Leia o segundo número de precisão dupla que sempre terá quatro casas decimais;
    7. Imprima a letra A, um espaço em branco, o sinal de igual, um espaço em branco, o número armazenado na primeira variável lida no passo 3, uma virgula, um espaço em branco, a letra B, um espaço em branco, o sinal de igual, um espaço em branco, o número armazenado na segunda variável lida no passo 4. Não esqueça de pular linha;
    8. Imprima a letra C, um espaço em branco, o sinal de igual, um espaço em branco, o número armazenado na primeira variável lida no passo 5, uma virgula, um espaço em branco, a letra D, um espaço em branco, o sinal de igual, um espaço em branco, o número armazenado na segunda variável lida no passo 6. Não esqueça de pular linha;
    9. Repita o procedimento 7, imprimindo os números com uma casa decimal;
    10. Repita o procedimento 8, imprimindo os números com uma casa decimal;
    11. Repita o procedimento 7, imprimindo os números com duas casas decimais;
    12. Repita o procedimento 8, imprimindo os números com duas casas decimais;
    13. Repita o procedimento 7, imprimindo os números com três casas decimais;
    14. Repita o procedimento 8, imprimindo os números com três casas decimais;
    15. Repita o procedimento 7, imprimindo os números com três casas decimais e em forma de notação cientifica com o carácter E;
    16. Repita o procedimento 8, imprimindo os números com três casas decimais e em forma de notação cientifica com o carácter E;
    17. Repita o procedimento 7, imprimindo somente a parte inteira do número;
    18. Repita o procedimento 8, imprimindo somente a parte inteira do número.

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/2758

# Resolução:
Diferente da maioria dos exercícios do URI, o enunciado passa um algoritmo. Para o exercício, vamos seguir esse algoritmo passo a passo.

Começamos declarando quatro variáveis sendo elas `a` e `b` do tipo `float` (precisão simples), e `c` e `d` do tipo `double` (precisão dupla): 
```c
  float a, b;
  double c, d;
```
Essa parte representa os passos 1 e 2 do exercício. As etapas 3 a 6 pedem a leitura de cada uma dessas variáveis. Aqui usamos a função `scanf`:
```c
  scanf("%f %f %lf %lf", &a, &b, &c, &d);
```
Perceba que usamos `%f` para `float` e `%lf` para `double`. Podemos ler mais de uma variável dentro do mesmo `scanf` ao escrever mais de um `%f` ou `%lf` entre as aspas.

O passo 7 pede para escrever os valores `a` e `b` lidos. Vamos usar o `printf`:
```c
  printf("A = %f, B = %f\n", a, b); 
```
O passo 8 pede para escrever os valores `c` e `d` lidos. Vamos usar o `printf` novamente:
```c
  printf("C = %lf, D = %lf\n", c, d);
```
As etapas 8 e 9 pedem para escrever as quatro variáveis com apenas 1 casa decimal. Vamos usar o `%.1` para escrever apenas a primeira casa decimal de cada número:
```c
  printf("A = %.1f, B = %.1f\n", a, b);
  printf("C = %.1lf, D = %.1lf\n", c, d);
```
As etapas 10 e 11 pedem para escrever as quatro variáveis com 2 casas decimais. Vamos usar o `%.2` para escrever as duas primeiras casas decimais de cada número:
```c
  printf("A = %.2f, B = %.2f\n", a, b);
  printf("C = %.2lf, D = %.2lf\n", c, d);
```
As etapas 12 e 13 pedem para escrever as quatro variáveis com 3 casas decimais. Vamos usar o `%.3` para escrever as três primeiras casas decimais de cada número:
```c
  printf("A = %.3f, B = %.3f\n", a, b);
  printf("C = %.3lf, D = %.3lf\n", c, d);
```
As etapas 14 e 15 pedem para escrever as quatro variáveis em notação científica com 3 casas decimais. Vamos usar o `%.3E` para os números aparecerem no formato `1.000E+00` em que o número depois do + representa o expoente:
```c
  printf("A = %.3E, B = %.3E\n", a, b);
  printf("C = %.3E, D = %.3E\n", c, d);
```
Os últimos passos do algoritmo pedem para escrever a parte inteira das variáveis. Para isso usamos `%.0`:
```c
  printf("A = %.0f, B = %.0f\n", a, b);
  printf("C = %.0lf, D = %.0lf\n", c, d);
```

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
* [Facebook](https://www.facebook.com/petbcc/),
* [Instagram](https://www.instagram.com/petbcc.ufscar/)
* ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com


