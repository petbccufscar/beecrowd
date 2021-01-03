# Problema 1235:    

A sua impressora foi infectada por um vírus e está imprimindo de forma incorreta. Depois de olhar para várias páginas impressas por um tempo, você percebe que ele está imprimindo cada linha de dentro para fora. Em outras palavras, a metade esquerda de cada linha está sendo impressa a partir do meio da página até a margem esquerda. Do mesmo modo, a metade direita de cada linha está sendo impressa à partir da margem direita e prosseguindo em direção ao centro da página.

Por exemplo a linha:
THIS LINE IS GIBBERISH

está sendo impressa como:
I ENIL SIHTHSIREBBIG S

Da mesma foma, a linha " MANGOS " está sendo impressa incorretamente como "NAM  SOG". Sua tarefa é desembaralhar (decifrar) a string a partir da forma como ela foi impressa para a sua forma original. Você pode assumir que cada linha conterá um número par de caracteres.

**Problema Completo**: https://www.urionlinejudge.com.br/judge/pt/problems/view/1235s


# Resolução:

O exercício pede para desembaralhar frases que são fornecidas na entrada de dados e possuem o mesmo erro em relação a organização de seus caracteres. Existem as versões incorretas de cada linha que são recebidas na entrada e as versões corretas da frase, as quais devem ser mostradas na saída de dados.

 A frase incorreta possui a primeira metade da frase correta começando do meio para a esquerda. Já a segunda metade da frase correta começa do fim da frase incorreta para o meio. Dessa maneira, por exemplo, se a frase correta for **PROGRAMAÇÃO É LEGAL**, a versão incorreta que recebemos na entrada é **ÇAMARGORPLAGEL É OÃ**.


Inicialmente, incluímos as bibliotecas padrão, a biblioteca `string.h` e estabelecemos o tamanho máximo da entrada, que é igual a **100** caracteres segundo o enunciado. Para considerar os caracteres **\n** e **\0** que podem aparecer no fim de cada linha de entrada, definimos `TAM_MAX` como **102**.

```c
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#define TAM_MAX 102
```

Utilizamos dois vetores de caracteres `linha[TAM_MAX]` e `nova_linha[TAM_MAX]`, que servirão, respectivamente, para receber a linha presente na entrada de dados e armazenar a versão correta que foi decifrada pelo programa. Também usamos duas variáveis inteiras `i` e `j` que servirão como contadores nos laços do programa, uma variável inteira `tam_linha` que armazena o tamanho da linha recebida na entrada e uma variável inteira `casos` que armazena o número de linhas a serem lidas.

```c
int main(){
  char linha[TAM_MAX], nova_linha[TAM_MAX];
  int i, j, tam_linha, casos;
```
Posteriormente, o programa lê um inteiro na entrada, que representa o número de casos a serem lidos, armazenando na variável casos. Em seguida, utiliza-se a função `getchar` para limpar o buffer de entrada de dados, eliminando um possível **\n** remanescente. Isso será útil pois o programa utilizará a função `fgets`, que consideraria este caractere **\n** como a primeira linha em sua leitura, resultando em uma string vazia.

```c
  scanf("%d", &casos);
  linha[0] = getchar();
```

Após essa leitura inicial, existe um laço `while`, no qual irá se decrementar a variável casos até que esta tenha valor 0. Dessa maneira, é possível definir uma quantidade de repetições equivalente ao valor armazenado na variável `casos`, de modo a ler cada frase na entrada.

No início do laço usamos a função `fgets` que irá ler da entrada padrão de dados `stdin` e irá armazenar seu conteúdo no vetor linhas, definindo um tamanho máximo de leitura. Assim, a função irá ler um conjunto de caracteres até encontrar um **\n** ou até um tamanho máximo definido por `TAM_MAX`. Além disso, usamos a função `strlen` para contar o tamanho da string recebida e armazenamos isso em `tam_linhas`.

```c
  while(casos > 0){
    fgets(linha, TAM_MAX, stdin);
    tam_linha = strlen(linha);
```

Como depois vamos precisar percorrer a string no sentido "do fim para o meio", precisamos desconsiderar o caractere **\n** que fica no final da string, uma vez que ele não é considerado um caractere da frase. Para isso, usamos um `if` que irá verificar se o último caractere de `linha` é igual a **\n** e irá colocar o delimitador `\0` em seu lugar. Esse delimitador é um caractere padrão usado para índicar o fim de qualquer string na linguagem C.


```c
    if(linha[tam_linha-1] == '\n'){
      linha[tam_linha-1] = '\0';
      tam_linha--;
    }
```

Para começarmos a reorganização da linha que foi recebida, devemos percorrer o vetor `linha` do meio da linha para o início. Desse modo, utlizamos um for no qual existem dois contadores `i` e `j`. O contador `i` começa com o valor da posição da metade do tamanho do vetor menos 1, pois trata-se de um índice de um vetor. Já o contador `j` começa com o valor 0.

 Assim, decrementa-se o valor de `i` até que seja menor que 0, e incrementa-se o valor de `j` até que este fique com o valor `tam_linha/2 - 1`. Dentro do laço, utilizamos o contador `j` para `nova_linha` e `i` para `linha`, de forma a armazenar a primeira metade de `linha` de maneira correta em `nova_linha`.

```c
    for(i=tam_linha/2 - 1, j=0; i >= 0; i--, j++){
      nova_linha[j] = linha[i];
    }
```

Da mesma maneira, percorremos a segunda metade de linha, só que com valores iniciais distintos para os contadores. Nesse caso, `i` começa com o valor da última posição do vetor linha e é decrementado até chegar na posição `tam_linha/2 - 1`. Já em relação ao contador `j`, aproveitamos o valor proveniente do laço anterior, que é igual a `tam_linha/2` na última iteração do laço. Com esse valor inicial, incrementamos `j` até que chegue ao valor de `tam_linha`.

```c
    for(i=tam_linha-1; i > tam_linha/2 - 1; i--, j++){
      nova_linha[j] = linha[i];
    }
```

Por fim, colocamos o caractere **\0** na última posição de `nova_palavra`, efetuamos um `printf` no conteúdo desta mesma variável e decrementamos a variável `casos` no fim do `while`.

```c
    nova_linha[j] = '\0';

    printf("%s\n", nova_linha);

    casos--;
  }
  return 0;
}
```

##### Para aprender um pouco mais sobre a biblioteca string.h: [string.h](http://linguagemc.com.br/a-biblioteca-string-h/)

##### Para aprender um pouco mais sobre a função fgets: [fgets](https://www.pucsp.br/~so-comp/cursoc/aulas/c970.html)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
