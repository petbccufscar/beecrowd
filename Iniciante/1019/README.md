# Problema 

 Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica, e informe-o expresso no formato horas:minutos:segundos.

###### [Link do problema](https://www.urionlinejudge.com.br/judge/pt/problems/view/1019)

# Resolução

Para resolver o problema, vamos receber o tempo de duração (que está em segundos) e ir localizando as horas, minutos e segundos por seus respectivos valores em segundos, nesta ordem.

Começamos declarando nossas variáveis que serão lidas no exercício. Devemos salvar o valor inteiro em uma variável, assim como a quantidade de cada célula que será apresentado no fim do exercício. 
Para declarar as variáveis, usaremos o tipo inteiro:

	int duracao, h, m, s;


Para a leitura do valor que nossa variável terá, usaremos a estrutura scanf:

	scanf("%d", &duracao);


Para saber quantas horas o evento teve de duração, devemos dividir o valor total pelo valor de segundos em uma hora

	h = duracao/3600;

Porém, como sabemos que este número não será 'quebrado'?
Por isso a importância em declarar a variável como inteira. Visto que ela é inteira, ela salvará apenas a parte inteira da divisão, descartando a parte fracionária.


Para os próximos, precisameros subtrair o número de horas do anterior para descartar a possibilidade que o valor inserido seja múltiplo, visto que o exercício pede a exibição de um relógio.

####Exemplo:
	Caso o valor inserido fosse 7200, podemos ter 2 horas ou 120 minutos. Visto que um relógio só mostra até 60 minutos, devemos sempre trabalhar com horas quando minutos > 60.

Com isso, devemos continuar com a divisão porém sempre subtraindo o número de horas já contabilizadas.

	m = (duracao - h*3600)/60;

De forma similar, devemos subtrair o número de horas e minutos já contabilizados para saber a quantidade de segundos.

Por fim, exibiremos na tela os resultados com a estrutura printf. Importante lembrar da estrutura da resposta e do '\n' ao lado para que pule uma linha após o valor ser escrito, visto que o URI costuma ser criterioso quanto à saída do problema:

	printf("%d:%d:%d\n", duracao);


##### Mais sobre [variáveis](http://linguagemc.com.br/variaveis-em-linguagem-c/), [leitura de dados e a estrutura scanf](http://linguagemc.com.br/operacoes-de-entrada-e-saida-de-dados-em-linguagem-c/), [resto de uma divisão inteira](http://linguagemc.com.br/resto-de-uma-divisao-inteira-em-c/), [escrita de dados e a estrutura printf](http://linguagemc.com.br/operacoes-de-entrada-e-saida-de-dados-em-linguagem-c/)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
* [Facebook](https://www.facebook.com/petbcc/),
* [Instagram](https://www.instagram.com/petbcc.ufscar/)
* ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com

