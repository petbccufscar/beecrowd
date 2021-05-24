# Problema

Escreva um algoritmo que leia um inteiro N (0 ≤ N ≤ 15), correspondente a ordem de uma matriz M de inteiros, e construa a matriz de acordo com o exemplo abaixo. O maior desafio do exercício é exibir os valores no modelo de dígitos demonstrado.

# Resolução

Para resolver o problema, devemos ler o tamanho da matriz quadrada e formular a saída de forma que esteja no modelo exibido pelo enunciado.

O primeiro passo é declarar as variáveis que serão utilizadas no exercício. Como todos os valores são inteiros, vamos utilizar o tipo `int`.
```c
   	int N, linha, coluna, valor;
```

Um dos grandes desafios deste problema é não exceder o tempo limite. Desta forma, usaremos uma forma não convencional da estrutura `while`, para que consigamos concluir o exercício sem exceder o tempo.
Desta forma, colocaremos nossa estrutura `while` com um loop infinito (isto é, com um valor 1 que, em booleano, simboliza `TRUE` - verdadeiro). Visto que sabemos o critério de parada (a inseção de um `N == 0`), iremos terminar o programa quando este valor for lido pela estrutura `scanf`.
```c
while(1)
{
	scanf("%d", &N);

	if (N == 0)
		return 0;
```
Agora que temos o tamanho da matriz, podemos declará-la com este valor `N`.
```c
		int M[N][N];
```

Seguindo o padrão pedido pelo exercício, iremos iniciar nosso valor com 1, para que seja o primeiro valor da matriz.
```c
		valor = 1;
```

Em seguida, usaremos duas estruturas de repetição `for`. Os laços das estruturas são entrelaçados para, com cada loop de `linha`, serão feitos `N` loops de `coluna`. 
```c
		for (linha = 0; linha < N; linha++)
		{
			for (coluna = 0; coluna < N; coluna++)
			{
```

Dentro dos loops, iremos colocar os valores nas posições da matriz. Primeiro, colocamos o valor presente na variável `valor`. Em seguida, atualizamos a variável para que seja o dobro do valor que já estava salvo nela (de forma similar a `valor = valor*2`) para que, na próxima volta do loop, esta variável esteja com seu valor atualizado.
```c
				M[linha][coluna] = valor;
				valor *= 2;
```

Como a linha de baixo da matriz sempre recebe o dobro do valor da linha de cima, ao terminar o loop interno da coluna, iremos duplicar novamente todos os valores presentes na variável `valor` para que este atributo seja completo e a próxima linha seja o dobro da anterior.
```c
			valor = (M[linha][0]) * 2;
```

Seguidamente, iremos iniciar o processo para a exibição da matriz. Conforme visto na saída dos exemplos do problema, as casas decimais devem estar alinhadas em todas as colunas da matriz exibida. Para fazer isso, iremos pegar o maior valor da matriz, armazená-lo em uma variável e contar o número de dígitos, para que a saída possa ser norteada pelo maior valor presente.

Começamos declararando as variáveis que serão usadas. Ambas são inteiras, logo, do tipo `int`.
```c
		maior = (M[N - 1][N - 1]);
```

Como determinado previamente que a última linha e coluna contém o maior valor da matriz, iremos armazenar este valor na variável `maior`.
```c
		maior = (M[N - 1][N - 1]);
```

Utilizaremos a estrutura de repetição `do .. while`. A vantagem da estrutura é que podemos modificar a condição de parada antes de verificar se ela ainda é válida, fazendo com que ganhemos um loop a mais da estrutura e que ela termine no momento certo.
Dentro da estrutura, iremos realizar nosso processo de contagem de dígitos. Começamos dividindo do valor em `maior` por 10, para que resulte um dígito a menos na variável. Com isso, somamos a contagem de dígitos que a variável tem.
```c
		do
		{
			maior = maior/10;
			digitos++;
```

Esse loop continua repetindo até que o valor em `maior` seja 0, ou seja, não existam mais dígitos a contar na variável.
```c
		}while (maior > 0);
```

Agora, iremos fazer a exibição da matriz com a função `printf`. Primeiro, inicializamos duas estruturas `for` entrelaçadas com as variáveis `linha` e `coluna` como contadores.
```c
		for (linha = 0; linha < N; linha++)
		{
			for (coluna = 0; coluna < N; coluna++)
			{
```

Caso seja a primeira coluna, não há espaços para serem feitos, deixando o valor colado ao espaçamento. Usaremos `%*d`, um tipo diferente de representação para o tipo inteiro. Esta estrutura permite que o tamanho da saída seja controlado (como no exercício, pela variável `digito`). Desta forma, será exibido a quantidade de espaços do valor em `dígitos`, independentemente do valor na posição da matriz. 
```c
			if (coluna == 0)
				printf("%*d", digitos, M[linha][coluna]);
```

De forma similar, o mesmo acontece quando não estamos na primeira coluna. A diferença é o espaçamento que deve ser feito da coluna à esquerda, que é representado em `" %*d"`.
```c
			else
				printf(" %*d", digitos, M[linha][coluna]);
```

Não podemos nos esquecer de pular as linhas para exibir as próximas linhas ou, no caso de `N` não seja 0, as próximas matrizes.
```c
			printf("\n");
		}
		printf("\n");
	}
```

##### Mais sobre matrizes: [matriz](http://linguagemc.com.br/matriz-em-c/)
##### Mais sobre o uso de while(1) e loops infinitos: [while(1)](http://linguagemc.com.br/loop-infinito-em-c/)
##### Mais sobre a estrutura utilizada no último print, em inglês: [%d](https://stackoverflow.com/questions/9937052/what-is-the-difference-between-d-and-d-in-c-language)
##### Mais sobre a estrutura do .. while: [do while](http://linguagemc.com.br/comando-do-while/)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
* [Facebook](https://www.facebook.com/petbcc/),
* [Instagram](https://www.instagram.com/petbcc.ufscar/)
* ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com

