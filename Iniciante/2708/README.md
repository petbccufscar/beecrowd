# Problema:   
A agência de turismo municipal da cidade de Ica, no Peru montou um posto de controle de jipes de aventura que sobem para as dunas do parque Hucachina. Como durante o dia, são vários os off-roads que sobem e descem do parque nacional, e nem sempre os turistas usam um mesmo transporte para a ida e volta, a prefeitura precisava ter um melhor controle e segurança sobre fluxo de visitantes no parque. Desenvolva um programa que receba como entrada se um jipe está entrando ou voltando do parque e a quantidade de turistas que este veículo está transportando. Ao final do turno, o programa deve indicar a quantidade de veículos e de turistas que ainda faltam regressar da aventura.

**Problema Completo**: https://www.urionlinejudge.com.br/judge/pt/problems/view/2708

# Resolução:

Iniciaremos a resolução deste problema com a inserção da blibioteca `string.h`, ela nos forncece funções para manipularmos strings como exemplo a função que usaremos, a `strcmp()` realiza a comparação entre dois elementos e nos retorna se estes são iguais ou diferentes, usaremos esta função para verificar qual foi a operação em cada iteração.
```c
#include <string.h>
```


Mas antes, declaramos algumas variaveis inteiras `turistas`, `jipes` e `turistasFaltantes`, estas serão responsaveis por respectivamente, armazenar a cada iteração a quantidade de turistas que estão chegando ou saindo em um jipe, uma variavel para contabilizar quantos jipes foram e ainda não voltaram e quantos turistas, dentre os que foram no passeio, ainda não voltaram. Declaramos também uma variavel para recebermos qual foi a operação realizado pelo jipe, sendo esse de saida ou chegada, ou ainda se encerraram os passeios.
```c
int turistas, jipes = 0, turistasFaltantes = 0;
char operacao[10];
```


Através da estrutura de repetição `while` com o valor "1" como parametro, iremos realizar as iterações, iniciando pela leitura da operação, esta iremos armazenar em nossa variavel do tipo `char`.
```c
while (1){
	scanf("%s", operacao);
	...
}
```


Dentro de nosso laço de repetição a primeira verificação que vamos fazer, após recebido e armazenado em `operacao`, é para verificar se foi recebido o conteudo "ABEND" que indica fim de processamento. Caso positivo, realizamos um `break` e saimos de nosso laço de repetição.

```c
if (strcmp(operacao, "ABEND") == 0)
	break;
```


Caso contrario, seguimos em nesso laço realizamo a leitura de quantos turistas embarcaram ou desembarcaram e iremos agora verificar se a operação foi "SALIDA" ou "VUELTA".
- Caso tenha sido "SALIDA" iremos somar em `turistasFaltantes` o valor recebido em `turistas` pois estes estão saindo para o passeio e deve ser armazenado esse valor para conferir se ao final todos voltaram, o mesmo para a quantidade de jipes que ficará armazenada na variavel `jipes` porém nesta variavel iremos incrementar apenas em 1 pois apenas um jipe esta saindo.
- Caso tenha sido "VUELTA" subtraimos o valor contido em `turistas` do total contido em `turistasFaltantes` indicando que esta quantidade de turistas voltaram do passeio, restando apenas os que ainda não voltaram, o mesmo para a variavel `jipe`, indicando que um jipe retornou do passeio.

```c
scanf("%d", &turistas);
if (strcmp(operacao, "SALIDA") == 0)
	turistasFaltantes += turistas, jipes++;
else
	turistasFaltantes -= turistas, jipes--;
```


Ao final, ou seja ao receber o sinalizador de fim de processamento "ABEND", realizamos a impressão de quantos turistas não retornaram de seu passeio de jipe e na linha de baixo a quantidade de jipes que não retornaram.
```c
printf("%d\n%d\n", turistasFaltantes, jipes);
```


##### Para revisar as funções da biblioteca: [string.h](http://linguagemc.com.br/a-biblioteca-string-h/)
    
Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com