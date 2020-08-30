# Problema:   
A agência de turismo municipal da cidade de Ica, no Peru montou um posto de controle de jipes de aventura que sobem para as dunas do parque Hucachina. Como durante o dia, são vários os off-roads que sobem e descem do parque nacional, e nem sempre os turistas usam um mesmo transporte para a ida e volta, a prefeitura precisava ter um melhor controle e segurança sobre fluxo de visitantes no parque. Desenvolva um programa que receba como entrada se um jipe está entrando ou voltando do parque e a quantidade de turistas que este veículo está transportando. Ao final do turno, o programa deve indicar a quantidade de veículos e de turistas que ainda faltam regressar da aventura.

**Problema Completo**: https://www.urionlinejudge.com.br/judge/pt/problems/view/2708

# Resolução:

Iniciaremos a resolução deste problema com a inserção da biblioteca `string.h`, ela nos fornece funções para manipularmos strings como exemplo a função que usaremos, a `strcmp()` realiza a comparação entre dois elementos e nos retorna se estes são iguais ou diferentes, usaremos esta função para verificar qual foi a operação em cada iteração.
```c
#include <string.h>

##### Para revisar as funções da biblioteca: [string.h](http://linguagemc.com.br/a-biblioteca-string-h/)
    
Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
