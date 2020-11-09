# Problema:

No Instituto Federal do Sul de Minas, na cidade de Muzambinho, há um matemático realizando uma pesquisa maluca. Ele está prestes a encontrar a fórmula da juventude. Depois de vários testes ele descobriu dados que o deixaram maluco, um deles foi que: quanto mais você coda mais ele rejuvenesce. Por enquanto a fórmula está em desenvolvimento e ele te contratou para ajudá-lo na pesquisa, pois após tanto trabalho esqueceu-se de alguns princípios da matemática, como metade da tabuada, e pediu para você construir a tabuada com os números que ele precisa.

##### Link do problema: https://www.urionlinejudge.com.br/judge/pt/problems/view/2691
 
# Resolução:

O exercício consiste em ler o número de casos de teste, para cada caso de teste teremos 2 `int` que iremos imprimir a tabuada de multiplicação do 5 ao 10.

Primeiro instanciamos as variáveis necessárias, sendo elas: 5 `int` (`i` e `j` para os `loopings`; `X` e `Y` para para armazenar os números; `N`  para o número de casos de teste) e 1 `char` (para ler o caractere `x`).
Começamos lendo o número de casos de teste.

```c
    int X, Y, i, N, j;
	unsigned char vezes;
	scanf("%d", &N);
```

Utilizaremos um `for()` para passar por todos os casos de teste.

```c
    for (i = 0; i < N; i++)
    {
        \\código para cada caso individual
    }
```

Dentro dele iremos ler o caso de teste, sendo ele com 2 `int` e um `x` entre eles. Depois, utilizando um `if()` para comparar os números e descobrir se são iguais (caso sejam iguais será impresso somente uma tabuada e não duas). Tanto no `if` quanto no `else` usaremos um `for` para imprimir as linhas da tabuada levando em conta o elemento implícito na ordem, ou seja, na primeira linha sendo a multiplicação do `X` e do `Y` por 5, na segunda linha sendo a multiplicação do `X` e do `Y` por 6, e assim por diante até o 10. 
Lembrando de imprimir no formato pedido, sendo:

- `%d x %d = %d` se forem iguais
- `%d x %d = %d && %d x %d = %d` se forem diferentes

```c
    if (X == Y)
			for (j = 5; j <= 10; j++)
				printf("%d x %d = %d\n", X, j, X*j);
		else
			for (j = 5; j <= 10; j++)
				printf("%d x %d = %d && %d x %d = %d\n", X, j, X*j, Y, j, Y*j);
```

##### Para aprender um pouco mais sobre a estrutura for: [For](http://linguagemc.com.br/a-estrutura-de-repeticao-for-em-c/)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
