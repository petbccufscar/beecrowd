# Problema

O arquivo de entrada contém dois valores: um valor inteiro X representando a distância total percorrida (em Km), e um valor real Y representando o total de combustível gasto, com um dígito após o ponto decimal.

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/1014

# Resolução

Primeiro, deve-se declarar as variáveis a serem utilizadas. Neste exercício, teremos uma variável inteira (km) e duas do tipo ponto flutuante
uma para armazenar o combustível gasto e outra para armazenar o resultado da divisão entre essas duas.

###### Modelo: TipoDaVariavel NomeDaVariavel;

	int km;
    float combustivel, km_l;

##### Mais sobre variáveis neste link (http://linguagemc.com.br/variaveis-em-linguagem-c/)

## Entrada

Para leitura da entrada, utiliza-se a função scanf(), que lerá os 2 valores juntos, podendo ser diferenciados na entrada por um espaço ou a tecla enter (quebra de linha)

###### Modelo: scanf("%TipoDaVariavel", &NomeDaVariavel);

	scanf("%d %f", &km, &combustivel);

##### Mais sobre leitura de dados e a estrutura scanf neste link (http://linguagemc.com.br/operacoes-de-entrada-e-saida-de-dados-em-linguagem-c/)

Para resolver esse problema, devemos apenas efetuar uma simples divisão entre as duas variaveis para obter a media de km/l da viagem.
## Saída

Para imprimir uma saída, exibindo-a na tela, é utilizada a função printf().
###### Modelo: printf("Texto a ser exibido e/ou %TipoDaVariavel", NomeDaVariavel);
	
	printf("%.3f km/l\n",km_l);

Aqui usamos o %.3f para imprimir apenas 3 casas após a vírgula de uma variável de ponto flutuante.

##### Mais sobre escrita de dados e a estrutura printf neste link (http://linguagemc.com.br/operacoes-de-entrada-e-saida-de-dados-em-linguagem-c/)
