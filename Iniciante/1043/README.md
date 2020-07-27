# Problema:

Leia 3 valores reais (A, B e C) e verifique se eles formam ou não um triângulo. Em caso positivo, calcule o perímetro do triângulo e apresente a mensagem:

Perimetro = XX.X

Em caso negativo, calcule a área do trapézio que tem A e B como base e C como altura, mostrando a mensagem

Area = XX.X

**Problema completo:** https://www.urionlinejudge.com.br/judge/pt/problems/view/1043

# Resolução:

Primeiramente, devemos nos atentar que os valores dados pelo exercício não são pontos, mas sim retas. Se as 3 retas conseguem fechar um triângulo, mostramos seu perímetro. Caso contrário, calculamos a área de um trapézio com estes valores.  
Para verificar se os valores/retas formam um triângulo, verificamos a [condição de existência de um triângulo](https://mundoeducacao.bol.uol.com.br/matematica/condicao-existencia-um-triangulo.htm):

```c
(A < (B + C)) &&
(B < (A + C)) &&
(C < (B + A)
```

Caso a condição seja atendida, exibimos o perímetro (soma dos lados) do triângulo. Como o enunciado pede que seja exibida apenas uma casa decimal, utilizamos `%.1f` ao invés de `%f`, sendo `.1` o número de casas após a vírgula.

```c
resultado = A + B + C;
printf("Perimetro = %.1f\n", resultado);
```

Caso contrário, as retas não fecham um triângulo e devemos exibir a área de um trapézio, considerando as bases como `A` e `B` e a altura como `C`:

```c
resultado = ((A + B) * C) / 2;
printf("Area = %.1f\n", resultado);
```

##### Para aprender mais sobre formatação de saída: [A printf format reference page](https://alvinalexander.com/programming/printf-format-cheat-sheet/)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso [Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com