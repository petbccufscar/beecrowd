# Problema

Faça um programa que leia um valor e apresente o número de Fibonacci correspondente a este valor lido. Lembre que os 2 primeiros elementos da série de Fibonacci são 0 e 1 e cada próximo termo é a soma dos 2 anteriores a ele. Todos os valores de Fibonacci calculados neste problema devem caber em um inteiro de 64 bits sem sinal.

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/1176

# Resolução

O exercício em suma será a construção da Sequência de [Fibonacci](https://pt.wikipedia.org/wiki/Sequência_de_Fibonacci), algo bem recorrente na computação, só que o foco do exercício não é printar a sequência toda e sim uma posição N desejada.

Iremos iniciar declarando as variáveis usadas no exercício, no caso desse exercício ele pede que o [vetor](http://linguagemc.com.br/vetores-ou-arrays-em-linguagem-c/#:~:text=O%20vetor%20é%20uma%20estrutura,inteiro%20denominado%20índice%20do%20vetor.) `Fib[61]` "um inteiro de 64 bits sem sinal" e para isso precisamos usar um [long long int](https://www.ime.usp.br/~yoshi/2001ii/CompI/Lista/msg00005.html)(O uso de 61 espaços se dá devido à, 0 ≤ N ≤ 60, sendo assim 0 e 60 são posições válidas) e para as outra variáveis como `i`(usado no for), `T`(número da sequência) e `N`(Posição) podemos usar `int`:

```c
        int T, N, i;
        long long int Fib[61];
```
Seguimos para a leitura da variável `T` que representa o tamanho da Sequência de Fibonacci:

```c
       scanf("%d", &T);
```
Temos que atribuir os valores as pocisões 0 e 1, devido a nescessidade desses valores no for posteriormente, sem eles não temos como iniciar a Sequência de Fibonacci:

```c
      Fib[0] = 0;
      Fib[1] = 1;      
```
Seguimos para o preenchimento do vetor `Fib[61]` com os números da Sequência de Fibonacci, lembrando que a posição de início será 2 devido ao fato explicado anteriormente, a lógica de preenchimento é o atual receber a soma dos dois anteriores a ele:

```c
      for(i = 2; i <= 60; i++)
        Fib[i] = Fib[i-1] + Fib[i-2];  
```
E finalizamos com o que foi pedido pelo exercício, que é printar um número T de casos. Para isso temos que ler a variável `T` utilizando um `scanf`. Dentro do `for` será lido a posição `N` desejada, para printar no `printf` abaixo:

```c
        scanf("%d", &T);
        for(i = 1; i<= T; i++){
                scanf("%d", &N);
                printf("Fib(%d) = %lld\n", N, Fib[N]);
        } 
```


Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para petbcc.ufscar@gmail.com

