# Problema:   
Escreva um algoritmo que leia um inteiro N (0 ≤ N ≤ 100), correspondente a ordem de uma matriz M de inteiros, e construa a matriz de acordo com o exemplo abaixo.


Exemplo de Entrada | Exemplo de Saida
------------ | -------------
1 | 1
2 | 1 2 </br> 2 1
3 | 1 2 3 </br> 2 1 2 </br> 3 2 1
5 | 1 2 3 4 5 </br> 2 1 2 3 4 </br> 3 2 1 2 3 </br> 4 3 2 1 2 </br> 5 4 3 2 1


**Problema Completo**: https://www.urionlinejudge.com.br/judge/pt/problems/view/1478

# Resolução:

Iniciaremos declarando alguma variaveis, estas irão armazenar informações a respeito da matriz, como `tamanho`,`linha` e `coluna`.
```c
int tamanho, linha, coluna;
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

int matriz[tamanho][tamanho];
```

Para a definição dos valores presentes em nossa matriz, iremos utilizar algumas condições
* Caso `linha == coluna` iremos definir o valor contido como "1"
* Caso `linha < coluna` iremos definir o valor contido como "coluna - linha + 1"
* Caso `linha > coluna` iremos definir o valor contido como "linha - coluna + 1"

```c
for(linha = 0; linha < tamanho; linha++)
	for(coluna = 0; coluna < tamanho; coluna++){

		if (linha == coluna)
			matriz[linha][coluna] = 1;
		
		if (linha < coluna)
			matriz[linha][coluna] = coluna - linha + 1;
		
		if (linha > coluna)
			matriz[linha][coluna] = linha - coluna + 1;
	}
```


Ao final percorremos nossa matriz realizando a impressão dos valores seguindo a formatação proposta
```c
for (linha = 0; linha < tamanho; linha++){
	for (coluna = 0; coluna < tamanho; coluna++){
		if (coluna == 0)
			printf("%3d", matriz[linha][coluna]);
		else
			printf(" %3d", matriz[linha][coluna]);
	}

printf("\n");
}
```


##### Para revisar sobre: [Do While](https://docs.microsoft.com/pt-br/cpp/c-language/do-while-statement-c?view=vs-2019)
    
Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com