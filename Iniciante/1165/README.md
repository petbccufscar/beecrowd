# Problema:   
Na matemática, um Número Primo é aquele que pode ser dividido somente por 1 (um) e por ele mesmo. Por exemplo, o número 7 é primo, pois pode ser dividido apenas pelo número 1 e pelo número 7.

**Problema Completo**: https://www.urionlinejudge.com.br/judge/pt/problems/view/1165


# Resolução:
Iniciamos realizando a declaração das variaveis que iremos utilizar, dentre essas a `nCasos` irá armazenar a quantidade de casos de teste que iremos realizar, este valor será passado no começo, portanto logo em seguida utilizamos a função `scanf` para receber o valor. Duas variaveis `i` e `j` que serão utilizadas como contadores durante os laços de repetição `for` que iremos utilizar. Teremos ainda uma variavel `valor` que a cada iteração irá receber um valor para ser verificado a condição de primo, para isso utilizaremos uma variavel `primo` que utilizaremos esta usando os valores `0 ou 1` indicando ser ou não primo.

```c
int nCasos, valor, i, j, primo;
scanf("%d", &nCasos);
```

Em nosso laço de repetição principal realizamos a leitura do valor que será passado e definimos também inicialmente este como primo, pois nas etapas futuras caso este não seja primo esse valor é alterado
```c
for(i=0; i<nCasos; i++){
	scanf("%d", &valor);
	primo = 1;
```

Após recebido o valor utilizamos a variavel `j` como contador indo de 2 até o valor, verificando a condição de não possuir divisor, o que representa a condição de ser um número primo. Caso encontre um divisor, definimos a variavel `primo` como 0
```c
for(j=2; j<valor; j++)
	if(valor % j == 0)
		primo = 0;
```

Ao final realizamos a verificação do valor final contido na variavel `primo`, caso este seja igual a 1, imprimimos que o número é primo, caso contrário imprimimos que o valor não é primo.
```c
if(primo == 1)
	printf("%d eh primo\n", valor);
else
	printf("%d nao eh primo\n", valor);
```

    
Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com