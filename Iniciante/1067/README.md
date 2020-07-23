# Problema: 1067
Leia um valor inteiro X (1 <= X <= 1000). Em seguida mostre os ímpares de 1 até X, um valor por linha, inclusive o X, se for o caso.


**Problema Completo**: https://www.urionlinejudge.com.br/judge/pt/problems/view/1067


# Resolução:
Para a resolução deste problema, receberemos um valor o qual usaremos como limite superior para mostrar quais são os números impares indo de 1 até esse limite.


Utilizamos uma variável inteira para armazenar o valor passado e uma variável inteira para utilizar como contador esta ira passar por todos os elementos até chegar ao valor passado
```c
int X, contador;
```

Realizamos a leitura do valor inicial que será passado, isso é feito através da função `scanf`
```c
scanf("%d",&X);
```

Para a realização do loop, iremos percorrer de 1 até o valor armazenado em `X`, para isso utilizamos um `for`, dentro deste é realizado a operação MOD, a qual verifica o valor do resto, ao verificar o resto de uma divisão de um número qualquer por 2, podemos inferir se este é ímpar ou par, caso diferente de 0 o número é ímpar. Ao entrar na condição do `if` realizamos a impressão do valor através da função `printf`
Como é requisitado que os valores impares sejam impressos um em cada linha, utilizamos o `\n` para realizar a quebra de linha
```c
for(contador = 1; contador<=X; contador++)
	if(contador%2!=0)
		printf("%d\n",contador);
```

##### Para revisar sobre operadores aritméticos: [Operadores Aritméticos](http://linguagemc.com.br/operadores-aritmeticos-em-linguagem-c/)
    
Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
