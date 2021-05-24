# Problema:   
Escreva um algoritmo que leia um inteiro N (0 ≤ N ≤ 100), correspondente a ordem de uma matriz M de inteiros, e construa a matriz de acordo com o exemplo abaixo.

Exemplo de Entrada | Exemplo de Saida
------------ | -------------
1 | 1
2 | 1 1 </br> 1 1
3 | 1 1 1 </br> 1 2 1 </br> 1 1 1
5 | 1 1 1 1 1 </br> 1 2 2 2 1 </br> 1 2 3 2 1 </br> 1 2 2 2 1 </br> 1 1 1 1 1

**Problema Completo**: https://www.urionlinejudge.com.br/judge/pt/problems/view/1435

# Resolução:

Para resolver este problema inicalmente iremos pensar em como de fato podemos reproduzir a maneira a qual as matrizes então se formando, dentre as intepretações possiveis iremos pensar de uma forma em que existe uma matriz de determinado tamanho e iremos prencher ela com o valor "1", após isso iremos reduzir a matriz em suas bordas, dessa forma iremos chegar em uma "matriz mais interna", a qual iremos preencher com o valor "2", assim por diante até que não tenha mais "matrizes internas". Por comparação podemos imaginar um cubo grande que vai se fechando/diminuindo até seu centro de maneira uniforme.


Pensado a lógica por trás da resolução, iniciaremos declarando algumas variaveis que serão utilizadas durante o processo, dentre elas algumas se referem sobre a matriz em si, como exemplo `tamanho`, `coluna` e `linha`. Usaremos também as variaveis que serão alteradas para delimitar os novos tamanhos das matrizes em que iremos alterar, sendo `inicioMatriz` e `fimMatriz`. Também usaremos uma variavel `elemento` para armazenar qual será o valor que iremos colocar em noss matriz mais interna a cada iteração
```c
int tamanho, coluna, linha;
int inicioMatriz, fimMatriz;
int elemento;
```


Como o problema quer que enquanto não seja inserido o valor "0" continue rodando em recebendo novos valores, iremos utilizar uma estrutura de repetição do tipo `do while` com parametro `(1)` no while, o que irá "retornar" positivo para o laço e fará com que o programa fique em "loop"
```c
do{
 ...
}while(1);
```


Para iniciar iremos receber o valor referente ao tamanho de nossa matriz, com isso ja realizamos a verificação em cima deste, caso seja "0" chamaremos a função `return 0` que será responsavel por encerrar nosso programa. Caso contrário, o valor é utilizado como parametro para a criação de nossa matriz, criando-a com o tamanho passado.
```c
scanf("%d", &tamanho);
if (tamanho == 0)
	return 0;

int m[tamanho][tamanho];
```


Definimos alguns valores iniciais para trabalharmos com a matriz que acabamos de declarar, estes baseados pelo tamanho de nossa matriz
```c
inicioMatriz = 0;
fimMatriz = tamanho;
elemento = 1;
```


Para nosso laço principal iremos percorrer a matriz, utilizando os valores contidos em `inicioMatriz` e `fimMatriz` para limitar as posições que iremos percorrer. Ao passar por cada elemento iremos atribuir o valor contido em `elemento` as posições. Ao final de cada iteração incrementamos a variavel `elemento` o que faz com que as posições mais centrais da matriz possua valores maiores em relação as posições exteriores. Reduzimos também a próxima área que iremos percorrer através das alterações dos valores contidos em `inicioMatriz` e `fimMatriz`, incrementando o primeiro e decrementando o segundo.
```c
while(fimMatriz>0){
	for (linha = inicioMatriz; linha < fimMatriz; linha++)
		for (coluna = inicioMatriz; coluna < fimMatriz; coluna++)
			m[linha][coluna] = elemento;

	inicioMatriz++;
	fimMatriz--;
	elemento++;
}
```


Ao final percorremos nossa matriz realizando a impressão dos valores seguindo a formatação proposta
```c
for (linha = 0; linha < tamanho; linha++){
	for (coluna = 0; coluna < tamanho; coluna++){
		if (coluna == 0)
			printf("%3d", m[linha][coluna]);
		else
			printf(" %3d", m[linha][coluna]);
	}

	printf("\n");
}
```


##### Para revisar sobre: [Do While](https://docs.microsoft.com/pt-br/cpp/c-language/do-while-statement-c?view=vs-2019)
    
Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com