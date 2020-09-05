# Problema:
O seu professor gostaria de fazer um programa com as seguintes características:

1. Leia os dados de um CPF no formato XXX.YYY.ZZZ-DD;
2. Imprima os quatro números, sendo um valor por linha.

**Problema Completo**: https://www.urionlinejudge.com.br/judge/pt/problems/view/2763


# Resolução:
O exercício consiste em realizar o armazenamento da entrada separadamente, para que seja possível avaliá-la e, então, exibir de acordo com padrão do CPF.  

Como primeiro passo, declaramos as variáveis inteiras `X`, `Y`, `Z` e `D`. Estas armazenarão, através da função `scanf()`, cada uma das 4 partes do documento, ou seja, os valores que estão entre os pontos (.) e o traço (-).  

```c
int X, Y, Z, D;

scanf("%d.%d.%d-%d", &X, &Y, &Z, &D);
```  

Utilizamos, então, a estrutura condicional `if-else` para verificar se os números lidos possuem algum 0 a esquerda, uma vez que serão desconsiderados pelo armazenamento do tipo `int`, mas são importantes para a estrutura do CPF.  
Iniciando pela variável `X`, caso o valor armazenado nesta seja inferior a 10, devemos exibi-lo com acréscimo 2 zeros à esquerda para respeitar o padrão de 3 dígitos. O comando `else` considera a situação em que isto não ocorre, ou seja, o valor é maior do que 10 e, assim, analisamos outros dois cenários possíveis:  
* o inteiro é menor que 100 e, assim, `printf()` exibe um único zero a esquerda da variável;
* nenhum dos casos anteriores foi satisfeito, portanto o valor já é representado através de 3 dígitos e basta que este seja exibido como está na memória.  

```c
if(X<10)
  printf("00%d\n",X);

else{
  if(X<100)
    printf("0%d\n",X);

	else
		printf("%d\n",X);
}
```  

Como `Y` e `Z` também são fragmentos que devem ser expressos em 3 dígitos, a mesma lógica ocorre para estes.  

```c
if(Y<10)
  printf("00%d\n",Y);

else{
  if(Y<100)
    printf("0%d\n",Y);

	else
		printf("%d\n",Y);
}
```  

```c
if(Z<10)
  printf("00%d\n",Z);

else{
  if(Z<100)
    printf("0%d\n",Z);

	else
		printf("%d\n",Z);
}
```  

No entanto, visto que `D` guarda o número existente após `-`, o qual deve conter apenas 2 dígitos, sua análise é um pouco diferente. Verificamos se o valor é menor do que 10 e, caso positivo, adicionamos um 0 à esquerda de `%d` na exibição do `printf()`. Em caso negativo, significa que este já contém 2 algarismos, então podemos apenas mostrá-lo na tela.  

```c
if(D<10)
  printf("0%d\n",D);
else
  printf("%d\n",D);
```


##### Para aprender um pouco mais sobre a estrutura condicional: [O teste condicional IF ELSE](https://www.cprogressivo.net/2013/01/O-testecondicional-IF-ELSE.html)  

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso [Facebook](https://www.facebook.com/petbcc/), [Instagram](https://www.instagram.com/petbcc.ufscar/) ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
