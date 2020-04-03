# Problema

Leia dois valores inteiros, no caso para variáveis A e B. A seguir, calcule a soma entre elas e atribua à variável SOMA. A seguir escrever o valor desta variável.

# Resolução

Primeiro, devemos declarar as variáveis que usaremos, conforme o exercício nomeia.

###### Modelo: tipodavariavel nomedavariavel;

int NOME;

##### Mais sobre variáveis neste link (http://linguagemc.com.br/variaveis-em-linguagem-c/)


Como vamos ler dois valores, deveremos usar a estrutura scanf duas vezes. Visto que será inserido um valor depois outro após 
apertar enter, colocamos um scanf abaixo do outro. 
	
###### Modelo: scanf("%tipodavariavel", &nomedavariavel);

	scanf("%d", &NOME);

##### Mais sobre leitura de dados e a estrutura scanf neste link (http://linguagemc.com.br/operacoes-de-entrada-e-saida-de-dados-em-linguagem-c/)

Como lemos os valores com o scanf, as variaveis A e B já tem valor, agora daremos o valor para a variável SOMA, que será exibido no final do problema:

	SOMA = A + B;

Por fim, exibiremos na tela o resultado com a estrutura printf:

###### Modelo: printf(" Texto a ser exibido / %tipodavariavel", nomedavariavel);
	
	printf("SOMA = %d\n", SOMA);

##### Mais sobre escrita de dados e a estrutura printf neste link (http://linguagemc.com.br/operacoes-de-entrada-e-saida-de-dados-em-linguagem-c/)
