# Problema:

Faça um programa que leia 5 valores inteiros. Conte quantos destes valores digitados são pares e mostre esta informação.


###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/1065

# Resolução:

Uma forma de resolver o problema é utilizar um contador e a cada número par, incrementar este contador. Como sabemos a condição de término da leitura, iremos utilizar a estrutura de repetição for , para ler os 5 valores.

##### Para aprender um pouco mais sobre a estrutura de repetição FOR: [Laços](http://linguagemc.com.br/a-estrutura-de-repeticao-for-em-c/)

Para representar isto em nosso programa, fazemos: 

```c
        int contPares = 0;
        int valor;
```

Ao declarar uma variável, uma posição da memória será escolhida para tal e esta posicao pode conter um valor desconhecido(lixo) já utilizado por outra aplicação. Por isso, contPares precisa ser iniciado com zero, pois será incrementádo mais a frente. Caso não seja inicializado, essa variável terá um valor aleatório e provavelmente irá levar a um resultado errado.

##### Para aprender um pouco mais sobre variáveis: [Variáveis](http://linguagemc.com.br/variaveis-em-linguagem-c/)

Para ler as variáveis, usa-se scanf dentro da estrutura de repetição. Caso o valor lido seja positivo, adiciona-o à soma e incrementa o contador de números positivos em 1.

```c
        int i ; // controlador da estrutura de repetição 
        for( i = 0; i < 5; i++){
        	scanf("%d", &valor);
        	if( valor%2 == 0){
        		contPares++; //  contador++ equivale à contaddor = contador + 1 
        	}
        }
```

Em seguida, escreve-se o contador de positivos, calcula-se a media a escreve na tela utilizando a função printf:

```c
	printf("%d valores pares\n", contPares);
```

##### Para aprender um pouco mais sobre tipos de variáveis: [Tipos de Variáveis](http://linguagemc.com.br/tipos-de-dados-em-c/)

