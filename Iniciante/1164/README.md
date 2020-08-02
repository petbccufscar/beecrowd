# Problema: 
Na matemática, um número perfeito é um número inteiro para o qual a soma de todos os seus divisores positivos próprios (excluindo ele mesmo) é igual ao próprio número. Por exemplo o número 6 é perfeito, pois 1+2+3 é igual a 6. Sua tarefa é escrever um programa que imprima se um determinado número é perfeito ou não.

**Problema Completo**: https://www.urionlinejudge.com.br/judge/pt/problems/view/1164


# Resolução:

Iniciamos realizando a declaração das variáveis que iremos utilizar, dentre essas a `nCasos` irá armazenar a quantidade de casos de teste que iremos realizar, este valor será passado no começo, portanto logo em seguida utilizamos a função `scanf` para receber o valor. Teremos também uma variável `valor` que a cada iteração do nosso laço `for` irá receber um novo valor, duas variáveis `i` e `j` que serão usadas como contadores dentro de laços de repetição `for` e uma ultima variável `soma` para armazenar o valor que será somado e será usado ao final na verificação do número perfeito 
```c
int nCasos, valor, i, j, soma;
scanf("%d", &nCasos);
```

No nosso laço `for` principal iremos receber o valor que deve ser verificado sob a condição de número perfeito. Realizamos então a leitura do valor para ser utilizado durante a iteração corrente. Importante a cada iteração definir o valor da variável `soma` como 0 pois será utilizada individualmente em cada iteração e assim, o resultado da iteração anterior não interfere na atual
```c
for(i=0; i<nCasos; i++){
	scanf("%d", &valor);
	soma = 0;
```

Neste laço mais interno é realizado uma comparação, utilizando a variável `j` indo de 1 até a entrada armazenada em `valor`, não incluindo este, verificando todos os possíveis divisores, caso encontre algum divisor durante esse trajeto, é realizado o incremento à variável soma com o valor presente na variável `j`
```c
for(j=1; j<valor; j++)
	if(valor % j == 0)
		soma += j;
```

Ao final realizamos a verficação comparando o valor obtido através da soma de todos os divisores encontrados com o valor inicialmente passado, caso sejam iguais retornamos que o valor passado é um número perfeito, caso contrário retornamos que este não é um número perfeito.
```c
if(soma == valor)
	printf("%d eh perfeito\n", valor);
else
	printf("%d nao eh perfeito\n", valor);
```

    
Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
