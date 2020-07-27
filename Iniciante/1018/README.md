# Problema

Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. A seguir mostre o valor lido e a relação de notas necessárias.

##### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/1018

# Resolução

Para resolver o exercício, receberemos o valor inteiro e começaremos a contar da nota de maior valor para a de menor, sempre subtraindo a quantidade de notas que utilizarmos, para que possamos conseguir a menor quantidade de notas possível.

Começamos declarando nossas variáveis que serão utilizadas no exercício. Devemos salvar o valor inteiro em uma variável, assim como a quantidade de cada célula que será mostrado no fim do exercício. 
Visto que não existe '1 nota e meia', sempre números inteiros, usaremos o tipo inteiro tanto para receber o valor quanto para a quantidade de cada nota:


	int valor, c100, c50, c20, c10, c5, c2, c1;


Para a leitura do valor que nossa variável terá, usaremos a estrutura scanf:

	scanf("%d", &valor);


Para saber quanto de cada cédula será usava, dividimos o valor inserido pelo valor da cédula, em ordem decrescente. 
Começamos dividindo o valor inserido pela maior cédula, a de 100. 

	c100 = valor/100;

Porém, como sabemos que o valor salvo não será 'quebrado'?
Por isso a importância em declarar a variável como inteira. Visto que ela é inteira, ela salvará apenas a parte inteira da divisão, descartando a parte fracionária.


Para os próximos, precisameros subtrair o número de cédulas do anterior para descartar a possibilidade que o valor inserido seja múltiplo, visto que o exercício pede a menor quantidade de cédulas. 

#### Exemplo:
	Caso o valor inserido fosse 200, podemos ter 2 cédulas de 100 ou 4 cédulas de 50. Porém, 2 de 100 são menos cédulas do que 4 de 50. 

Com isso, devemos continuar com a divisão, sempre subtraindo o número de cédulas já utilizadas.

    c50 = (valor - c100*100)/50;

Por fim, exibiremos na tela os resultados com a estrutura printf. Importante lembrar do '\n' ao lado da estrutura em % para que pule uma linha após o valor ser escrito, visto que o URI costuma ser criterioso quanto à saída do problema:

	printf("%d\n", valor);

##### * Mais sobre variáveis: [variáveis](http://linguagemc.com.br/variaveis-em-linguagem-c/)

##### * Mais sobre leitura de dados e a estrutura scanf: [scanf](http://linguagemc.com.br/operacoes-de-entrada-e-saida-de-dados-em-linguagem-c/)

##### * Mais sobre o resto de uma divisão inteira: [Resto divisão inteira](http://linguagemc.com.br/resto-de-uma-divisao-inteira-em-c/)

##### * Mais sobre escrita de dados e a estrutura printf: [printf](http://linguagemc.com.br/operacoes-de-entrada-e-saida-de-dados-em-linguagem-c/)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
* [Facebook](https://www.facebook.com/petbcc/),
* [Instagram](https://www.instagram.com/petbcc.ufscar/)
* ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com

