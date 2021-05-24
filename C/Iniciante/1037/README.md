# Problema:
 
Você deve fazer um programa que leia um valor qualquer e apresente uma mensagem dizendo em qual dos seguintes intervalos ([0,25], (25,50], (50,75], (75,100]) este valor se encontra. Obviamente se o valor não estiver em nenhum destes intervalos, deverá ser impressa a mensagem “Fora de intervalo”.
 
##### Link do problema: https://www.urionlinejudge.com.br/judge/pt/problems/view/1037
 
# Resolução:

Em suma o problema é identificar em qual intervalo está o número a ser lido, ou seja, após ter lido o número será feito uma série de comparações (uma para cada intervalo), caso o número esteja em algum intervalo será impresso qual o intervalo, caso contrário será impresso “Fora de intervalo”.
 
Sabemos que o programa somente irá receber uma informação (valor) do tipo `ponto flutuante`, portanto devemos reservar somente uma variável do mesmo tipo:
 
```c
    float valor;
```
 
Para lermos um valor do tipo `float` usamos a função `scanf()` e usamos `%f` para indicar que será lido um valor tipo `float`:
 
```c
    scanf("%f", &valor);
```
 
Em seguida faremos uma série de comparações para descobrir se o valor está em algum intervalo válido e, se estiver, em qual está. Para isso iremos utilizar as funções `if` e `else` (respectivamente **se** e **senão**) somadas aos operadores relacionais (exemplos `>,>=,=<,<`) e lógicos (exemplos `&&, ||`).
 
Obs: Quando a condição dentro da função `if()` for verdadeira seu trecho de código referente será executado e o do `else` não e vice-versa.
 
Os operador relacionais retornam se a respectivas comparações são verdadeiras(1) ou falsas(0). Os operadores lógicos fazem a correlação dos termos lógicos, ou seja, faz a correlação de verdadeiro e falso.
 
Caso não esteja em nenhum intervalo temos que imprimir que o valor está fora do intervalo, mas caso esteja devemos imprimir qual o intervalo:
 
```c
if (valor >= 0 && valor <= 25)
  printf("Intervalo [0,25]\n");
else if (valor > 25 && valor <= 50)
  printf("Intervalo (25,50]\n");
else if (valor > 50 && valor <= 75)
  printf("Intervalo (50,75]\n");
else if (valor > 75 && valor <= 100)
  printf("Intervalo (75,100]\n");
else
  printf("Fora de intervalo\n");
```
 
##### Para aprender um pouco mais operações sobre entrada e saída de dados: [Entrada e saída](http://linguagemc.com.br/operacoes-de-entrada-e-saida-de-dados-em-linguagem-c/)
 
##### Para revisar sobre variáveis: [Variáveis](http://linguagemc.com.br/variaveis-em-linguagem-c/)
 
##### Para revisar sobre tipos de variáveis: [Tipos de Variáveis](http://linguagemc.com.br/tipos-de-dados-em-c/)
 
##### Para aprender um pouco mais sobre operadores relacionais: [Operadores relacionais](http://linguagemc.com.br/operadores-relacionais/)
 
##### Para aprender um pouco mais sobre operadores lógicos: [Operadores logicos](http://linguagemc.com.br/operadores-logicos-em-c/)
 
Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
 
