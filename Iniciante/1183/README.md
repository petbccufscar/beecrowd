# Problema:
Leia um caractere maiúsculo, que indica uma operação que deve ser realizada e uma matriz M[12][12]. Em seguida, calcule e mostre a soma ou a média considerando somente aqueles elementos que estão acima da diagonal principal da matriz, representados por `#`:
 
[ ] [#] [#] [#] [#] [#] [#] [#] [#] [#] [#] [#]
[ ] [ ] [#] [#] [#] [#] [#] [#] [#] [#] [#] [#]
[ ] [ ] [ ] [#] [#] [#] [#] [#] [#] [#] [#] [#]
[ ] [ ] [ ] [ ] [#] [#] [#] [#] [#] [#] [#] [#]
[ ] [ ] [ ] [ ] [ ] [#] [#] [#] [#] [#] [#] [#]
[ ] [ ] [ ] [ ] [ ] [ ] [#] [#] [#] [#] [#] [#]
[ ] [ ] [ ] [ ] [ ] [ ] [ ] [#] [#] [#] [#] [#]
[ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [#] [#] [#] [#]
[ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [#] [#] [#]
[ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [#] [#]
[ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [#]
[ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ]
 
##### Link do problema: https://www.urionlinejudge.com.br/judge/pt/problems/view/1183
 
 
# Resolução:
 
Começamos instanciando as variáveis necessárias, sendo elas 2 do tipo `double` (um para a soma e outro para a matriz), um vetor de `char`(definido como `T[2]` pois o último espaço de memória dele é obrigatoriamente definido como `\0`), e 5 inteiros(`coluna` para fazer as contagem por coluna, `x` e `y` para percorrer a matriz e adicionam valores, `z` para ser o valor de linha no momento da soma, e `contagem` vai ser o número de valores por coluna lidos, que será referente ao número da coluna, no caso, a coluna 0 terá 0 valores, a coluna 1 terá 1 valor e assim por diante). O valor de `contagem` começa em 1 pois não será somado valores da coluna 0.
Após definir as variáveis, podemos ler a operação (`T`).
 
```c
    double soma = 0.0, M[12][12];
    char T[2];
    int coluna, x, y, z, contagem = 1;
    scanf("%s", &T);
```
 
Vamos utilizar 2 `for()` aninhados para ler os valores de cada elemento.
 
```c
    for (x = 0; x <= 11; x++)
    {
        for (y = 0; y <= 11; y++)
            scanf("%lf", &M[x][y]);
    }
```
 
Agora utilizaremos 2 `for()` aninhados para fazer a soma dos elementos. Ao final do `for()` externo incrementamos a `contagem` para diminuir a quantidade de valores somados por linhas, como mostrado no exemplo.
 
```c
    for (z = 0; z <= 11; z++)
    {
        for (coluna = contagem; coluna <= 11; coluna++)
            soma += M[z][coluna];
        contagem++;
    }
```
Levando em conta que o caractere maiúsculo pode somente ser 'S' ou 'M', comparamos `T[0]` à 'S', se for verdadeiro imprimimos `soma` na tela, caso contrário imprimimos `soma/66.0`.
 
```c
    if (T[0] == 'S')
        printf("%.1lf\n", soma);
    else
    {
        printf("%.1lf\n", soma / 66.0);
    }
```
##### Para aprender um pouco mais sobre o laço de repetição for: [For](http://linguagemc.com.br/a-estrutura-de-repeticao-for-em-c/)
 
##### Para aprender um pouco mais sobre matriz: [Matriz](http://linguagemc.com.br/matriz-em-c/)
 
Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com