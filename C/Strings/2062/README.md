# Problema 2062:

Mariazinha criou um exercício para as suas irmãs Paula e Marta: ela distribui um texto e pede que ambas corrijam este texto, sabendo que apenas as palavras OBI e URI podem estar escritas de forma errada, e o erro pode estar apenas na última letra.

Sua tarefa aqui é automatizar este processo, ou seja, criar um programa que faça a correção dos textos distribuídos pela Mariazinha para que ela possa conferir as correções de suas irmãs sem muito trabalho.

Note que se "OB" ou "UR" forem o início ou parte de uma palavra maior, como por exemplo "OBOS" ou "URAT"), estas palavras não devem ser alteradas.

**Problema Completo**: https://www.urionlinejudge.com.br/judge/pt/problems/view/2062


# Resolução:

O exercício pede para recebermos um conjunto de palavras e corrigir apenas o erro nas palavras que possuem um total de três letras, com prefixo "OB" e "UR", colocando a letra "I" como última letra destas palavras. Em outros termos, caso estas palavras comecem com "UR" e "OB" e tenham a última letra diferente da letra "I", deve-se reescrever a palavra inserindo esta letra "I".

Para a resolução deste exercício incluímos a biblioteca `<string.h>` que contém diversas funções úteis para se trabalhar com strings.

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
```

Após a inclusão destas bibliotecas, define-se um tamanho `TAM_MAX` igual a **22** que servirá como um tamanho máximo para a variável que armazena as palavras na entrada dos dados, possuindo um tamanho máximo de 20 letras conforme especificado no enunciado. Dessa forma, considerando os caracteres `\n` e `\0` que podem aparecer no final das strings, adicionamos mais 2 unidades ao tamanho de 20 caracteres.   

```c
#define TAM_MAX 22
```

Utilizamos o vetor de caracteres `palavra[TAM_MAX]` para armazenar cada palavra presente na entrada de dados, uma variável inteira `primeiro` que determinará qual é a primeira iteração no laço de repetição e, por fim, uma variável inteira `num_palavras` que armazenará o número total de palavras a serem recebidas na entrada.

```c
int main(){

  char palavra[TAM_MAX];
  int primeiro, num_palavras;
```

Inicialmente utilizamos a função `scanf` para ler o primeiro valor da entrada, que, de acordo com o enunciado do problema, será um inteiro representando o número total de palavras que serão verificadas posteriormente. Assim, este valor é armazenado na variável `num_palavras`.

Além disso, definimos um valor inicial **1** para a variável `primeiro`, indicando que haverá a primeira iteração do laço de repetição. Isso servirá para efetuarmos a formatação correta dos dados na saída, uma vez que precisamos colocar espaço antes de cada palavra que colocamos na saída de dados, com exceção da primeira.

```c
  scanf("%d", &num_palavras);
  primeiro = 1;
```

Para ler e analisar cada palavra na entrada utiliza-se um `while` que decrementa a variável `num_palavras` enquanto esta é maior que zero. Dentro deste laço utiliza-se o `scanf` com a string de leitura `"%s"` para ler cada palavra na entrada dos dados.

Depois disso, verificamos se a variável `primeiro` tem o valor **0** (`primeiro == 0`), indicando que não é a primeira repetição do laço e, assim, pode-se colocar um espaço na saída de dados. Caso `primeiro` tenha o valor **1**, mudamos seu valor para **0**, com a finalidade de evitar que o programa entre na condição anterior nas próximas iterações do laço.

```c
  while(num_palavras > 0){
    scanf("%s", palavra);

    if(primeiro == 0){
      printf(" ");
    }
    else{
      primeiro = 0;
    }
```

Logo após isso, existem as condições principais
que servirão para determinar qual palavra deve ser corrigida ou mantida. O programa entra no primeiro `if` caso a palavra analisada contenha apenas 3 letras. Esse aspecto é verificado pela função da `strlen` da biblioteca `<string.h>`. Após isso, observa-se se os caracteres nas posições **0** e **1** do vetor `palavra` são iguais aos caracteres **'O'** e **'B'**, respectivamente. Por fim, a última condição do `if` examina se o caractere da posição **2** do vetor `palavra` difere da letra **'I'**. Caso essas quatro condições se satisfaçam simultaneamente, colocamos na saída a palavra **"OBI"** através da função `printf`.

O segundo `else if` possui condições similares ao primeiro `if`, porém difere-se verificando se as duas primeiras posições do vetor `palavra` possuem respectivamente os caracteres **'U'** e **'R'**. Dessa maneira, caso todas as suas condições se satisfaçam simultaneamente, coloca-se a palavra **"URI"** na saída de dados.

Por fim, caso o programa não entre em nenhuma das condições citadas anteriormente, repete-se a palavra analisada na saída de dados, sem nenhuma alteração. Com isso, pode-se efetuar o decremento da variável `num_palavras` no fim do `while`.

```c
    if(strlen(palavra) == 3 && palavra[0] == 'O' && palavra[1] == 'B' && palavra[2] != 'I'){
      printf("OBI");
    }
    else if(strlen(palavra) == 3 && palavra[0] == 'U' && palavra[1] == 'R' && palavra[2] != 'I'){
      printf("URI");
    }
    else{
      printf("%s", palavra);
    }

    num_palavras--;
```
Para adequarmos a saída ao que é esperado pela correção do URI, efetua-se um `printf` com o caractere de quebra de linha (`\n`) no fim do programa.

```c
  printf("\n");
  return 0;
}
```
##### Para aprender um pouco mais sobre a biblioteca string.h: [string.h](http://linguagemc.com.br/a-biblioteca-string-h/)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
