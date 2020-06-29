# Problema: 1005

Leia 2 valores de ponto flutuante de dupla precisão A e B, que correspondem a 2 notas de um aluno. A seguir, calcule a média do aluno, sabendo que a nota A tem peso 3.5 e a nota B tem peso 7.5 (A soma dos pesos portanto é 11). Assuma que cada nota pode ir de 0 até 10.0, sempre com uma casa decimal.

##### Problema Completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/1005

# Resolução

Primeiro temos que ler dois números reais que são chamados de [Float](https://www.cprogressivo.net/2012/12/Os-tipos-float-e-double-numeros-decimais-reais-em-C.html) em c:

```c
		float A, B;               
		scanf("%f%f", &A, &B);
```
Float é lido no `scanf` com a letra "f".

Temos que calcular a média considerando os pesos, podemos fazer de duas formas:

Primeira: criar uma nova variável, exemplo: 
```c
		float media;
```
E realizar o cálculo atribuindo o valor a essa variável:
```c
		media = ((A*3.5)+(B*7.5))/11;
```
Obs: Lembre de respeitar a ordem das chaves é importante para o resultado final.
Segunda: fazer o mesmo cálculo, porém na função `printf` sem usar uma terceira variável.
```c
		printf("f\n", ((A*3.5)+(B*7.5))/11);
```
A saída que ele espera tem esse formato: **MEDIA = 6.43182**.

Portanto ele espera um float com 5 casas após a vírgula e para isso fazemos:
```c
		printf("MEDIA = %.5f\n", ((A*3.5)+(B*7.5))/11);
```
Para designar o número de casas após a vírgula de um float usamos [%.nf*](https://pt.stackoverflow.com/questions/94564/como-limitar-casas-decimais) onde n é o número de casas que se quer colocar após a vírgula.  	
<<<<<<< HEAD

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para petbcc.ufscar@gmail.com

##### Para aprender um pouco mais sobre:
[Bibliotecas em c](http://linguagemc.com.br/bibliotecas/)

=======
##### Para aprender um pouco mais sobre:
[Bibliotecas em c](http://linguagemc.com.br/bibliotecas/)
>>>>>>> 753b16d... Alterado os README - 1005, 1044, 1045, 1046




