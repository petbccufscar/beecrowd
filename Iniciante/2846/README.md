# Problema:

A sequência de Fibonacci é uma das sequências mais famosas do mundo. Os termos de Fibonacci são sempre iguais à soma dos dois termos anteriores a eles na sequência, e os dois primeiros termos são 1. Ou seja:

1, 1, 2, 3, 5, 8, 13, 21, 34 ...

Porém, não estamos interessados em achar os termos da sequência de Fibonacci, mas sim os termos da sequência de Fibonot!

A sequência de Fibonot é composta pelos números que não pertencem à sequência de Fibonacci. Mais especificamente, os números inteiros positivos não-nulos. Em ordem crescente!

Eis os primeiros termos de Fibonot:

4, 6, 7, 9, 10, 11, 12, 14, 15 ...

Sua tarefa é achar o K-ésimo número de Fibonot.

##### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/2846

# Resolução:

Nesse exercício temos ler um valor `k` e dizer qual é o k-ésimo valor da sequência crescente de valores que não pertencem à Fibonacci.

Nesse exercício vamos declarar sete variáveis do tipo `int`:
```c
  int a, b, fibo, k, vetor[1000000], aux, i;
```
`a`, `b` e `fibo` são as variáveis usadas para calcular quais são os números da sequência de Fibonacci. `k` é a posição da sequência de Fibonot que devemos ler como resultado do algoritmo. `vetor[1000000]` é um vetor de números inteiros que vai guardar a sequência de Fibonot. `aux` e `i` são variáveis auxiliares que serão usadas no laço de repetição.

Precisamos saber qual posição da sequência devemos obter. Para isso lemos este valor usando o `scanf`:
```c
  scanf("%d", &k);
```
Agora, vamos guardar valores em `a`, `b` e `i`. Aqui preparamos as variáveis para começar a descobrir quais são os valores de Fibonot:
```c
  a = 2;
  b = 3;
  i = 0;
```
`a` e `b` começam com o terceiro(2) e quarto(3) valores da sequência de Fibonacci, pois o primeiro valor da sequência Fibonot é o número 4, que só aparece após o quarto valor de Fibonacci. O `i` vai representar a posição do vetor que vamos preencher no laço de repetição.

Para fazer o laço de repetição, usaremos um `while`. Dentro dele vamos descobrir os valores da sequência de Fibonacci e Fibonot até a k-ésima posição:
```c
  while (i <= k-1) {
    fibo = a + b;
    a = b;
    b = fibo;
```
Aqui descobrimos o próximo valor de Fibonacci. Ele será representado pela variável `fibo` e é a soma de `a` e `b`. Depois de fazer a soma, atualizamos as variáveis usadas na soma para poder descobrir o próximo número da sequência.

Agora vamos ver os valores de Fibonot. Primeiro temos que saber se há números que não são da sequência de Fibonacci entre `a` e `b`. Para isso fazemos um `if` comparando `b-a` a 1, se a subtração der um resultado maior que 1 (`b - a > 1`), começamos o processo pra descobrir os números de Fibonot:
```c
    if (b - a > 1) {
      aux = a + 1;
      while (aux < b) {
        vetor[i] = aux;
        aux++;
        i++;
      }
    }
  }
```
Os números da sequência de Fibonot estarão entre `a` e `b`. Então igualamos `aux` a `a+1` e criamos um novo laço de repetição. Dentro dele vamos inserir na posição `i` do `vetor` o valor de `aux` e incrementar os valores de `aux` e `i`. Caso `aux` seja menor que `b` (`aux < b`), repetimos o processo.  

Depois de finalizar os dois laços `while`, mostramos na tela o k-ésimo valor da sequência de Fibonot. Usamos `printf` pra isso:
```c
  printf("%d\n", vetor[k+1]);
```
Como os vetores sempre começam na posição 0, temos que subtrair 1 do valor `k` para mostrar a resposta esperada.

##### Para aprender um pouco mais sobre vetores: [Vetores](http://linguagemc.com.br/vetores-ou-arrays-em-linguagem-c/)
##### Para aprender um pouco mais sobre a estrutura while: [While](http://linguagemc.com.br/o-comando-while-em-c/)
##### Para aprender um pouco mais sobre if: [Estruturas de decisão](http://linguagemc.com.br/estrutura-de-decisao-if-em-linguagem-c/)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
