
# Problema 2974:    

Em um porão escuro, há uma caixa de madeira com soluções impressas para todas as tarefas deste concurso. No entanto, o porão tem paredes grossas e uma porta, e uma fechadura na porta. Na fechadura existem n barras de ferro horizontais e em cada uma das barras há uma palavra com letras de igual largura. Cada barra pode ser movida independentemente para a esquerda ou direita para uma ou mais larguras de uma letra. Há pelo menos uma letra que é comum a todas as palavras. Portanto, as barras podem ser alinhadas de modo que haja uma linha vertical de n letras idênticas acima uma da outra (cada letra em uma barra). Para destrancar a porta, as barras devem ser posicionadas de tal forma que haja um número máximo de linhas verticais consecutivas.

Você está naturalmente interessado em escrever um programa que resolva esse problema.


**Problema Completo**: https://www.urionlinejudge.com.br/judge/pt/problems/view/2974


# Resolução:
O exercício em questão pede para encontrarmos a substring ou sub-palavra de maior tamanho possível que esteja presente em todas as palavra recebidas na entrada do programa.

Além das bibliotecas padrão da linguagem C, utilizamos também a biblioteca `string.h` que contém diversas funções auxiliares para lidar com strings.

```c
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
```

Utiliza-se uma definição de `MAX_PALAVRA` com valor **102** para representar o tamanho máximo de uma palavra que pode ser recebida na entrada.

```c
#define MAX_PALAVRA 102
```

Inicialmente são definidas as variáveis que serão utilizadas posteriormente no programa. As variáveis inteiras `i`, `j` e `k` são contadores que serão utilizadas em laços de repetição. As variáveis inteiras `min_tam` e `min_tam_i` representam, respectivamente, o tamanho da menor palavra recebida na entrada e o índice que representa a ordem na qual esta palavra foi recebida na entrada. A string `aux` servirá como uma variável auxiliar para armazenar as substrings de uma palavra. Os ponteiros `linha` e `linhas` servirão para armazenar uma linha de palavra e todas as linhas de palavras, respectivamente. A variável `achou` indicará se o programa encontrou ou não a substring de tamanho máximo como solução.

```c
  int n, i, j, k, min_tam_i, min_tam, achou;
  char aux[MAX_PALAVRA];
  char *linha;
  char ** linhas;
```
Após isso, efetua-se a leitura do inteiro `n` através da função `scanf` e aloca-se dinamicamente um número de ponteiros igual a este inteiro que foi lido.

```c
  scanf("%d", &n);

  linhas = malloc(sizeof(char*)*n);
```

Posteriormente, atribuímos o valor **1001** à variável `min_tam`, uma vez que utilizaremos um laço de repetição para obter a palavra com o menor tamanho no vetor `linhas`. Neste laço, alocamos dinamicamente um espaço para armazenar a palavra que será lida através da função `scanf`. Ainda no laço, existe um `if` que verifica se a palavra lida é menor que o menor tamanho armazenado até então. Caso isso se satisfaça, substituímos os valores das variáveis `min_tam` e `min_tam_i` pelos menores valores de tamanho e o índice da palavra recebidos na entrada.

```c
  min_tam = 1001;
  for(i=n-1; i >= 0; i--){
    linha = malloc(sizeof(char)*MAX_PALAVRA);
    scanf("%s", linha);
    linhas[i] = linha;
    if(strlen(linhas[i]) < min_tam){
      min_tam_i = i;
      min_tam = strlen(linhas[i]);
    }
}
```
Depois de obtermos os valores correspondentes à menor palavra, usamos 3 `for`'s aninhados para solucionar o problema. O laço mais externo servirá para variar o tamanho da substring que será procurada em todas as palavras, com o contador `i` representando esse tamanho, iniciando com o valor `min_tam` até 1.

 O laço intermediário tem a função de percorrer a palavra de menor tamanho do início ao fim "deslocando" a janela de tamanho `i` até o fim desta palavra e gerando uma substring diferente a cada iteração desse laço. A função `strncpy` copia uma parte da substring gerada para o buffer auxiliar `aux`. Esse pedaço copiado vai do endereço da posição `k` até o tamanho `i`.

No laço mais interno todas as palavras são percorridas e utiliza-se a função `strstr` para verificar se existe essa substring nas `n` palavras recebidas na entrada. Caso, em algum momento, essa substring `aux` que está sendo procurada não seja encontrada em alguma dessas `n` palavras, a função `strstr` retorna `NULL` e a flag `achou` recebe 0, fazendo com que a condição do laço seja falsa.

Caso a flag `achou` seja 1, isso significa que a solução correta foi encontrada. Dessa maneira, as condições dos laços intermediário e externo tornam-se falsas, interrompendo esses laços de repetição.

```c
  achou = 0;

  for(i=min_tam; i > 0 && achou == 0; i--){
    for(k=0; k + i <= min_tam && achou == 0; k++){
      strncpy(aux, &linhas[min_tam_i][k], i);
      aux[i] = '\0';
      achou = 1;
      for(j=0; j < n && achou == 1; j++){
        if(strstr(linhas[j], aux) == NULL){
          achou = 0;
        }
      }
    }
  }
```

Por fim, utiliza-se o `printf` para apresentar a solução na saída.

```c
  printf("%s\n", aux);
```

##### Para aprender um pouco mais sobre a biblioteca string.h: [string.h](http://linguagemc.com.br/a-biblioteca-string-h/)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
