# Problema 

Leia dois valores inteiros, no caso para variáveis A e B. A seguir, calcule a soma entre elas e atribua à variável SOMA. A seguir escrever o valor desta variável.

###### [Link do problema](https://www.urionlinejudge.com.br/judge/pt/problems/view/1003)

# Resolução

Primeiro, devemos declarar as variáveis que usaremos, conforme o exercício nomeia.

	int A, B, SOMA;


Como vamos ler dois valores, deveremos usar a estrutura scanf duas vezes. Visto que será inserido um valor depois outro após 
apertar enter, colocamos um scanf abaixo do outro. 

	scanf("%d", &A);


Como lemos os valores com o scanf, as variaveis A e B já tem valor, agora daremos o valor para a variável SOMA, que será exibido no final do problema:

	SOMA = A + B;

Por fim, exibiremos na tela o resultado com a estrutura printf:

	printf("SOMA = %d\n", SOMA);


##### Mais sobre [variáveis](http://linguagemc.com.br/variaveis-em-linguagem-c/), [leitura de dados e a estrutura scanf](http://linguagemc.com.br/operacoes-de-entrada-e-saida-de-dados-em-linguagem-c/), [escrita de dados e a estrutura printf](http://linguagemc.com.br/operacoes-de-entrada-e-saida-de-dados-em-linguagem-c/).

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
* [Facebook](https://www.facebook.com/petbcc/),
* [Instagram](https://www.instagram.com/petbcc.ufscar/)
* ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com