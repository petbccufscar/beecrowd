# Problema:
... Semana passada, Vovó Zazá e seus colegas de turma foram ao cinema assistir a um filme, mas ficaram estarrecidos com o aumento do preço do ingresso. Revoltados, eles decidiram fazer uma manifestação contra o sistema capitalista opressor, agendada para amanhã na Praça General Bertaso. Vovó Zazá quer colaborar com o movimento fazendo um cartaz com a seguinte palavra de ordem:

QUE ABSURDO! O PREÇO DO CINEMA SUBIU … % !!

Mas ela não é muito boa em Matemática, e está solicitando sua ajuda para calcular a porcentagem de que precisa para completar o cartaz.
 
 
##### Link do problema: https://www.urionlinejudge.com.br/judge/pt/problems/view/1963
 
 
# Resolução:
 
Para calcular o aumento percentual do valor do ingresso, iremos dividir o novo preço pelo preço inicial, subtrair 1 e depois multiplicar por 100.

Iremos declarar duas variáveis do tipo `dou,ble`  `valorInicial` e `valorNovo`.
 
```c
double valorInicial, valorNovo;
```
  
Em seguida, iremos calcular e exibir o aumento percentual, com duas casas decimais e quebra de linha, por meio da função `printf()` a seguir. Note que para exibirmos a porcentagem corretamente basta escrevê-la duas vezes, `%%`.

```c
printf("%.2lf%%\n", ( (valorNovo/valorInicial)-1)*100);
```
 
##### Mais sobre aumento percentual: [aumento percentual](https://pt.wikihow.com/Calcular-Aumento-Percentual)
 
Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com