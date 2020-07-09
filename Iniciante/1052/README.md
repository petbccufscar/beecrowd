# Problema:

Leia um valor inteiro entre 1 e 12, inclusive. Correspondente a este valor, deve ser apresentado como resposta o mês do ano por extenso, em inglês, com a primeira letra maiúscula.\
Obs: Meses em Inglês.

Exemplo:\
	Entrada: 4\
	Saida: April

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/1052

# Resolução:

Para ler o valor inteiro que será passado, antes precisamos declará-los como variáveis, para isso fazemos:
```c
        int mes;
```

Para leitura, usamos a função scanf:
```c
        scanf("%d", &mes);
```
Dessa forma realizamos a leitura e atribuimos o valor inserido à variavel "mes". 

Agora usaremos uma estrutura comum dentro da linguagem que substitui a utilização de varios "if".\
Usaremos a estrutura Switch Case

```c
	switch (variável){
		case constante1:
			Instruções;
		break;

		case constante2:
			Instruções;
		break;

		default:
			Instruções;
	}
```

A estrutura Switch atua em cima da variavel passada entre os parenteses.\
É pre-defenido alguns valores os quais se esperam que o valor contido na variavel seja igual.\
Caso for igual a algum valor, realiza-se as operaçoes contidas dentro do "case"

###### Para uma explicação mais detalhada sobre Switch Case: http://linguagemc.com.br/o-comando-switch-case-em-c/

No nosso caso, assim que entra em alguma condição do case, ja é realizado o Print indicando o mês que corresponde a aquele valor:
```c
	switch (mes){
		case 1:
			printf("January\n");
		break;

		(continua)

```

Dessa forma, para quaiquer valor atribuido à variavel "mes" caso esteja dentro de alguma das opções de nosso Switch Caso, será realizado a exibição do mês relacionado.

###### Todas as funções utlizadas estão contidas na biblioteca stdio.h, incluída na primeira linha do nosso programa.


