# Problema:   
Neste problema estamos interessados na frequência das letras em uma dada linha de texto.

Especificamente, deseja-se saber qual(is) a(s) letra(s) de maior frequência do texto, ignorando o “case sensitive”, ou seja maiúsculas ou minúsculas (sendo mais claro, “letras” referem-se precisamente às 26 letras do alfabeto).

**Problema Completo**: https://www.urionlinejudge.com.br/judge/pt/problems/view/1255

# Resolução:

Para a realização deste exercício começaremos importando algumas bibliotecas dentre elas a `<string.h>` para usarmos as propriedades e funções para trabalharmos com cadeias de caracteres, e também a biblioteca `<ctype.h>` da qual iremos utilizar a função `tolower()` a qual ao ser passado um caractere maiúsculo ela nos retorna este caractere em seu formato minúsculo.
```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
```

Iremos declarar algumas variáveis que serão utilizadas durante a resolução do problema, dentre elas temos um vetor do tipo inteiro `counter` que irá armazenar em cada posição quantas vezes o caractere referente à aquela posição foi repetido, essa posição será relaciona ao caractere do alfabeto por isso possui 26 posições, para relacionarmos a posição 0 com o caractere "a" será feito nas próximas partes, variáveis `i` e `j` para utilizarmos em nossos laços de repetição, além de um vetor do tipo `char` no qual iremos armazenar o texto que será passado.
```c
int counter[26], vezes = 0, i, j;
char texto[201];

scanf("%d", &vezes);
```

Em nosso loop inicialmente declaramos uma variável `maior` essa irá armazenar o número de vezes que o caractere mais comum apareceu, além disso setamos o vetor `counter` com zeros em todas suas 26 posições. Para realizar a leitura utilizamos a função `scanf` com o parâmetro `" %[^\n]"` para que seja lidos todos os caracteres até encontrar um `\n`
```c
for (j = 0; j < vezes; j++){
    int maior = -1;
    memset(&counter, 0, 26*sizeof(int));
    scanf(" %[^\n]", texto);
```

Após lido o texto, iremos usar um laço de repetição `for`, passando cada caractere de nosso texto para a função `tolower()`, essa será responsável por tornar todos os caracteres de nosso texto em seus formatos minúsculos
```c
for(i = 0; texto[i]; i++)
	texto[i] = tolower(texto[i]);
```

Para realizar a contagem de quantas vezes determinado caractere apareceu iremos utilizar o vetor `counter` o índice será o valor na tabela ASCII de determinado caractere menos o valor 97, pois dessa forma conseguimos fazer com que o caractere "a" que possui valor 97 na tabela ASCII ocupe a posição de índice 0 de nosso vetor, o caractere "b" ocupe a posição 1 e assim por diante.
Outra forma de fazer seria usando letras maiúsculas misturadas com letras minusculas, para isso é preciso fazer uma operação OR com o caractere " " ou espaço, que possui valor 32 na tabela ASCII, assim teremos `counter[(texto[i] | ' ')-97]++;`. Essa operação OR faz com que o caractere em formato maiúsculo passe a possuir seu formato minusculo, por exemplo o caractere "A" possui valor 65 na tabela ASCII, ao fazer a operação OR com o caractere " ", que possui valor 32, iremos resultar no valor 97 que representa, na tabela ASCII o caractere "a".
```c
for (i = 0; i < strlen(texto); i++)
    counter[(texto[i]) - 97]++;
```

Após definir em cada posição do vetor `counter` quantas vezes os caracteres repetiram iremos realizar uma busca em nosso vetor para descobrir o maior valor deste, ou seja, quantas vezes o caractere mais comum apareceu
```c
for (i = 0; i < 26; i++)
    if (counter[i] > maior)
        maior = counter[i];
```

Após isso, tendo o maior valor, iteramos novamente pelo vetor `counter`, buscando por esse ou esses caracteres que mais repetiram e imprimindo estes em suas formas de caracteres e não valores inteiros. Como exemplo ao achar que o valor no índice "3" foi o que repetiu mais vezes, acrescentamos "97" a esse valor, possuindo assim o valor "100", ao atribuir esse valor à tabela ASCII iremos encontrar o caractere "d" e assim por diante.
```c
for (i = 0; i < 26; i++)
    if (counter[i] == maior)
        printf("%c", i+97);
```


##### Para revisar sobre strings: [String em C](http://linguagemc.com.br/string-em-c-vetor-de-caracteres/)
    
Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com