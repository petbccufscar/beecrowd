# Problema:
Frequentemente, ao arredondar um número real para um inteiro nós o fazemos para cima se a parte fracionária é maior ou igual a 0,5 e para baixo se a parte fracionária é menor do que 0,5. Neste problema você recebe uma string num contendo um número real e uma string cutoff contendo um valor de corte. A string cutoff será formatada exatamente como "0.####", onde cada '#' representa um dígito ('0'-'9'). Pelo menos um dos dígitos da parte fracionária de cutoff será diferente de zero. Sua tarefa é arredondar num para cima se a parte fracionária é maior do que o valor de corte e para baixo caso contrário, devolvendo o resultado como um inteiro. Para evitar problemas com imprecisão de representação em ponto flutuante a parte fracionária de num não será exatamente igual a cutoff. Assim, o método tradicional de arredondamento descrito na frase inicial seria representado por cutoff = "0.5000"
 
##### Link do problema: https://www.urionlinejudge.com.br/judge/pt/problems/view/1305
 
 
# Resolução:
 
O problema é sobre determinar se iremos arredondar um número para cima ou para baixo. Para isso, verificamos se a parte fracionária é maior do que o valor de corte e se for, arredondamos-o para cima. Caso contrário, arredondamos-o para baixo.

Inicialmente, iremos incluir a biblioteca `<string.h>`, para utilizar as funções `atoi()`, que converte caractere para inteiro  e `atof()`, que converte caractere para double. Em seguida, iremos declarar dois vetores de caracteres `numero[10]` e `corte[7]`, indicando respectivamente o número (incluindo parte inteira e fracionária) e o valor de corte, uma variável do tipo inteiro `inteiro`, para armazenar somente a parte inteira do número e duas variáveis do tipo double, `fracionario` e `cutoff`, para armazenar somente a parte fracionária do número e o valor de corte, respectivamente.

```c
char numero[10];
char corte[7];

int inteiro;
double fracionario, cutoff;
```

Depois, como o final da entrada é determinado por `EOF`, utlizamos um laço de repetição `while( scanf("%s %s", numero, corte) != EOF)`. Com isso, lemos a entrada enquanto ela for diferente de `EOF` e a cada repetição do laço:

- convertemos `numero`, em caractere, para inteiro, utilizando `atoi()`;
- obtemos a parte fracionaria de `numero`, subtraindo-o pela sua parte inteira;
- convertemos `corte`, em caractere, para inteiro, utilizando `atof()`;
- verificamos se a parte fracionaria é maior que corte:
	- se sim, arredondamos a parte inteira para cima e a imprimimos.

```c
while( scanf("%s %s", numero, corte) != EOF){
		
		inteiro = atoi(numero);
		fracionario = atof(numero) - inteiro;
		cutoff = atof(corte); 

		if(fracionario > cutoff)
			inteiro++; 

		printf("%d\n", inteiro);
	}
```


Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
