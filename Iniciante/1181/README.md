# Problema:
Neste problema você deve ler um número, indicando uma linha da matriz na qual uma operação deve ser realizada, um caractere maiúsculo, indicando a operação que será realizada, e todos os elementos de uma matriz M[12][12]. Em seguida, calcule e mostre a soma ou a média dos elementos que estão na área verde da matriz, conforme for o caso. A imagem abaixo ilustra o caso da entrada do valor 2 para a linha da matriz, demonstrando os elementos que deverão ser considerados na operação.
 
![Matriz](https://resources.urionlinejudge.com.br/gallery/images/problems/UOJ_1181.png)

 
##### Link do problema: https://www.urionlinejudge.com.br/judge/pt/problems/view/1181
 
 
# Resolução:
 
Começamos instanciando as variáveis necessárias, sendo elas 2 do tipo `double` (uma para a soma e outra para a matriz), um vetor de `char` (definido como `T[2]`, este vetor de char tem capacidade de armazenar 2 caracteres, contudo, o último caracter de uma string, deve ser sempre o caracter nulo “\0” que serve para indicar o final da string, ou seja, só modificaremos o `T[0]` pois o `T[1]` será o caracter nulo), e 3 inteiros (`L` que será a linha analisada e corresponde a 1ª entrada, e `x` e `y` para percorrer a matriz).
Após definir as variáveis, podemos ler as duas entradas, `L` e `T`.
 
```c
    double soma=0.0, M[12][12];
    char T[2];
    int L,x,y;
    scanf("%d", &L);
    scanf("%s", &T);
```
 
Usaremos dois `for()` aninhados para percorrer os espaços da matriz, em que o externo representa as 12 linhas e o interno, as 12 colunas.
Dentro do `for()` interno iremos fazer uma comparação para saber se estamos na linha que queremos analisar: caso seja verdadeira a expressão (`x==L`) iremos adicionar o respectivo valor à soma, até que toda a linha em questão seja percorrida.
```c
    for(x=0;x<=11;x++)
    {
        for(y=0; y<=11; y++)
        {
        scanf("%lf", &M[x][y]);
        if(x==L)
            soma+=M[x][y];
        }
    }
```
Levando em conta que o caractere maiúsculo pode somente ser 'S' ou 'M', comparamos `T[0]` à 'S', se for verdadeiro imprimimos `soma` na tela, caso contrário imprimimos o cálculo `soma/12.0` correspondente à média.

```c
    if(T[0]=='S')
        printf("%.1lf\n",soma);
    else
    {
        printf("%.1lf\n",soma/12.0);
    }
```
 
##### Para aprender um pouco mais sobre o laço de repetição for: [For](http://linguagemc.com.br/a-estrutura-de-repeticao-for-em-c/)
 
##### Para aprender um pouco mais sobre matriz: [Matriz](http://linguagemc.com.br/matriz-em-c/)
 
Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com