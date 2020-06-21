# Problema: 1052    
Leia um valor inteiro entre 1 e 12, inclusive. Correspondente a este valor, deve ser apresentado como resposta o mês do ano por extenso, em inglês, com a primeira letra maiúscula.\

##### Link do problema: https://www.urionlinejudge.com.br/judge/pt/problems/view/1052


# Resolução:
Temos para esse exercicio, assim como usado no exercicio anterior (1051), a utilização da estrutura switch case, agora imprimindo o mês correspondente ao valor passado.\
Exemplo:\
	Entrada: 4\
	Saida: April

Iniciaremos declarando a variável que irá armazenar valor correspondente ao mes, para isso fazemos:
```c
        int mes;
```

Para leitura, usamos a função `scanf`:
```c
        scanf("%d", &mes);
```

Agora usaremos a estrutura `Switch Case` que substitui a utilização de varios `if`.\
Um exemplo de como é a estrutura: 
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

No nosso caso, assim que entra em alguma condição do case, ja é realizado o Print indicando o mês que corresponde a aquele valor:
```c
switch (mes){
	case 1:
		printf("January\n");
	break;

	...

	case 12:
		printf("December\n");
	break;
}	
```

Dessa forma, para quaisquer valor atribuido à variavel "mes" caso esteja dentro de alguma das opções de nosso Switch Case, será realizado a exibição do mês relacionado.


##### Para uma explicação mais detalhada sobre Switch Case: http://linguagemc.com.br/o-comando-switch-case-em-c/
    
“Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC (facebook, twitter, etc)”