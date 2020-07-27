# Problema:
Neste problema você deve ler um número que indica uma coluna de uma matriz na qual uma operação deve ser realizada, um caractere maiúsculo, indicando a operação que será realizada, e todos os elementos de uma matriz M[12][12]. Em seguida, calcule e mostre a soma ou a média dos elementos da coluna requisitada.
Exemplo representando a coluna usando `#`:
 
[ ] [ ] [ ] [#] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ]
[ ] [ ] [ ] [#] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ]
[ ] [ ] [ ] [#] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ]
[ ] [ ] [ ] [#] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ]
[ ] [ ] [ ] [#] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ]
[ ] [ ] [ ] [#] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ]
[ ] [ ] [ ] [#] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ]
[ ] [ ] [ ] [#] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ]
[ ] [ ] [ ] [#] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ]
[ ] [ ] [ ] [#] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ]
[ ] [ ] [ ] [#] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ]
[ ] [ ] [ ] [#] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ]
 
##### Link do problema: https://www.urionlinejudge.com.br/judge/pt/problems/view/1182
 
 
# Resolução:
 
Começamos instanciando as variáveis necessárias, sendo elas 2 do tipo `double` (um para a soma e outro para a matriz), um vetor de `char`(definido como `T[2]` pois o último espaço de memória dele é obrigatoriamente definido como `\0`), e 3 inteiros(`coluna` que será analisada e `x` e `y` para percorrer a matriz).
Após definir as variáveis, podemos ler as duas entradas, `coluna` e `T`.
 
```c
    double soma = 0.0, M[12][12];
    char T[2];
    int coluna, x, y;
    scanf("%d", &coluna);
    scanf("%s", &T);
```
 
Usaremos dois `for()` aninhados para percorrer os espaços da matriz (sendo o externo para as 12 linhas e o interno para as 12 colunas).
Dentro do `for()` interno iremos fazer uma comparação para saber se estamos na coluna que queremos analisar, caso seja verdadeira a expressão (`x==coluna`) iremos adicionar o respectivo valor à soma.
```c
    for (x = 0; x <= 11; x++)
    {
        for (y = 0; y <= 11; y++)
        {
            scanf("%lf", &M[x][y]);
            if (y == coluna)
                soma += M[x][y];
        }
    }
```
Levando em conta que o caractere maiúsculo pode somente ser 'S' ou 'M', comparamos `T[0]` à 'S', se for verdadeiro imprimimos `soma` na tela, caso contrário imprimimos `soma/12.0`.
 
```c
    if (T[0] == 'S')
        printf("\n%.1lf\n", soma);
    else
    {
        printf("%.1lf\n", soma / 12.0);
    }
```
 
##### Para aprender um pouco mais sobre o laço de repetição for: [For](http://linguagemc.com.br/a-estrutura-de-repeticao-for-em-c/)
 
##### Para aprender um pouco mais sobre matriz: [Matriz](http://linguagemc.com.br/matriz-em-c/)
 
Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com