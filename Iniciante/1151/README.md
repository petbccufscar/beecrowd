# Problema:

A seguinte sequência de números 0 1 1 2 3 5 8 13 21... é conhecida como série de Fibonacci. Nessa sequência, cada número, depois dos 2 primeiros, é igual à soma dos 2 anteriores. Escreva um algoritmo que leia um inteiro N (N < 46) e mostre os N primeiros números dessa série.

##### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/1151

# Resolução:

O enunciado do problema pede um programa que mostre N números da série de Fibonacci. Sendo os primeiros números 0 e 1, os seguintes são a soma dos dois valores anteriores.

Para começar o exercício, primeiro instanciamos 5 variáveis do tipo `int`, sendo uma delas o `N` mencionado no enunciado:
```c
    int i, aux1, aux2, N, x;
```
A variável `i` será usada na estrutura `for`, `aux1` e `aux2` serão os dois valores auxiliares, usados para guardar valores anteriores da série de Fibonacci. `x` é uma variável que representa o valor atual da sequência.

Como sabemos quais são os dois primeiros valores da série, já colocaremos eles em `aux1` e `aux2`, respectivamente:
```c
    aux1 = 0;
    aux2 = 1;
```
Vamos ler a variável `N` usando `scanf`. Ela vai indicar quantos valores da sequência de Fibonacci devem ser escritos na tela:
```c
    scanf("%d", &N);
```
Para poder escrever a ordem, vamos usar uma estrutura `switch` para separar as 2 situações em que sabemos o resultado:
 ```c
     switch (N) {
 ```
O primeiro caso que sabemos o resultado é se `N` for 1, pois sabemos que o primeiro valor da série é 0, então podemos escrever a resposta com `printf` e o programa se encerra:
```c
      case 1:
        printf("0\n");
      break;
```
O segundo caso que sabemos o resultado é se `N` for 2, pois sabemos que o primeiro valor da série é 0 e o segundo é 1, então podemos escrever a resposta e terminar o programa:
```c
      case 2:
        printf("0 1\n");
      break;
```
Nos dois casos, a função `break` é usada para que o programa não continue executando o código especificado nos `case` seguintes.

O caso final é chamado de `default` e será acessado caso `N` não entre nas condições anteriores:
```c
      default:
        printf("0 1 ");
```
A primeira parte do caso final é mostrar na tela os dois primeiros valores da sequência de Fibonacci. Em seguida vamos descobrir os próximos valores da série usando a estrutura `for`:
```c
        for (i=2;i<N-1;i++) {
```
Dentro dos parênteses estão as informações iniciais do laço de repetição (`i=2`), condição de parada (`i<N-1`) e procedimento feito a cada repetição (`i++`). Dentro desse `for` descobrimos o próximo valor da sequência.

O próximo valor é a soma dos dois valores anteriores da série:
```c
          x = aux1 + aux2;
```
Como `x` não é o último valor da série que precisamos mostrar no resultado, vamos atualizar `aux1` e `aux2` para calcular o próximo valor:
```c
          aux1 = aux2;
          aux2 = x;
```
A atualização é feita sempre descartando o valor de `aux1`, que é o mais antigo, e incluindo o valor de `x` para ser usado na próxima soma. Dessa forma o valor de `aux2` passa para o `aux1` e `aux2` recebe o valor de `x`.

Por fim, escrevemos na tela o valor de `x` usando `printf` e continuamos a repetição até que reste apenas um número a ser descoberto para a resposta do exercício:
```c
          printf("%d ", x);
        }  
```
Como falta apenas um número para escrevermos os `N` números da sequência de Fibonacci, descobrimos esse novo valor e escrevemos ele na tela:
```c
        x = aux1 + aux2;
        printf("%d\n", x);
    }
```
O `\n` no fim serve para pular uma linha na tela depois de mostrar o dado. O enunciado pede que não haja espaço depois do último valor. A chave no final fecha o `switch` do início do código.
##### Para aprender um pouco mais sobre a série de Fibonacci: [Fibonacci](https://brasilescola.uol.com.br/matematica/sequencia-fibonacci.htm)
##### Para aprender um pouco mais sobre switch case: [Switch](http://linguagemc.com.br/o-comando-switch-case-em-c/)
##### Para aprender um pouco mais sobre a estrutura for: [For](http://linguagemc.com.br/a-estrutura-de-repeticao-for-em-c/)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
