# Problema 

Leia um valor inteiro correspondente à idade de uma pessoa em dias e informe-a em anos, meses e dias

Obs.: apenas para facilitar o cálculo, considere todo ano com 365 dias e todo mês com 30 dias. Nos casos de teste nunca haverá uma situação que permite 12 meses e alguns dias, como 360, 363 ou 364. Este é apenas um exercício com objetivo de testar raciocínio matemático simples.

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/1020

# Resolução

Começamos nomeando nossas variáveis que serão lidas no exercício.  
Para nomear as variáveis, usaremos o tipo inteiro:

###### Modelo: tipodavariavel nomedavariavel;

	int NOME;

##### Mais sobre variáveis neste link (http://linguagemc.com.br/variaveis-em-linguagem-c/)

Para a leitura do valor que nossa variável de idade terá, usaremos a estrutura scanf:

	scanf("%d", &NOME);

##### Mais sobre leitura de dados e a estrutura scanf neste link (http://linguagemc.com.br/operacoes-de-entrada-e-saida-de-dados-em-linguagem-c/)

Para saber quantos anos existe na quantidade de dias inserida, devemos dividir o valor total pela quantidade de dias em um ano.

	anos = idade/365;

Porém, como sabemos que este número não será 'quebrado'?
Por isso a importância em inicializar a variável como inteira. Visto que ela é inteira, ela salvará apenas a parte inteira da divisão, descartando a parte fracionária.

##### Mais sobre o resto de uma divisão inteira neste link (http://linguagemc.com.br/resto-de-uma-divisao-inteira-em-c/)

Para os próximos, precisameros subtrair o número de anos do anterior para descartar a possibilidade que o valor inserido seja múltiplo, visto que o exercício pede a exibição em anos, meses e dias.

Com isso, devemos continuar com a divisão porém sempre subtraindo o número de anos já contabilizadas.

	meses = (idade - anos*365)/30;

De forma similar, devemos subtrair o número de anos e meses já contabilizados para saber a quantidade de dias.

Por fim, exibiremos na tela os resultados com a estrutura printf:

###### Modelo: printf(" Texto a ser exibido / %tipodavariavel", nomedavariavel);

	printf ("%d ano(s)\n", anos);

##### Mais sobre escrita de dados e a estrutura printf neste link (http://linguagemc.com.br/operacoes-de-entrada-e-saida-de-dados-em-linguagem-c/)


