# Problema:
Começou a 4ạ Maratona de Programação da UFFS! Esperamos que você aproveite as próximas horas que passará conosco e que se divirta muito! Boa sorte!

Para aquecer você para esta competição, vamos pedir que você desenvolva um programa que calcule o quociente e o resto da divisão de dois números inteiros, pode ser? Lembre que o quociente e o resto da divisão de um inteiro a por um inteiro não-nulo b são respectivamente os únicos inteiros q e r tais que 0 ≤ r < |b| e:

a = b × q + r

Caso você não saiba, o teorema que garante a existência e a unicidade dos inteiros q e r é conhecido como ‘Teorema da Divisão Euclidiana’ ou ‘Algoritmo da Divisão’.


##### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/1837

# Resolução:

Nesse exercício temos que aplicar a fórmula `a = b × q + r` para descobrir o quociente e o resto de uma divisão. No entanto, o resto não pode ser negativo.

Nesse exercício vamos declarar quatro variáveis do tipo `int`:
```c
  int a, b, q, r;
```
Essas são as variáveis presentes na fórmula, sendo `a` o resultado da multiplicação mais o resto, `b` e `q` os multiplicadores e `r` representando o resto.

Pra começar o exercício fazemos a leitura do `a` e `b` no `scanf` para determinar os valores que temos para descobrir `q` e `r`:
```c
  scanf("%d %d", &a, &b);
```
Um único `scanf` pode ler mais de um valor se usarmos mais de um `%d`. Depois de obter esses valores vamos descobrir o valor de `r`:
```c
  r = a % b;
```
Modificando um pouco a fórmula, podemos transformar `a = b × q + r` em `a / b = q + r`. Como `q` é um número inteiro, `r` representa o resto da divisão `a / b`, esse resto pode ser obtido usando `%`. Mas como `r` deve ser positivo, temos que verificar se `r` é menor que zero e, se for, devemos tornar o valor positivo sem modificar a fórmula:
```c
  if (r < 0) {
    if (b > 0)
      r = b + r;
    else
      r = -b + r;
  }
```
Usamos um `if` para descobrir se `r` é negativo (`r < 0`) e, dentro dele, criamos outro `if` para verificar se `b` é positivo (`b > 0`). Para que a fórmula funcione, o novo `r` deve ser o valor positivo do divisor mais `r`, que é negativo (`r = b + r`).

Descobrindo `r`, podemos aplicar a fórmula como `q = (a - r) / b` para descobrir `q`. Depois disso mostramos os dois números obtidos usando `printf`:
```c
  q = (a - r) / b;
  printf("%d %d\n", q, r);
```

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
