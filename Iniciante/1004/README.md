# Problema

Leia dois valores inteiros. A seguir, calcule o produto entre estes dois valores e atribua esta operação à variável PROD. A seguir mostre a variável PROD com mensagem correspondente.

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/1004

# Resolução

Primeiro, deve-se declarar as variáveis a serem utilizadas. O exercício não estipulou nomes específicos para variáveis de entrada, permitindo nomenclaturas de nossa preferência. Neste caso, usaremos "A" e "B". Porém, determinou que a variável contendo a saída (resultado final) deve ser "PROD"

###### Modelo: TipoDaVariavel NomeDaVariavel;

	int NOME;

##### Mais sobre variáveis neste link (http://linguagemc.com.br/variaveis-em-linguagem-c/)


Para leitura da entrada, utiliza-se a função scanf(). Visto que serão inseridas duas entradas, armazenadas em variáveis diferentes, a função ocorrerá duas vezes, uma logo abaixo da outra. Desse modo, após a inserção da primeira entrada, é necessário apertar a tecla enter para que, só assim, seja inserida a próxima entrada.

###### Modelo: scanf("%TipoDaVariavel", &NomeDaVariavel);

	scanf("%d", &NOME);

##### Mais sobre leitura de dados e a estrutura scanf neste link (http://linguagemc.com.br/operacoes-de-entrada-e-saida-de-dados-em-linguagem-c/)

Após a leitura, os respectivos valores encontram-se nas variáveis A e B. Então, deve-se calcular o valor a ser guardado na variável de saída PROD, equivalente a multiplicação de A e B:

	PROD = A * B;
    

Para imprimir uma saída, exibindo-a na tela, é utilizada a função printf(). Então, por fim, o resultado inserido na variável PROD deve ser impresso através da seguinte estrutura:

###### Modelo: printf("Texto a ser exibido e/ou %TipoDaVariavel", NomeDaVariavel);
	
	printf("PROD = %d\n",PROD);

##### Mais sobre escrita de dados e a estrutura printf neste link (http://linguagemc.com.br/operacoes-de-entrada-e-saida-de-dados-em-linguagem-c/)
