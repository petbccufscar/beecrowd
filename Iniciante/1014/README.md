# Problema

O arquivo de entrada contém dois valores: um valor inteiro X representando a distância total percorrida (em Km), e um valor real Y representando o total de combustível gasto, com um dígito após o ponto decimal.

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/1014

# Resolução

Neste problema, iremos receber dois valores reais e dividiremos o primeiro (distância) pelo segundo (gasto de combustível) para obtermos a média de consumo que esse automóvel fez nessa distância.

Primeiro, deve-se declarar as variáveis a serem utilizadas. Neste exercício, teremos uma variável inteira para armazenar os quilômetros e duas do tipo ponto flutuante,
uma para armazenar o combustível gasto e outra para armazenar o resultado da divisão entre essas duas.

```c
	int km;
    float combustivel, km_l;
```

Para leitura da entrada, utiliza-se a função `scanf`, que lerá os 2 valores juntos, podendo ser diferenciados na entrada por um espaço ou a tecla enter (quebra de linha)

```c
	scanf("%d %f", &km, &combustivel);
```

Para resolver esse problema, devemos apenas efetuar uma simples divisão entre `km` e `combustivel` e armazena-la em `km_l` para obter a media de km/l da viagem.

```c
	km_l = km / combustivel;
```

Para imprimir uma saída, exibindo-a na tela, é utilizada a função `printf`.

```c
	printf("%.3f km/l\n",km_l);
```

Aqui usamos o `%.3f` para imprimir apenas 3 casas após a vírgula de uma variável de ponto flutuante.


##### Para aprender um pouco mais sobre variáveis: [Variáveis](http://linguagemc.com.br/variaveis-em-linguagem-c/)

##### Para entender sobre entradas e saídas: [Entrada e Saida](http://linguagemc.com.br/operacoes-de-entrada-e-saida-de-dados-em-linguagem-c/)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
