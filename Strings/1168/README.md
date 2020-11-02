# Problema:

João quer montar um painel de leds contendo diversos números. Ele não possui muitos leds, e não tem certeza se conseguirá montar o número desejado. Considerando a configuração dos leds dos números abaixo, faça um algoritmo que ajude João a descobrir a quantidade de leds necessário para montar o valor.

##### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/1168

# Resolução:

Nesse exercício temos que mostrar quantos leds serão necessários para mostrar o número pedido. Cada dígito utiliza um número de leds para ser montado em um [display de 7 segmentos](https://pt.wikipedia.org/wiki/Display_de_sete_segmentos).

Vamos usar cinco variáveis, sendo uma do tipo `char` e quatro variáveis do tipo `int`:
```c
  char numero[200];
  int n, numLed, i, j;
```
`numero` é uma string que representa os dígitos do número a ser montado. `n` representa quantos números serão montados. `numLed` é a representação do número de leds pra montar o número. `i` e `j` são variáveis auxiliares para a estrutura `for`.

Para saber quantos casos de teste vão ser realizados, vamos usar um `scanf` para ler `n`:
```c
  scanf("%d", &n);
```
Sabendo quantos números serão montados, criamos um laço de repetição `for` para fazer `n` testes. Todo teste deve começar com a atribuição de `numLed` a 0 e a leitura de `numero`:
```c
  for(i = 0; i < n; i++) {
    numLed = 0;
    scanf(" %200[^\n]", numero);
```
`%200[^\n]` significa que a leitura da variável será feita até chegar a um `\n` ou até chegar a 200 caracteres. Cada caractere do vetor `numero` será um dígito de 0 a 9, então precisamos criar um `for` para verificar o número de leds usado para montar cada dígito:
```c
    for(j = 0; j < strlen(numero); j++) {
      switch (numero[j]) {
        case '0':
          numLed += 6;
          break;
        case '1':
          numLed += 2;
          break;
        case '2':
          numLed += 5;
          break;
        case '3':
          numLed += 5;
          break;
        case '4':
          numLed += 4;
          break;
        case '5':
          numLed += 5;
          break;
        case '6':
          numLed += 6;
          break;
        case '7':
          numLed += 3;
          break;
        case '8':
          numLed += 7;
          break;
        case '9':
          numLed += 6;
      }
    }
```
Aqui usamos a função `strlen` da biblioteca [string.h](http://linguagemc.com.br/a-biblioteca-string-h/) para determinar o tamanho da string `numero`. Como cada dígito usa um número específico de leds, fazemos um `switch case` para somar os leds usados ao valor de `numLed` de acordo com o dígito escrito em `numero[j]`.

Para finalizar o exercício, mostramos na tela quantos leds serão usados para montar todos os dígitos de `numero`:
```c
    printf("%d leds\n", numLed);
  }
```

##### Para aprender um pouco mais sobre vetores: [Vetores](http://linguagemc.com.br/vetores-ou-arrays-em-linguagem-c/)
##### Para aprender um pouco mais sobre a estrutura for: [For](http://linguagemc.com.br/a-estrutura-de-repeticao-for-em-c/)
##### Para aprender um pouco mais sobre o comando switch case: [Switch](http://linguagemc.com.br/o-comando-switch-case-em-c/)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
