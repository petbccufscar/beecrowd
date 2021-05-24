# Problema 

Leia um valor inteiro correspondente à idade de uma pessoa em dias e informe-a em anos, meses e dias

Obs.: apenas para facilitar o cálculo, considere todo ano com 365 dias e todo mês com 30 dias. Nos casos de teste nunca haverá uma situação que permite 12 meses e alguns dias, como 360, 363 ou 364. Este é apenas um exercício com objetivo de testar raciocínio matemático simples.

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/1020

# Resolução

Para resolver o problema, vamos receber a idade em dias e separar em anos, meses e dias por seus respectivos valores em dias, sempre nesta ordem.

Começamos declarando nossas variáveis que serão lidas no exercício.  
Para nomear as variáveis, usaremos o tipo inteiro:

	int idade, anos, meses, dias;


Para a leitura do valor que nossa variável de idade terá, usaremos a estrutura scanf:

	scanf("%d", &idade);


Para saber quantos anos existe na quantidade de dias inserida, devemos dividir o valor total pela quantidade de dias em um ano.

	anos = idade/365;

Porém, como sabemos que este número não será 'quebrado'?
Por isso a importância em declarar a variável como inteira. Visto que ela é inteira, ela salvará apenas a parte inteira da divisão, descartando a parte fracionária.


Para os próximos, precisameros subtrair o número de anos do anterior para descartar a possibilidade que o valor inserido seja múltiplo, visto que o exercício pede a exibição em anos, meses e dias.

Com isso, devemos continuar com a divisão porém sempre subtraindo o número de anos já contabilizadas.

	meses = (idade - anos*365)/30;

De forma similar, devemos subtrair o número de anos e meses já contabilizados para saber a quantidade de dias.

Por fim, exibiremos na tela os resultados com a estrutura printf, para anos, meses e dias. Importante lembrar da estrutura da resposta e do '\n' ao lado para que pule uma linha após o valor ser escrito, visto que o URI costuma ser criterioso quanto à saída do problema:

	printf ("%d ano(s)\n", anos);


##### Mais sobre variáveis: [variáveis](http://linguagemc.com.br/variaveis-em-linguagem-c/)
##### Mais sobre leitura de dados e a estrutura scanf: [scanf](http://linguagemc.com.br/operacoes-de-entrada-e-saida-de-dados-em-linguagem-c/)
##### Mais sobre resto de uma divisão inteira: [Resto de divisão inteira](http://linguagemc.com.br/resto-de-uma-divisao-inteira-em-c/)
##### Mais sobre escrita de dados e a estrutura printf:[printf](http://linguagemc.com.br/operacoes-de-entrada-e-saida-de-dados-em-linguagem-c/)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
* [Facebook](https://www.facebook.com/petbcc/),
* [Instagram](https://www.instagram.com/petbcc.ufscar/)
* ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com

