# Problema

Leia 2 valores de ponto flutuante de dupla precisão A e B, que correspondem a 2 notas de um aluno. A seguir, calcule a média do aluno, sabendo que a nota A tem peso 3.5 e a nota B tem peso 7.5 (A soma dos pesos portanto é 11). Assuma que cada nota pode ir de 0 até 10.0, sempre com uma casa decimal.
[Exercício Completo 1005 - URI](https://www.urionlinejudge.com.br/judge/pt/problems/view/1005)

# Resolução

Sempre lembrar de inserir as bibliotecas que serão nescessárias para resolução do exercício, no caso as duas apontadas abaixos são tratadas como as padrões para qualquer código. 
```c
#include <stdio.h>
#include <stdlib.h>
```
Primeiro temos que ler dois números reais que são chamados de float em c:
```c
		float a,b;               
		scanf("%f%f", &a, &b);
```
Float é lido no scanf com a letra "f".

Temos que calcular a média considerando os pesos, podemos fazer de duas formas:
Primeira: criar uma nova variável, exemplo: 
```c
		float media;
```
E realizar o cálculo atribuindo o valor a essa variável:
```c
		media = ((a*3.5)+(b*7.5))/11; //Obs: Lembre de respeitar a ordem das chaves é importante para o resultado final.
```
Segundo: fazer o mesmo cálculo, porém na função printf sem usar uma terceira variável.
```c
		printf("f\n", ((a*3.5)+(b*7.5))/11);
```
A saída que ele espera tem esse formato: **MEDIA = 6.43182**.

Portanto ele espera um float com 5 casas após a vírgula e para isso fazemos:
```c
		printf("MEDIA = %.5f\n", ((a*3.5)+(b*7.5))/11);
```
Para designar o número de casas após a vírgula de um float usamos **%.nf** onde n é o número de casas que se quer colocar após a vírgula  	

##### Para aprender mais sobre manipular um float: 
[Limitar casas decimais de um float](https://pt.stackoverflow.com/questions/94564/como-limitar-casas-decimais)
[Float](https://www.cprogressivo.net/2012/12/Os-tipos-float-e-double-numeros-decimais-reais-em-C.html)


