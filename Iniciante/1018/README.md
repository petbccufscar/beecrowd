# Problema

Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. A seguir mostre o valor lido e a relação de notas necessárias.

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/1018

# Resolução

Começamos nomeando nossas variáveis que serão lidas no exercício. Devemos salvar o valor inteiro em uma variável, assim como a quantidade de cada célula que será apresentado no fim do exercício. 
Para nomear as variáveis, usaremos o tipo inteiro:

###### Modelo: tipodavariavel nomedavariavel;

	int NOME;

##### Mais sobre variáveis neste link (http://linguagemc.com.br/variaveis-em-linguagem-c/)

Para a leitura do valor que nossa variável terá, usaremos a estrutura scanf:

	scanf("%d", &NOME);

##### Mais sobre leitura de dados e a estrutura scanf neste link (http://linguagemc.com.br/operacoes-de-entrada-e-saida-de-dados-em-linguagem-c/)

Para saber quanto de cada cédula será usava, dividimos o valor inserido pelo valor da cédula, em ordem decrescente. 
Começamos dividindo o valor inserido pela maior cédula, a de 100. 

	notas100 = valor/100;

Porém, como sabemos que o valor salvo não será 'quebrado'?
Por isso a importância em inicializar a variável como inteira. Visto que ela é inteira, ela salvará apenas a parte inteira da divisão, descartando a parte fracionária.

##### Mais sobre o resto de uma divisão inteira neste link (http://linguagemc.com.br/resto-de-uma-divisao-inteira-em-c/)

Para os próximos, precisameros subtrair o número de cédulas do anterior para descartar a possibilidade que o valor inserido seja múltiplo, visto que o exercício pede a menor quantidade de cédulas. 

####Exemplo:
	Caso o valor inserido fosse 200, podemos ter 2 cédulas de 100 ou 4 cédulas de 50. Porém, 2 de 100 são menos cédulas do que 4 de 50. 

Com isso, devemos continuar com a divisão porém sempre subtraindo o número de cédulas já utilizadas.

	notas50 = (valor - notas100*100)/50;

Por fim, exibiremos na tela os resultados com a estrutura printf:

###### Modelo: printf(" Texto a ser exibido / %tipodavariavel", nomedavariavel);

	printf("%d\n", valor);

##### Mais sobre escrita de dados e a estrutura printf neste link (http://linguagemc.com.br/operacoes-de-entrada-e-saida-de-dados-em-linguagem-c/)
