# Problema:

Matheus estava conversando com a sua noiva via mensagem de texto, quando ela lhe enviou a seguinte mensagem:
```
1-4-3
```
Ele não entendeu a mensagem, então ele perguntou o que isso significava, e ela respondeu que era "I Love You" e logo ele percebeu que cada número separado por um ' - ' é a quantidade de caracteres de cada uma das palavras que compõem a frase. Com isso, ele teve a ideia de criar um programa que inserindo determinada frase, ele calcula a quantidade de caracteres de cada uma das palavras e separa os valores por ' - '. Mas ele ainda teve a ideia de que o programa deveria receber várias frases linha por linha e ainda no final da execução do programa, a palavra com a maior quantidade de letras deveria ser exibida.

##### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/2108

# Resolução:

O objetivo desse exercício é criar um programa que leia inúmeras frases até ler "0" e responda o comprimento das palavras da frase e a maior palavra encontrada.

Vamos criar iniciamente quatro variáveis, sendo duas do tipo `char` e duas do tipo `int`:
```c
  char frase[101], palavra[101];
  int maior, i;
```
`frase` é uma string que representa a frase que será enviada. `palavra` vai guardar a maior palavra encontrada nas frases. `maior` vai indicar o tamanho da maior palavra encontrada. `i` é uma variável auxiliar para a estrutura `for`.

Como nenhuma palavra foi lida, o valor de `maior` será 0:
```c
  maior = 0;
```
Como não sabemos quantas frases serão lidas, vamos usar um `do..while`. Para poder encontrar a maior palavra, temos que separar as palavras de uma frase. Para isso, criamos o vetor `lista_palavra`, que vai guardar todas as posições que contém espaço na `frase`; e uma variável `num_palavras` representando quantas palavras estão contidas em uma frase:
```c
  do {
    int lista_palavra[50], num_palavras;
```
Feito isso, podemos fazer a leitura da frase:
```c
    scanf(" %101[^\n]", frase);
```
`%101[^\n]` significa que a leitura da variável será feita até a presença de um `\n` ou até chegar a 101 caracteres. Com a `frase` lida, vamos igualar `lista_palavra[0]` a 0 e `num_palavras` a 1:
```c
    lista_palavra[0] = 0;
    num_palavras = 1;
```
Antes de descobrir quantas palavras contém `frase`, vamos verificar se ela é um caso de encerramento de programa (`frase[0] != '0'`). Se não for, criamos um laço de repetição `for` e, se `frase[i]` é um espaço branco, significa que encontramos mais uma palavra, então colocamos a posição encontrada no vetor `lista_palavra` e incrementamos `num_palavras`:
```c
    if (frase[0] != '0') {
      for(i=0;i<strlen(frase);i++) {
        if (frase[i] == ' ') {
          lista_palavra[num_palavras] = i;
          num_palavras++;
        }
      }
```
Aqui usamos a função `strlen` da biblioteca [string.h](http://linguagemc.com.br/a-biblioteca-string-h/) para determinar o tamanho da string `frase`. Depois de verificar todos os caracteres de `frase`, vamos colocar o comprimento da frase como último elemento de `lista_palavra`. Para verificar o comprimento da palavra, subtraímos `lista_palavra[1]` por `lista_palavra[0]` e, se o resultado for maior que `maior`, substituímos o valor e copiamos a palavra na string `palavra` usando a função `strncpy` da biblioteca [string.h](http://linguagemc.com.br/a-biblioteca-string-h/):
```c
      lista_palavra[num_palavras] = strlen(frase);
      
      if (lista_palavra[1] - lista_palavra[0] >= maior) {
        maior = lista_palavra[1] - lista_palavra[0];
        strncpy(palavra, frase + 0, maior);
      }
      printf("%d", lista_palavra[1] - lista_palavra[0]);
```
Sabendo o comprimento da primeira palavra, mostramos esse valor na tela usando `printf`. Em seguida, fazemos um outro laço de repetição `for` para verificar o tamanho das outras palavras da `frase`:
```c
      for(i = 2; i <= num_palavras; i++) {
        if (lista_palavra[i] - lista_palavra[i-1] - 1 >= maior) {
          maior = lista_palavra[i] - lista_palavra[i-1] - 1;
          strncpy(palavra, frase + lista_palavra[i-1]+1, maior);
        }
        printf("-%d", lista_palavra[i] - lista_palavra[i-1] - 1);
      }
      
      printf("\n");
    }
  } while (frase[0] != '0');
```
O processo para calcular o comprimento da palavra varia precisa de `- 1` para não incluir os espaços em branco que usamos como referência ao encontrar as palavras. Após cada iteração haverá um `printf` para mostrar o comprimento obtido na tela.

Depois de ler todas as frases, `frase` será igual a 0 e o `do..while` é encerrado. Ao terminar a repetição, mostramos na tela a maior palavra encontrada. No entanto, a função `strncpy` que foi usada anteriormente possui alguns bugs que copiam caracteres nulos para a variável destino (que no nosso caso é `palavra`). Para evitar esse problema, colocamos na saída de dados apenas as letras contidas em `palavra`:
```c
  i = 0;
  printf("\nThe biggest word: ");
  printf("%s", palavra);
  printf("\n");
```
Para imprimir cada caractere de `palavra`, usamos um `while` em que os caracteres da string serão mostrados na tela até `palavra[i]` não ser uma letra (A-Z ou a-z).

##### Para aprender um pouco mais sobre vetores: [Vetores](http://linguagemc.com.br/vetores-ou-arrays-em-linguagem-c/)
##### Para aprender um pouco mais sobre a estrutura do..while: [Do..while](http://linguagemc.com.br/comando-do-while/)
##### Para aprender um pouco mais sobre a estrutura for: [For](http://linguagemc.com.br/a-estrutura-de-repeticao-for-em-c/)
##### Para aprender um pouco mais sobre a estrutura while: [While](http://linguagemc.com.br/o-comando-while-em-c/)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
