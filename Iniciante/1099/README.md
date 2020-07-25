# Problema: 1099

Leia um valor inteiro N que é a quantidade de casos de teste que vem a seguir. Cada caso de teste consiste de dois inteiros X e Y. Você deve apresentar a soma de todos os ímpares existentes entre X e Y.

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/1099

# Resolução

Para resolver o exercício é bom se atentar a partes chaves como o valor inteiro N que será uma condição de parada, portanto podemos utilizar um `for` com a N sendo o limitante, outro ponto importante é a soma dos números [ímpares](https://brasilescola.uol.com.br/o-que-e/matematica/o-que-sao-numeros-pares-impares.htm). 

No exercício será utilizado 4 valores inteiros, X e Y que denota o intervalo, N o número de casos, soma assim como nome sugere a soma do intervalo de X e Y e aux que será explicado mais a frente:

```c
        int X, Y, N, soma, aux;
```

A lógica do exercício se inicia com a leitura do N, número de repetições, e a utilização dele para a construção do nosso `for`
```c
        scanf("%d", &N);

        for (int i = 0; i < N; i++) {

        }

```
A leitura de X e Y devem estar dentro do for para poder garantir que a cada loop o valor de ambos mude.
Não é tão explícito, mas o exercício espera que Y receba o maior valor na hora da leitura dos valores e para garantir isso temos que fazer a verificação usando um `if`:
```c
       
    for (int i = 0; i < N; i++) {
        
        scanf("%d %d", &X, &Y);

        if (X > Y) {
            aux = X;
            X = Y;
            Y = aux;
        }
    }

```
O `if` que verifica se Y é menor que X e irá fazer uma troca simples de variável utilizando uma variável auxiliar inteira chamada de aux.

Em seguida teremos que zerar a variável soma dentro do `for` para que cada loop ela seja resetada e com outro `for`, tendo o intervalo definido entre a diferença de X e Y, iremos fazer a soma dos números ímpares, lembrando que a característica de um número ímpar é: 2n + 1, caso tenha dúvida sobre a definição de uma olhada clicando na palavra ímpar acima. O `if` se encarregará dessa verificação comparando o [resto da divisão](http://linguagemc.com.br/resto-de-uma-divisao-inteira-em-c/) com 1.

```c
        for (int i = 0; i < N; i++) {
        
        scanf("%d %d", &X, &Y);

        if (X > Y) {
            aux = X;
            X = Y;
            Y = aux;
        }

        soma = 0;

        for (X++; X < Y; X++) {
            if (X % 2 == 1) {
                soma = soma + X;
            }
        }

        printf("%d\n", soma);
    }

```


Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para petbcc.ufscar@gmail.com

##### Para aprender um pouco mais sobre Operadores Lógicos em C:
[Operadores Lógicos em C](http://linguagemc.com.br/operadores-logicos-em-c/#:~:text=Os%20operadores%20lógicos%20são%20utilizados,condições%20simples%20em%20expressões%20lógicas.)


