# Problema:

Leia 5 valores Inteiros. A seguir mostre quantos valores digitados foram pares, quantos valores digitados foram ímpares, quantos valores digitados foram positivos e quantos valores digitados foram negativos.


###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/1066

# Resolução:

Uma forma de resolver o problema é utilizar 4 contadores e a cada número par, impar, positivo ou negativo, incrementar tal contador. Como sabemos a condição de término da leitura, iremos utilizar a estrutura de repetição for , para ler os 5 valores.

##### Para aprender um pouco mais sobre a estrutura de repetição FOR: [Laços](http://linguagemc.com.br/a-estrutura-de-repeticao-for-em-c/)

Para representar isto em nosso programa, fazemos: 

```c
        int contPares = 0;
        int contImpares = 0;
        int contPositivos = 0;
        int contNegativos = 0;
        int valor;
```

Ao declarar uma variável, uma posição da memória será escolhida para tal e esta posicao pode conter um valor desconhecido(lixo) já utilizado por outra aplicação. Por isso, os contadores precisam ser iniciados com zero, pois serão incrementados mais a frente. Caso não sejam icializados, essas variáveis terão um valor aleatório e provavelmente irão levar a um resultado errado.

##### Para aprender um pouco mais sobre variáveis: [Variáveis](http://linguagemc.com.br/variaveis-em-linguagem-c/)

Para ler as variáveis, usa-se scanf dentro da estrutura de repetição. Caso o valor lido seja positivo, adiciona-o à soma e incrementa o contador de números positivos em 1.

```c
        int i ; // controlador da estrutura de repetição 
        for( i = 0; i < 5; i++){
        	scanf("%d", &valor);
        	if( valor%2 == 0){
        		contPares++; //  cont++ equivale à cont = cont + 1 
                        if( valor > 0){
                                contPositivos++;
                        }else if( valor != 0){
                                contNegativos++;
                        }
        	}else{
                        contImpares++;
                        if( valor > 0){
                                contPositivos++;
                        }else if( valor != 0){
                                contNegativos++;
                        }
                }
        }
```

Em seguida, escreve-se o contador de positivos, calcula-se a media a escreve na tela utilizando a função printf:

```c
	printf("%d valor(es) par(es)\n", contPares);
        printf("%d valor(es) impar(es)\n", contImpares);
        printf("%d valor(es) positivo(s)\n", contPositivos);
        printf("%d valor(es) negativo(s)\n", contNegativos);
```

##### Para aprender um pouco mais sobre tipos de variáveis: [Tipos de Variáveis](http://linguagemc.com.br/tipos-de-dados-em-c/)

