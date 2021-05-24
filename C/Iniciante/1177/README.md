# Problema

Faça um programa que leia um valor T e preencha um vetor N[1000] com a sequência de valores de 0 até T-1 repetidas vezes, conforme exemplo abaixo. Imprima o vetor N.

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/1177

# Resolução

O exercício pede então para repetirmos um sequência númerica de 0 até T-1 1000 vezes que no caso é o tamanho do vetor `N`, ficando com esse tipo de saída para `T` valendo 3:         

                                N[0] = 0
                                N[1] = 1
                                N[2] = 2
                                N[3] = 0
                                N[4] = 1
                                    .
                                    .
                                    .


Para fazermos isso precisamos iniciar nosso código declarando as variáveis que iremos utilizar ao longo do exercício, incluindo o [vetor](http://linguagemc.com.br/vetores-ou-arrays-em-linguagem-c/#:~:text=O%20vetor%20é%20uma%20estrutura,inteiro%20denominado%20índice%20do%20vetor.) que também é uma variável e precisa receber um tipo:

```c
        int T, i, aux;
        int N[1000];
```
Temos que ler o valor de `T` que para o exercício é a sequência que será repetida ao longo do vetor `N[1000]`:

```c
        scanf("%d", &T);
```
Seguimos agora para a lógica do exercício onde iremos iniciar a variável `aux` com 0, pois o exercício pede que a sequência sempre se inicie do 0, e em seguida criamos o `for` que será o responsável por rodar o `printf` que irá printar o vetor. Note que não estamos preenchendo o vetor e sim printando ele apenas na ordem pedida:

```c
        aux = 0;
        for(i = 0; i < 1000; i++)
        {
        printf("N[%d] = %d\n", i, aux);
        aux++;
        if(aux==T){
                aux=0;
        }
 
```
Dentro do `for` iremos dar o `printf` do nosso vetor seguindo a sequência desejada e para garantir isso temos a variável `aux` que será [incrementada](http://excript.com/linguagem-c/operador-incremento-decremento-c.html) a cada iteração de `i` e para garantir que `aux` não passe do valor máximo da nossa sequência tratamos ele no `if`, onde ao alcançar o valor máximo da sequência no caso ser igual a `T`, resetamos `aux` ou "mandamos de volta ao ínicio da sequência, no caso 0". Essa ação será repetida ao longo das iterações até `i` atingir o valor de 999. 


Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para petbcc.ufscar@gmail.com


