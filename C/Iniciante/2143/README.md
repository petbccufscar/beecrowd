# Problema:
Todo ano após a competição que ocorre na cidade de Taxilândia, os participantes e os coaches vão para o célebre restaurante Radar. Porém, os garçons (sempre muito gentis e educados) ficam sobrecarregados devido à quantidade de pessoas, e consequentemente, acabam demorando um pouco para atender a um pedido.

Os participantes ou coaches que sentam nas pontas são os privilegiados, pois são atendidos com somente um pedido, mas os demais precisam sempre pedir duas vezes, pois os garçons (apesar de gentis e educados) são desatentos e se esquecem facilmente dos pedidos. Além disso, há uma superstição entre os participantes e coaches de que se não houver um número par de pessoas que não sentam nas pontas, na próxima competição nenhuma equipe da universidade conseguirá vencer.

Portanto, sua tarefa é determinar a soma da quantidade de pedidos de cada um para saber se vale a pena ir ao Radar. Mas apesar do resultado, lembre-se: sempre vale a pena ir ao Radar!

Entrada

A entrada é composta por T (1 ≤ T ≤ 100) indicando a quantidade de casos de teste e então, T inteiros N (3 ≤ N ≤ 104), indicando a quantidade de pessoas. A mesa é retangular e haverá pelo menos e no máximo uma pessoa em uma das pontas, isto é, se uma ponta estiver vazia, a outra deve ser ocupada, ou senão, as duas pontas estarão ocupadas, mas o número de pessoas que não estão nas pontas sempre será par. O final da entrada é indicado por T = 0.
 
 
##### Link do problema: https://www.urionlinejudge.com.br/judge/pt/problems/view/2143
 
 
# Resolução:

Embora a explicação da entrada seja complicada, na verdade o exercício é simples. Note que, conforme o enunciado, as pontas de uma mesa nunca estarão vazias, sempre haverá uma ou duas pessoas sentadas nestas e que todas, exceto as sentadas nas pontas, irão repetir o pedido duas vezes.

A ponta da mesa terá duas pessoas sentadas quando o número de pessoas lido for par e uma quando este número for ímpar. Então, quando só houver uma pessoa sentada na ponta, o número de pedidos será `N*2 - 1`, ao passo que quando houver duas pessoas sentadas nas pontas, o número de pedidos será `N*2 - 2`.

Além disso, caso o valor lido seja 1,2 ou 3, este valor indica uma nova quantidade de casos teste. O programa encerra quando o valor lido for 0.

Iremos declarar três variáveis inteiras, `T`,`N` e `i`.

```c
int T, N, i;
```

Depois, lemos o valor de `T`, por meio da função `scanf()`.

```c
scanf("%d",&T);
```

Em seguida, vamos utilizar a estrutura de repetição `while( T > 0)` para o programa funcionar até que o valor de `T` lido seja 0.
Dentro deste laço, usaremos outro laço, a estrutura de repetição `for` para calcular T quantidades de pedido.

A cada iteração do laço de repetição:
- lemos `N` ;
- Verificamos `N` é par ou ímpar:
    -caso seja par, exibimos `N*2 - 2`
    -caso seja ímpar, exibimos `N*2 - 1`

Fora da estrutura de repetição `for`, lemos `T` novamente, para verificar se o programa continua a funcionar ou não.

```c
while( T > 0){
        
        for(i=0; i < T; i++){
            scanf("%d", &N);
            
            if ( N%2 == 0 )
                printf("%d\n", N*2 - 2);
            else
                printf("%d\n", N*2 - 1);
        }

    scanf("%d", &T);
    }
```
 
 
Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com