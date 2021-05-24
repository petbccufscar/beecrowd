# Problema:
Os dados armazenados no computador estão em binário. Uma forma econômica de ver estes números é usar a base 16 (hexadecimal).

Sua tarefa consiste em escrever um programa que, dado um número natural na base 10, mostre sua representação em hexadecimal.

**Problema Completo**: https://www.urionlinejudge.com.br/judge/pt/problems/view/1957


# Resolução:
O objetivo deste exercício é bem simples: transformar um número que está 10 para a base 16. Portanto, é importante relembrarmos a correspondência destas:
Base 10 | Base 16
--------|---------
   0    |    0
   1    |    1
   2    |    2
   3    |    3
   4    |    4
   5    |    5
   6    |    6
   7    |    7
   8    |    8
   9    |    9
   10   |    A
   11   |    B
   12   |    C
   13   |    D
   14   |    E
   15   |    F
   16   |    10
   17   |    11
  ...   |    ...

Visto que a base 16 inclui caracteres (strings), é essencial a importação da biblioteca `string.h` para possibilitar seu uso. Além disso, com o intuito de instanciar uma variável sem determinar seu tamanho no momento da declaração (ou seja, trabalhar com alocação dinâmica), utilizaremos uma função inclusa na biblioteca `stdlib.h`.  

```c
#include <stdlib.h>
#include <string.h>
```  

Como primeiro passo, declaramos a variável inteira `V`, na qual será guardado, através da função `scanf()`, o número fornecido (pertencente à base 10).  

```c
int V;
scanf("%d",&V);
```  

Observando a tabela anterior, podemos notar que os valores em hexadecimal possuem apenas 16 tipos diferentes de caracteres: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E e F. Tendo esta informação em mãos, iremos declarar `digitosHexa` para armazená-los e, sabendo que todo vetor de `char` possui como último elemento o caractere especial `\0`, este possuirá tamanho 17.
Também é importante declararmos `Vhexa`, que conterá o resultado obtido; e seu índice auxiliar, o inteiro `i`. Porém, teremos conhecimento do tamanho da string gerada em hexadecimal apenas durante a execução do programa e, consequentemente, não há como alocar, com antecedência, a quantidade de memória necessária. Em cenários como este, podemos desfrutar da função `malloc` para realizar uma alocação dinâmica, sendo necessário fornecer-lhe somente o tamanho do tipo a ser utilizado (neste caso, `char`).  

```c
char digitosHexa[17] = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'};
char *Vhexa = (char*) malloc(sizeof(char));
int i = 0;
```  

Conforme estabelecido pela [conversão entre sistemas de numeração](https://www.embarcados.com.br/conversao-entre-sistemas-de-numeracao/), precisaremos realizar sucessivas divisões por 16 (guardando o resto obtido) para que, assim, sejam gerados cada um dos dígitos correspondentes ao valor hexadecimal. Desse modo, utilizaremos a estrutura `while` para que tal cálculo seja feito enquanto o número a ser dividido for superior a 0.
A cada conta realizada, usufruímos do resto da divisão (representado por `V % 16`) para indicar a posição correta no vetor `digitosHexa`. Por exemplo, caso o excedente da divisão (feita em base decimal) seja 11, iremos considerar, na verdade, o conteúdo da posição 11 de `digitosHexa`, que representa exatamente este número na base hexadecimal (ou seja, 'B'). Isto será armazenado em `Vhexa`, tendo `i` como auxílio para incrementar sua posição a cada iteração.
Em seguida, é necessário atualizar o valor de `V` como sendo `V/16`, pois já efetuamos esta divisão e, no próximo loop, necessitamos de seu quociente resultante.  

```c
while(V > 0){
  Vhexa[i] = digitosHexa[V%16];
  V = V/16;
  i = i + 1;
}
```  

Agora, basta exibirmos tudo que está armazenado em `Vhexa`. Todavia, os valores estão em ordem inversa: a primeira posição do vetor contém o último dígito do número hexadecimal gerado. Portanto, precisaremos utilizar o comando `for` para ir decrementando o valor de `i`. É importante notar que este representa a última iteração realizada anteriormente, em que `V` foi atualizado para um valor inválido (inferior a 0). Como não desejamos incluí-la na resolução, precisamos, então, decrementar a variável auxiliar em 1 e, apenas em seguida, expor os resultados com `printf()`.  

```c
i = i - 1;

for(i; i >= 0; i--){
  printf("%c", Vhexa[i]);
}
printf("\n");
```


##### Para aprender um pouco mais sobre vetores: [Arrays em linguagem C](http://linguagemc.com.br/vetores-ou-arrays-em-linguagem-c/)

##### Para aprender um pouco mais sobre strings: [Programar em C/Strings](https://pt.wikibooks.org/wiki/Programar_em_C/Strings)

##### Para aprender um pouco mais sobre alocação dinâmica: [Alocação Dinâmica em C](http://linguagemc.com.br/alocacao-dinamica-de-memoria-em-c/)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso [Facebook](https://www.facebook.com/petbcc/), [Instagram](https://www.instagram.com/petbcc.ufscar/) ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
