# Problema:
Como se sabe, léxico é o conjunto de palavras que existe em uma língua. Nas línguas ocidentais, é comum escrever usando o alfabeto latino, com 26 letras que vão de a até z.

É comum enumerar as letras na seguinte ordem: a, b, c, d, e f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z.

Se uma lista de palavras está organizadas de acordo com esta ordem, fica muito mais rápido pesquisá-las. Seu trabalho neste problema é ordenar duas palavras de acordo com esta ordem.

Sejam duas palavras A e B. Caso o primeiro caractere de A venha antes do primeiro de B, coloca-se A antes de B. Se o primeiro caractere for igual, usa-se o seguinte para desempate. E se o segundo empatar, usa-se o terceiro, etc. Quando todos os caracteres de A forem iguais ao começo de B, ou todos os de B forem iguais ao começo de A, coloca-se a menor palavra primeiro.

**Problema Completo**: https://www.urionlinejudge.com.br/judge/pt/problems/view/2826


# Resolução:
Para resolução deste exercício, consideraremos os valores que a [tabela ASCII](https://www.ime.usp.br/~pf/algoritmos/apend/ascii.html) associa a cada caractere.  

Tratando-se de um problema que exige a manipulação de strings, devemos incluir a biblioteca `string.h` para permitir tal feito.  

```c
#include <string.h>
```  

Declaramos, então, os vetores `firstWord` e `secondWord`, do tipo `char`, para armazenar as duas palavras da entrada, cada uma possuindo tamanho máximo igual a 20. Em seguida, realizamos a leitura das strings fornecidas através da função `scanf`.  

```c
char firstWord[20], secondWord[20];

scanf("%s",&firstWord);
scanf("%s",&secondWord);
```  

De acordo com a tabela ASCII, os valores correspondentes às 26 letras minúsculas do alfabeto relacionam-se da seguinte forma: 'a' > 'b' > 'c' > 'd' > ... > 'z'. Além disso, a biblioteca `string.h` contém uma função que compara caracteres (`strcmp`) e seu retorno corresponde a um valor:
* = 0, se o conteúdo das strings são iguais;
* < 0, se o conteúdo da 1ª string é menor do que da 2ª;
* > 0, se o conteúdo da 1ª string é maior do que da 2ª.  

Considerando tais informações, utilizamos a estrutura condicional `if` para verificar se a comparação das strings `firstWord` e `secondWord` retorna valor inferior a 0; ou seja, a 1ª palavra é menor do que a 2ª e, neste caso, será exibida primeiro. Se tal cenário não ocorrer, `else` conterá outro comando `if` em seu interior para averiguar se o contrário acontece (retorno é superior a 0) e, assim, imprimir `secondWord` primeiramente.  

```c
if(strcmp(firstWord, secondWord) < 0){
  printf("%s\n",firstWord);
	printf("%s\n",secondWord);
}

else if(strcmp(firstWord, secondWord) > 0){
  printf("%s\n",secondWord);
	printf("%s\n",firstWord);
}
```  


##### Para aprender um pouco mais sobre manipulação de strings: [A biblioteca string.h](http://linguagemc.com.br/a-biblioteca-string-h/)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso [Facebook](https://www.facebook.com/petbcc/), [Instagram](https://www.instagram.com/petbcc.ufscar/) ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
