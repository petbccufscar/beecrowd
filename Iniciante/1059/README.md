# Problema:

Faça um programa que mostre os números pares entre 1 e 100, inclusive.

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/1059

# Resolução:

Como não é necessário nenhuma leitura de entrada só precisamos instanciar a variavel utilizada para fazer as impressões.

```c
        int par;

```
##### Para aprender um pouco mais sobre variáveis: [Variáveis](http://linguagemc.com.br/variaveis-em-linguagem-c/)

Para imprimir os pares utilizaremos um looping com a função **for()**.

Lembrando a estrutura do **for**:

        for( VARIAVEL = num_inicial ; condicao_parada ; incremento_da_variavel_após_a_repetição)

Dentro do **for()** iremos imprimir os pares utilizando a própria variável do looping e seu incremento será de adicionar 2 e o valor inicial será 2, então ela sempre será par, sendo assim, iremos imprimir todos os pares de 1 a 100.

```c
	for (par=2; par <= 100; par = par+2){
		printf("%d\n", par);
```
Obs: Como vamos imprimir um par por linha temos que colocar o '\n' para trocarmos de linha.

##### Para aprender um pouco mais sobre o laço de repetição for: [For](http://linguagemc.com.br/a-estrutura-de-repeticao-for-em-c/)

###### Todas as funções utlizadas estão contidas na biblioteca stdio.h, incluída na primeira linha do nosso programa.
