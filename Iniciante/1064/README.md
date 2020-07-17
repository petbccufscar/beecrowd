# Problema:

Leia 6 valores. Em seguida, mostre quantos destes valores digitados foram positivos. Na próxima linha, deve-se mostrar a média de todos os valores positivos digitados, com um dígito após o ponto decimal.

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/1064

# Resolução:

Vale lembrar que a média de um conjunto de N números, é a soma de todos os N números, dividido por N.

Uma forma de resolver o problema é, conforme se realiza a leitura da entrada, caso o valor lido seja positivo, somá-lo em uma variável(`soma`) para armazenar a soma de todos os números positivos e incrementar um contador(`contPositivos`) em 1, para ao fim da leitura, calcular a média dividindo a soma pelo contador. Como sabemos a condição de término da leitura, iremos utilizar a estrutura de repetição for, para ler os 6 valores.

Para representar estes valores no programa, fazemos: 

```c
        int contPositivos = 0;
        float valor, soma = 0;
```

Ao declarar uma variável, uma posição da memória será escolhida para tal e esta posição pode conter um valor desconhecido(lixo) já utilizado por outra aplicação. Por isso, `soma` e `contPositivos` precisam ser iniciados com zero, pois serão incrementados mais a frente no decorrer do código. Caso não sejam inicializados, essas variáveis terão valores aleatórios e provavelmente irão levar a um resultado errado.


Para ler a entrada, usa-se `scanf` dentro da estrutura de repetição. Caso o valor lido seja positivo, adiciona-o à `soma` e se incrementa `contPositivos`  em 1.

```c
        int i; // controlador da estrutura de repetição 
        for( i = 0; i < 6; i++){
            scanf("%f", &valor);
            if( valor > 0){
                soma = soma + valor;
                contPositivos++;  
            }
        }
```

Em seguida, escreve-se o contador de positivos, calcula-se a media a escreve na tela utilizando a função `printf`:

```c
        printf("%d valores positivos\n", contPositivos);
        printf("%.1f\n", soma/contPositivos);
```

O '%.1f' será substituido pelo valor contido em valorTotal. O '.1' indica quantas casas decimais serão mostradas na tela, que no caso é uma.

##### Para revisar a estrutura de repetição FOR: [For](http://linguagemc.com.br/a-estrutura-de-repeticao-for-em-c/)
##### Para revisar sobre variáveis: [Variáveis](http://linguagemc.com.br/variaveis-em-linguagem-c/)


Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou envie um e-mail com o assunto "URI" para petbcc.ufscar@gmail.com
