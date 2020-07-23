# Problema: 1070    
Leia um valor inteiro X. Em seguida apresente os 6 valores ímpares consecutivos a partir de X, um valor por linha, inclusive o X ser for o caso.

**Problema Completo**: https://www.urionlinejudge.com.br/judge/pt/problems/view/1070


# Resolução:
Para a resolução deste problema, receberemos um valor inteiro e a partir deste iremos percorrer seus sucessores procurando pelos próximos valores ímpares

Utilizamos uma variável inteira para armazenar o valor que será passado e uma variável inteira que sérá utilizada como contador.
```c
int contador, X;
```

Realizamos a leitura do valor inicial que será passado, isso é feito através da função `scanf`.
```c
scanf("%d",&X);
```

Para resolver o problema será necessário um loop de operações, para isso utilizaremos a estrutura `while`, esta será responsavel de verificar se o valor em questão é ímpar, através da comparação `(X%2!=0)`, durante o loop iremos reutilizar a variavel `X`, que possuia inicialmente o valor passado pelo usuário, este ira armazenar a cada iteração do loop, um valor da iteração passado adicionado de 1, como é possivel ver ao final a utilização de `X++`. Para que os números impares sejam impressos um em cada linha, utilizamos o `\n` dentro da função `printf`.

```c
contador = 0;
while (contador<6){
	if(X%2!=0){
		printf("%d\n",X);
		contador++;
	}
	X++;
}
```

##### Para revisar sobre operadores aritméticos: [Operadores Aritméticos](http://linguagemc.com.br/operadores-aritmeticos-em-linguagem-c/)
    
Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
