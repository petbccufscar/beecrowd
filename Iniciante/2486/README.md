# Problema:
Ultimamente, diversas pessoas estão indo à Dra. Cláudia Café com Leite para saber se estão consumindo a quantidade recomendada diária de vitamina C. Isso tem a deixado exausta, e por isso ela lhe pediu para escrever um programa que, dado o consumo diário de alimentos ricos em vitamina C por uma pessoa, indique o quanto essa pessoa deve consumir a mais ou a menos para atingir o recomendado.

Para tal, você poderá utilizar a tabela a seguir:

Alimentos ricos em Vitamina C | Quantidade de Vitamina C
------------------------------| -----------------------
suco de laranja               | 120 mg
morango fresco                | 85 mg
mamao                         | 85 mg
goiaba vermelha               | 70 mg
manga                         | 56 mg
laranja                       | 50 mg
brocolis                      | 34 mg

Considere que o consumo diário recomendado de vitamina C está entre 110 mg e 130 mg, inclusive.

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/2486

# Resolução:
Para resolver esse problema, iremos receber uma quantidade de alimentos, a quantidade e o nome de um determinado alimento. A patir disso, iremos multiplicar o valor indicado na tabela, referente ao nome do alimento com a quantidade desse alimento e somaremos esse resultado com os outros alimentos. Assim, exibimos o quanto uma pessoa deve ingerir a mais ou a menos para atingir o indice recomendado de vitamina C.

Começamos inserindo a biblioteca `string.h`, que contém a função `strncmp` e será utilizada posteriormente para comparar duas `strings`.
```c
	#include <string.h>
```

Em seguida, vamos declarar as variáveis, que serão: `quantDiaria`, que irá armazenar a quantidade diária de alimentos consumidos; `quantAlimento`, que armazenará a quantidade consumida de um determinado alimento; `quantVitaminaC`, que irá guardar o total de vitamina C consumido diariamente; `i`, que servirá para iterar sobre um laço de reptição e `alimento`, para receber o nome de um determinado alimento.
```c
int quantDiaria, quantAlimento, quantVitaminaC, i;
char alimento[16];
```
* Note que `alimento` é um vetor de caracteres.

Depois, recebemos a quantidade diária de alimentos consumidos com a função `scanf`.
```c
 scanf("%d", &quantDiaria);
```

Iniciamos um laço de repetição `while`, que irá calcular a quantidade de vitamina C ingerida diariamente até que a `quantAlimentos` seja zero, ou seja, não há mais casos para testar. 
```c
while(quantDiaria != 0){  
```

Iniciamos a variável `quantVitaminaC` em 0 dentro do `while`, pois ainda iremos calcular a quantidade de vitamina C, e criamos um loop `for`. Dentro dele, vamos receber a quantidade de um determinado alimento com `scanf` e o nome do alimento com `fgets`, até que a `quantDiaria` seja atingida. 
```c
quantVitaminaC = 0;

for(i=0; i<quantDiaria; i++){
	scanf("%d ", &quantAlimento);
	fgets(alimento, sizeof(alimento), stdin); 
```
 * Obs: Utilizamos a função `fgets`, que tem a mesma função do `scanf` com a diferença de que podemos ler espaços(' ') mais facilmente do que com o `scanf`.

Com isso, iremos calcular a quantidade de vitamina C ingerida diariamente. Para isso, verificamos se o nome do alimento recebido é igual a algum alimento presente na tabela. Caso seja, multiplicamos a quantidade de alimentos pela quantidade de vitamina C, também dada na tabela do problema. 
Utilizamos a função `strncmp` para comparar duas `strings`. Se o nome do alimento for igual a `alimento`, a função retorna 0 e, com o operador `!`, mudamos esse 0 para 1 tornando a condição do `if` verdadeira.  
```c
if (!strncmp(alimento, "suco de laranja", 15))
	quantVitaminaC += quantAlimento * 120;
else if (!strncmp(alimento, "morango fresco", 14))
	quantVitaminaC += quantAlimento * 85;
else if (!strncmp(alimento, "mamao", 5))
	quantVitaminaC += quantAlimento * 85;
else if (!strncmp(alimento, "goiaba vermelha", 15))
	quantVitaminaC += quantAlimento * 70;
else if (!strncmp(alimento, "manga", 5))
	quantVitaminaC += quantAlimento * 56;
else if (!strncmp(alimento, "laranja", 7))
	quantVitaminaC += quantAlimento * 50;
else if (!strncmp(alimento, "brocolis", 8))
	quantVitaminaC += quantAlimento * 34;
```

Assim, no fim do `for`, temos a quantidade total de vitamina C consumida e verificamos se o consumo está dentro do recomendado diariamente (entre 110 e 130mg). 
Caso esteja acima do recomendado, exibimos que está acima e a quantidade de mg a mais que está sendo consumida; 
Caso contrário, exibimos que está abaixo e a quantidade a menos de mg que está sendo consumida;
Caso esteja dentro do recomendado, exibimos a quantidade de mg consumida.    
```c
if(quantVitaminaC>130)
	printf("Menos %d mg\n", quantVitaminaC-130);

else if(quantVitaminaC<110)
	printf("Mais %d mg\n", 110-quantVitaminaC);
		
else
	printf("%d mg\n", quantVitaminaC);
```

Por fim, recebemos uma nova quantidade total de alimentos que serão testados ou o valor 0 que irá encerrar o programa.
```c
scanf("%d", &quantDiaria); 
```

##### Para aprender um pouco mais sobre o laço de repetição `for` : [for](http://linguagemc.com.br/a-estrutura-de-repeticao-for-em-c/)
##### Para aprender um pouco mais sobre a função `fgets`: [fgets](https://aprendendoc.wordpress.com/tag/fgets/)
##### Para aprender um pouco mais sobre a biblioteca `string.h`e a funçao `strncmp`: [string.h e strncmp](http://linguagemc.com.br/a-biblioteca-string-h/)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
* [Facebook](https://www.facebook.com/petbcc/),
* [Instagram](https://www.instagram.com/petbcc.ufscar/)
* ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com


