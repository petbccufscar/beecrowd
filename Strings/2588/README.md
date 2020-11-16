# Problema 2588:    
Rener era um garoto que adorava palíndromos. Tanto que inventou um jogo com estes. Dada uma sequência de letras, quantas mais teriam que ser adicionadas, pelo menos, de modo que alguma permutação desta sequência formasse um palíndromo. Por exemplo, batata precisa adicionar um b no final, para virar o palíndromo batatab. Em outro exemplo, aabb, não precisa adicionar nenhuma letra, pois se faz o palíndromo abba ou baab. Em mais um exemplo, abc precisa de duas letras a mais, para formar um palíndromo, que pode ser abcba, acbca, bacab, bcacb, cabac ou cbabc. Escreva um programa que, dada uma sequência de letras, informe qual é o mínimo de letras que precisam ser adicionadas à sequência, para que haja, pelo menos, um anagrama que forme um palíndromo.

**Problema Completo**: https://www.urionlinejudge.com.br/judge/pt/problems/view/2588


# Resolução:
O exercício pede para descobrirmos a quantidade de caracteres que devem ser adicionados de maneira que qualquer anagrama da sequência de letras na entrada se torne um [palíndromo](https://www.normaculta.com.br/palindromo-exemplos-de-palavras-e-frases/).

No início do código, é definido um tamanho máximo de valor **1002** que será usado posteriormente no tamanho vetor que armazena cada caso de teste da entrada. Apesar do enunciado apontar que o valor máximo da linha na entrada é de 1000 caracteres, colocamos **1002**, considerando os carcteres `\n` e `\0` que ficam no final da string.

```c
#define TAM_MAX 1002
```

Após isso, existe a definição da função `ordena_sequencia`, que recebe como parâmetro um endereço para a posição inicial do vetor de caracteres e efetua uma ordenação nesse mesmo vetor. O algoritmo adotado para ordenar a sequência é o Insertion Sort, com seu código adaptado a caracteres presentes no vetor `sequencia`. Esta função de ordenação servirá para compor a solução do exercício que se encontra na função `main`.

```c
void ordena_sequencia(char *sequencia){
 int i, j;
 char aux;
 for(i=0; sequencia[i+1] != '\n' && sequencia[i+1] != '\0'; i++){
   for(j=i+1; j-1 >= 0 && sequencia[j] <= sequencia[j-1]; j--){
     aux = sequencia[j];
     sequencia[j] = sequencia[j-1];
     sequencia[j-1] = aux;
   }
 }
}
```

No início da função `main`, utilizamos um vetor de caracteres com tamanho `TAM_MAX` denominado `sequencia` para armazenar cada string da entrada. Também temos 4 variáveis inteiras: `i` que servirá como contador para um laço de repetição; `par`que indicará se um par de um determinado caractere ainda precisa ser encontrado ou não; `aux` que auxiliará no armazenamento de algum caractere verificado; `caracteres_faltantes` que armazena quantos caracteres não têm seu par de caractere com mesmo valor dentro da seqûencia.

```c
  char sequencia[TAM_MAX];
  int i, par, aux, caracteres_faltantes;
```

Utilizamos a função `scanf` dentro de um laço `while`. No `scanf`, usamos o `%s` para ler cada string na entrada e armazenar na variável `sequencia`. A condição para continuar a execução do `while` verifica se o valor retornado pela função `scanf` a cada leitura difere da constante `EOF`, que possui o valor **-1** na maioria dos computadores e indica fim de arquivo, como foi solicitado pelo exercício.
```c
  while(scanf("%s", sequencia) != EOF){
```

Logo em seguida, chama-se a função `ordena_sequencia` para ordenar a string armazenada no vetor `sequencia` e as variáveis declaradas anteriormente recebem seus valores iniciais. A variável `par` começa com o valor **0** , indicando que ainda não foi encontrado nenhum caractere sem seu par correspondente. A variável `caracteres_faltantes` inicia-se com o valor **0**, já que nenhum caractere foi observado para ser contabilizado na soma dos caracteres sem seu par. Por fim, há também a variável `aux`, que recebe, inicialmente, o primeiro caractere da sequência.

Depois há um laço `for` que utiliza o contador `i` para percorrer cada posição da sequência ordenada até o final, ou seja, quando forem encontrados os caracteres `'\n'` ou `'\0'`.

```c
    for(i=0; sequencia[i] != '\n' && sequencia[i] != '\0'; i++){
```

Como a sequência está ordenada, os caracteres iguais estarão agrupados um ao lado do outro. Assim, no final do laço existem estruturas `if` e `else if` que alteram periodicamente o valor da variável par de **0** para **1** e vice-versa. Em outras palavras, quando o valor de `par` for **0**, significa que o caractere presente em `sequencia[i]` está sendo considerado como um primeiro caractere que faz parte de um novo par de caracteres iguais e adjacentes na sequência. Desta maneira adiciona-se **1** à variável `par`.

Quando o valor de `par` é igual a **1**, significa que ainda é necessário encontrar o segundo caractere do `par`. Quando este é encontrado, muda-se novamente o valor de `par` para **0**.

```c
      if(par == 1)
        par--;
      else if(par == 0)
        par++;
    }
```

No início do laço sempre é verificado através de um `if` se o caractere atual representado por `sequencia[i]` difere do caractere anterior, representado por `aux`. Caso isso seja verdade, sabemos que o programa se encontra agora em um grupo de caracteres distintos e que o valor de `par` determina se existe algum caractere "sobrando" no grupo de caracteres anterior.

Dessa maneira, atualizamos o valor de `caracteres_faltantes`, somando seu valor atual com o valor armazenado em `par` (que pode ser **0** ou **1**), voltamos o valor de `par` para **0** e atualizamos o valor da variável `aux` para `sequencia[i]`, já que agora um grupo diferente de caracteres será analisado.

```c
      if(sequencia[i] != aux){
        caracteres_faltantes += par;
        par = 0;
        aux = sequencia[i];
      }
```

Após este laço, ainda é necessário efetuar uma última soma no valor de `caracteres_faltantes`, pois essa soma, que sempre ocorre no começo de cada iteração do laço `for`, se refere ao conjunto anterior de caracteres de um mesmo valor. Esta soma final é referente ao último conjunto de caracteres na sequência ordenada.

```c
    caracteres_faltantes += par;
```

É importante destacar que, pode haver uma letra sem seu par correspondente dentro de um palíndromo, desde que ela esteja no meio deste palíndromo. Esta é a maneira de minimizar o número de caracteres que deve ser adicionado na sequência para que algum de seus anagramas se torne um palíndromo.

Com essa consideração, verificamos se o valor de `caracteres_faltantes` difere de **0** e usamos a função `printf` com `%d\n` para mostrar na saída o valor de `caracteres_faltantes-1`. No caso de
`caracteres_faltantes` ter o valor **0** , não é necessária nenhuma alteração do valor de `caracteres_faltantes` na saída, pois a sequência analisada já é um palíndromo.

```c
    if(caracteres_faltantes != 0){
      printf("%d\n", caracteres_faltantes-1);
    }
    else{
      printf("%d\n", caracteres_faltantes);
    }
  }
```

##### Para aprender um pouco mais sobre o algoritmo Insertion Sort: [Insertion Sort](https://www.geeksforgeeks.org/insertion-sort/)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
