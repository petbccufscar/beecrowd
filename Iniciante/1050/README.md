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

##### Link do problema: https://www.urionlinejudge.com.br/judge/pt/problems/view/1050


# Resolução:
Para essa resolução temos que inicialmente será passado um valor e com este, iremos verificar dentro de uma tabela, a qual cidade esse valor está atribuido ou caso não esteja deveremos informar a ausência. Para essas verificaçõs usaremos uma estrutura chamada Switch Case. \

Mas antes devemos declarar as variaveis que serão usadas, no caso apenas a que será responsavel de armazenar o valor passado no começo da execução, então faremos:
```c
int ddd;
```

Realizamos também a leitura do valor passado através da função `scanf`:
```c
scanf("%d", &ddd);		
```

Dessa forma realizamos a leitura e atribuimos o valor inserido à variavel "ddd".\
Agora usaremos a estrutura Switch Case, que será util na verificação de diversos valores, substituindo a necessidade de utilizar diversas estruturas do tipo `IF Else`\
A estrutura consiste de diversos "cases" em que podem ser definidos o que será feito caso a entrada coincida com algum dos existentes ou caso não coincida, existe a possibilidade de uma saida padrão, exemplo:
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

Aplicando isso para o caso do nosso exercicio, receberemos como variavel o ddd que foi passado, após isso é feito a verificação dentro de cada "case" para ver se coincide, caso positivo é utilizada a função `printf` indicando a qual cidade corresponde aquele valor, exemplo:
```c
switch (ddd){
	case 61:
		printf("Brasilia\n");
	break;

	...

	default:
		printf("DDD nao cadastrado\n");
}
```

Dessa forma, para quaisquer valor atribuido à variavel "ddd" caso esteja dentro de alguma das opções de nosso `Switch Case`, será realizado a exibição da cidade relacionada.\
Caso não esteja dentro das opções, será exibido "DDD não cadastrado".


##### Para mais informações sobre [Switch Case](http://linguagemc.com.br/o-comando-switch-case-em-c/)

    
“Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC (facebook, twitter, etc)”