# Problema:   
Na matemática, um Número Primo é aquele que pode ser dividido somente por 1 (um) e por ele mesmo. Por exemplo, o número 7 é primo, pois pode ser dividido apenas pelo número 1 e pelo número 7.

**Problema Completo**: https://www.urionlinejudge.com.br/judge/pt/problems/view/1165


# Resolução:
Iniciamos realizando a declaração das variáveis que iremos utilizar, dentre essas a `nCasos` irá armazenar a quantidade de casos de teste que iremos realizar, este valor será recebido no começo, portanto logo após a declaração de variáveis, utilizamos a função `scanf` para recebe-lo. Duas variáveis `i` e `j` que serão utilizadas como contadores durante os laços de repetição `for` que iremos utilizar. Teremos ainda uma variável `valor` que a cada iteração irá receber um valor para ser verificado a condição de primo, para isso utilizaremos a variável `primo` que assumirá valores `0 ou 1` indicando ser primo (1) ou não primo (0).

```c
int nCasos, valor, i, j, primo;
scanf("%d", &nCasos);
```

Em nosso laço de repetição principal realizamos a leitura do `valor` que será passado e definimos também inicialmente este como primo, pois nas etapas futuras teremos verificações que invalidam a condição de primo, alterando o valor da variável `primo` para 0.
```c
for(i=0; i<nCasos; i++){
	scanf("%d", &valor);
	primo = 1;
	if(valor == 1)
            primo = 0;
	
```
Observe que verificamos aqui se o `valor` recebido é 1 e caso positivo, setamos a variável primo para 0, já que o número 1 não é primo, pois apesar de ser divisível por 1 e ele mesmo, não possui 2 divisores.  
Após recebido o valor utilizamos a variavel `j` como contador indo de 2 até o valor, verificando a condição de não possuir divisor, o que representa a condição de ser um número primo. Caso encontre um divisor, definimos a variavel `primo` como 0
```c
for(j=2; j<valor; j++)
	if(valor % j == 0)
		primo = 0;
```

Ao final realizamos a verificação do valor final contido na variável `primo`, caso este seja igual a 1, significa que após dividirmos este valor por todos os números que o antecedem, partindo de 2, ele não foi divisível por nenhum, portanto, só é divisível por 1 e ele mesmo (condição de existência de um número primo). Assim, imprimimos que o número é primo e caso ele encontre ao menos um número divisor além de 1 e ele mesmo, imprimimos que o valor não é primo.
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
