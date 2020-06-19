# Problema:
 
Faça um programa que mostre os números pares entre 1 e 100, incluindo o 100.
 
##### Link do problema: https://www.urionlinejudge.com.br/judge/pt/problems/view/1059
 
# Resolução:

O problema não necessita de dados de entrada, portando ele consiste de um único loop que imprima os valores pares e como é possível indicar como o loop vai se comportar podemos cria-lo de forma que cada ciclo seja um número par.
 
Como não é necessário nenhuma leitura de entrada só precisamos instanciar a variável utilizada para fazer as impressões.
 
```c
        int par;
 
```
 
Para imprimir os pares utilizaremos um looping com a função `for()`.
  
Dentro do `for()` iremos imprimir os pares utilizando a própria variável do looping e seu incremento será de adicionar 2 e o valor inicial será 2, então ela sempre será par, sendo assim, iremos imprimir todos os pares de 1 a 100.
 
```c
        for (par=2; par <= 100; par = par+2){
                printf("%d\n", par);
```
Obs: Como vamos imprimir um par por linha temos que colocar o `\n` para trocarmos de linha.
 
##### Para aprender um pouco mais sobre o laço de repetição for: [For](http://linguagemc.com.br/a-estrutura-de-repeticao-for-em-c/)
 
Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC (facebook, twitter, etc).

