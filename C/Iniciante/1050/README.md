# Problema: 1050

Leia um número inteiro que representa um código de DDD para discagem interurbana. Em seguida, informe à qual cidade o DDD pertence, considerando a tabela abaixo:

	61 - Brasilia
	71 - Salvador
	11 - Sao Paulo
	21 - Rio de Janeiro
	32 - Juiz de Fora
	19 - Campinas
	27 - Vitoria
	31 - Belo Horizonte
	Outro - "DDD nao cadastrado"

Se a entrada for qualquer outro DDD que não esteja presente na tabela acima, o programa deverá informar:
DDD nao cadastrado

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/1050

# Resolução:

Para ler o valor inteiro que será passado, antes precisamos declará-los como variáveis, para isso fazemos:
```c
        int ddd;
```

Para leitura, usamos a função `scanf`:
```c
        scanf("%d", &ddd);
```
Dessa forma realizamos a leitura e atribuimos o valor inserido à variavel "ddd".\
Agora usaremos uma estrutura comum dentro da linguagem que substitui a utilização de varios `if`.
Usaremos a estrutura `Switch Case`

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

A estrutura `Switch` atua em cima da variavel passada entre os parenteses.\
É pre-defenido alguns valores os quais se esperam que o valor contido na variavel seja igual.\
Caso for igual a algum valor, realiza-se as operaçoes contidas dentro do `case`

###### Para uma explicação mais detalhada sobre Switch Case: http://linguagemc.com.br/o-comando-switch-case-em-c/

No nosso caso, assim que entra em alguma condição do case, ja é realizado o `Print` indicando a cidade que corresponde a aquele valor:
```c
	switch (ddd){
		case 61:
			printf("Brasilia\n");
		break;

		(continua)

```

Dessa forma, para quaiquer valor atribuido à variavel "ddd" caso esteja dentro de alguma das opções de nosso `Switch Case`, será realizado a exibição da cidade relacionado.\
Caso não esteja dentro das opções, será exibido "DDD não cadastrado".

###### Todas as funções utlizadas estão contidas na biblioteca stdio.h, incluída na primeira linha do nosso programa.


Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para petbcc.ufscar@gmail.com