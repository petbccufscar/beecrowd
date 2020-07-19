# Problema

Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido da mensagem “eh o maior”. Utilize a fórmula:

MaiorAB = (a+b+abs(a-b)) / 2

Obs: a fórmula apenas calcula o maior entre os dois primeiros (a e b). Um segundo passo, portanto é necessário para chegar no resultado esperado.

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/1013

# Resolução
Neste problemas, iremos receber 3 valores do usuário e apontaremos qual é o maior, utilizando a fórmula dada no enunciado.

Utilizamos para esse problema a biblioteca `stdlib.h`, para usarmos a função [abs](http://www.w3big.com/pt/cprogramming/c-function-abs.html) que recebe um valor inteiro e retorna seu valor absoluto (positivo)

Primeiro, deve-se declarar as variáveis a serem utilizadas. Neste exercício, todas as variáveis serão inteiras. declararemos uma variável `maior` para guardar o maior de dois números. 

```c
	int a, b, c, maior;
```

Para leitura da entrada, utiliza-se a função `scanf`, que lerá os 3 valores juntos, podendo ser diferenciados por um espaço ou a tecla enter (quebra de linha)

```c
	scanf("%d %d %d", &a,&b,&c);
```

Para resolver esse problema de comparação, vamos utilizar a fórmula do exercício para comparar os números `a` e `b`.Salvamos o maior na variável `maior` e comparamos `maior` e `c` com a mesma fórmula. O resultado será salvo novamente na variável `maior`, que irá conter o maior número entre os três.

```c
	maior = (a+b+abs(a-b))/2;
    maior = (maior+c+abs(maior-c))/2;
```

Lembre-se que a função `abs` utilizada na fórmula dada pelo exercício, pertence a biblioteca `stdlib.h`, importada na segunda linha do nosso código.

Para imprimir uma saída, utilizamos a função `printf`.

```c
	printf("%d eh o maior",maior);
```

##### Para aprender um pouco mais sobre variáveis: [Variáveis](http://linguagemc.com.br/variaveis-em-linguagem-c/)

##### Para entender melhor sobre entradas e saídas: [Entrada e Saida](http://linguagemc.com.br/operacoes-de-entrada-e-saida-de-dados-em-linguagem-c/)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
