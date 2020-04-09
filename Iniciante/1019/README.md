# Problema 

 Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica, e informe-o expresso no formato horas:minutos:segundos.

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/1019

# Resolução

Começamos nomeando nossas variáveis que serão lidas no exercício. Devemos salvar o valor inteiro em uma variável, assim como a duração do evento, que será apresentado no fim do exercício. 
Para nomear as variáveis, usaremos o tipo inteiro:

###### Modelo: tipodavariavel nomedavariavel;

	int NOME;

##### Mais sobre variáveis neste link (http://linguagemc.com.br/variaveis-em-linguagem-c/)

Para a leitura do valor que nossa variável terá, usaremos a estrutura scanf:

	scanf("%d", &NOME);

##### Mais sobre leitura de dados e a estrutura scanf neste link (http://linguagemc.com.br/operacoes-de-entrada-e-saida-de-dados-em-linguagem-c/)

Para saber quantas horas o evento teve de duração, devemos dividir o valor total pelo valor de segundos em uma hora

	horas = duracao/3600;

Porém, como sabemos que este número não será 'quebrado'?
Por isso a importância em inicializar a variável como inteira. Visto que ela é inteira, ela salvará apenas a parte inteira da divisão, descartando a parte fracionária.

##### Mais sobre o resto de uma divisão inteira neste link (http://linguagemc.com.br/resto-de-uma-divisao-inteira-em-c/)

Para os próximos, precisameros subtrair o número de horas do anterior para descartar a possibilidade que o valor inserido seja múltiplo, visto que o exercício pede a exibição de um relógio.

####Exemplo:
	Caso o valor inserido fosse 7200, podemos ter 2 horas ou 120 minutos. Visto que um relógio só mostra até 60 minutos, devemos sempre trabalhar com horas quando minutos > 60.

Com isso, devemos continuar com a divisão porém sempre subtraindo o número de horas já contabilizadas.

	minutos = (duracao - horas*3600)/60;

De forma similar, devemos subtrair o número de horas e minutos já contabilizados para saber a quantidade de segundos.

Por fim, exibiremos na tela os resultados com a estrutura printf:

###### Modelo: printf(" Texto a ser exibido / %tipodavariavel", nomedavariavel);

	printf("%d\n", valor);

##### Mais sobre escrita de dados e a estrutura printf neste link (http://linguagemc.com.br/operacoes-de-entrada-e-saida-de-dados-em-linguagem-c/)
