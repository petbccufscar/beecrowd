# Problema:

No tabuleiro de xadrez, o quadrado do tabuleiro da linha 1, coluna 1 (canto superior esquerdo) é sempre branco e as cores das casas se alternam entre o branco e o preto, seguindo o padrão conhecido como ... xadrez! Desta forma, como o tabuleiro tradicional possui oito linhas e oito colunas, a casa da linha 8, coluna 8 (canto inferior direito) também será branca. Neste problema, entretanto, queremos saber a cor do quadrado do tabuleiro no canto inferior direito de um tabuleiro com quaisquer dimensões: L linhas e C colunas. No exemplo da figura, para L = 6 e C = 9, o quadrado do tabuleiro no canto inferior direito será preto!

![Imagem_Da_Descrição](https://resources.urionlinejudge.com.br/gallery/images/problems/UOJ_2787.png)

**Input**

A primeira linha da entrada contém um inteiro L (1 ≤ L ≤ 1000) indicando o número de linhas no tabuleiro de xadrez. A segunda linha da entrada contém um inteiro C (1 ≤ C ≤ 1000) representando o número de colunas.

**Output**

Imprima uma linha na saída. A linha deve conter um inteiro, representando a cor da casa no canto inferior direito do tabuleiro: 1, se for branco; e 0, se for preto.

**Problema Completo:** https://www.urionlinejudge.com.br/judge/en/problems/view/2787

# Resolução:

Para resolver este problema, primeiramente devemos declarar as variáveis que serão utilizadas ao longo do exercício em questão. Iniciamos declarando a variável `matriz[1000][1000]` globalmente por se tratar de uma matriz muito grande, e em seguida, dentro da `int main(){}` declaramos as outras variáveis, sendo `L` e `C` o número de linhas e o número de colunas, respectivamente. E também declaramos as variáveis `i` e `j` para nos ajudar no preenchimento da matriz.

```c
#include <stdio.h>

int matriz[1000][1000];
 
int main() {

    int L,C,i,j;

    /**
     * Restante do código aqui
    **/

    return 0;
}
```

Após informarmos as variáveis que serão utilizadas no decorrer do problema, usamos o comando `scanf` para lermos os valores de `L` e `C`, que serão as linhas e colunas, da matriz.

```c
scanf("%d %d",&L,&C);
```

Em seguida, usamos um laço do tipo `for` dentro de outro laço do tipo `for` para preenchermos todos os valores da matriz, utilizando a variável `i` para percorrer as linhas, e a variável `j` para percorrer as colunas.

```c
for ( i=0; i<L; i++ ) {
    for ( j=0; j<C; j++ )
    
        /**
         * Estruturas de decisão if aqui
        **/
    
    }
}
```

Assim, resta fazer as estruturas de decisão `if` para saber em qual posição preenchemos a matriz com 0 e em qual posição preenchemos a matriz com 1. Para isto, fazemos nossa estruturação `if` da seguinte forma:

`if` para as linhas que são impares:

E dentro disto, utilizando o operador mod `%` fazemos -> Se a coluna é ímpar recebe 1, se a coluna é par recebe 0.

`else if` para as linhas que são pares:

E dentro disto, utilizando o operador mod `%` fazemos -> Se a coluna é ímpar recebe 0, se a coluna é par recebe 1.

Sendo assim, a nossa estrutura de decisão fica:

```c
if (i % 2 == 1){
    if (j % 2 == 1)
    {
    matriz[i][j] = 1 ;
    }
    else
    {
    matriz[i][j] = 0 ;
    }
}
else if (i % 2 == 0) {
    if (j % 2 == 1)
    {
    matriz[i][j] = 0 ;
    }
    else
    {
    matriz[i][j] = 1 ;
    }
}   
```

E por fim, escrevemos o nosso resultado com o comando `printf`, conforme demonstrado abaixo.

```c
printf ("%d\n",matriz[L-1][C-1]);
```

No caso, no `printf` a matriz é L-1 e C-1, pois nossa matriz vai de 0 até L-1 linhas, e de 0 até C-1 colunas.

#### Para aprender mais sobre matrizes: [http://linguagemc.com.br/arrays-com-varias-dimensoes-em-c/] [http://linguagemc.com.br/matriz-em-c/]
#### Para aprender mais sobre estruturas condicionais alinhadas: [https://www.vichinsky.com.br/Cbasico/pag13b.html] [http://linguagemc.com.br/estruturas-de-decisao-encadeadas-if-else-if-else/]
