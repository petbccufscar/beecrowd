# Problema:

Faça um programa que leia 5 valores inteiros. Conte quantos destes valores digitados são pares e mostre esta informação.


###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/1065

# Resolução:

Uma forma de resolver o problema é utilizar um contador de números pares(`contPares`) e a cada número par lido, incrementá-lo. Como sabemos a condição de término da leitura, iremos utilizar a estrutura de repetição `for` , para ler os 5 valores.

Para representar estes valores no programa, fazemos: 

```c
        int contPares = 0;
        int valor;
```

Ao declarar uma variável, uma posição da memória será escolhida para tal e esta posição pode conter um valor desconhecido(lixo) já utilizado por outra aplicação. Por isso, `contPares` precisa ser iniciado com zero, pois será incrementado mais a frente no decorrer do código. Caso não seja inicializado, essa variável terá um valor aleatório e provavelmente irá levar a um resultado errado.

Para ler as variáveis, usa-se `scanf` dentro da estrutura de repetição `for`. Em seguida, utiliza-se a estrutura condicional `if` para verificar se o número é par: se o resto da divisão deste número por 2 for zero, ou seja, é par, incrementa-se `contPares` em 1.

```c
        int i ; // controlador da estrutura de repetição 
        for( i = 0; i < 5; i++){
            scanf("%d", &valor);
            if( valor%2 == 0){
                contPares++; 
            }
        }
```

Em seguida, escreve-se o contador de pares na tela utilizando a função `printf`:

```c
    printf("%d valores pares\n", contPares);
```

##### Para aprender um pouco mais sobre a estrutura de repetição FOR: [For](http://linguagemc.com.br/a-estrutura-de-repeticao-for-em-c/)
##### Para aprender um pouco mais sobre variáveis: [Variáveis](http://linguagemc.com.br/variaveis-em-linguagem-c/)