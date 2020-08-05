# Problema:
Leia um caractere maiúsculo, que indica uma operação que deve ser realizada e uma matriz M[12][12]. Em seguida, calcule e mostre a soma ou a média considerando somente aqueles elementos que estão abaixo da diagonal principal da matriz, conforme ilustrado abaixo (área verde).
 
![Matriz](https://resources.urionlinejudge.com.br/gallery/images/problems/UOJ_1184.png)
 
##### Link do problema: https://www.urionlinejudge.com.br/judge/pt/problems/view/1184
 
 
# Resolução:
 
Começamos instanciando as variáveis necessárias, sendo elas: 2 do tipo `double` (uma para armazenar a soma e outra, a matriz), um vetor de `char` (definido como `O[2]`, este vetor de char tem capacidade de armazenar 2 caracteres, contudo, o último caracter de uma string, deve ser sempre o caracter nulo “\0” que serve para indicar o final da string, ou seja, só modificaremos o `O[0]` pois o `O[1]` será o caracter nulo), e 5 inteiros (`coluna` para representar qual coluna está sendo acessada naquele momento; `x` e `y` para percorrer a matriz adicionando seus valores; `linha` que corresponde à linha percorrida no momento da soma; e `contagem` que garante um caminho na diagonal, pois indica em qual coluna está o 1º número dentre todos que devem ser somados na linha em questão). O valor de `contagem` começa em 0.
Após definir as variáveis, podemos ler o caractere que indica a operação (ou seja, `O`).
 
```c
    double soma = 0.0, M[12][12];
    char O[2];
    int coluna, x, y, linha, contagem = 0;
    scanf("%s", &O);
```
 
Vamos utilizar 2 `for()` aninhados para ler os valores de cada elemento da matriz.
 
```c
    for (x = 0; x <= 11; x++)
    {
        for (y = 0; y <= 11; y++)
            scanf("%lf", &M[x][y]);
    }
```
 
Agora utilizaremos 2 `for()` aninhados para fazer a soma dos elementos. Ao final do `for()` externo incrementamos a `contagem` para aumentar a quantidade de valores somados por linhas, ou seja, para cada linha iremos somar todos os elementos das colunas com índice menor do que o da linha referente, por exemplo, na linha 5 iremos somar todas as colunas com indice de 0 até 4
 
```c
    for (linha = 1; linha <= 11; linha++)
    {
        for (coluna = 0; coluna <= contagem; coluna++)
            soma += M[linha][coluna];
        contagem++;
    }
```
Levando em conta que o caractere maiúsculo pode somente ser 'S' ou 'M', comparamos `O[0]` à 'S'. Se a igualdade for verdadeira, imprimimos `soma` na tela; caso contrário imprimimos o cálculo `soma/66.0` referente à média (66 indica a quantidade de valores considerados na soma).
 
```c
    if (O[0] == 'S')
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