# Problema:

Neste momento está sendo escolhida a data do evento. Para que todas as pessoas possam participar, foi decidido que o encontro na pizzaria ocorrerá em um data tal que todas as N pessoas podem comparecer à pizzaria nesta data. Portanto, nem toda data pode ser escolhida, pois algumas pessoas podem ter outros compromissos já marcados em alguns dias.

Dada a lista de datas consideradas para o evento e a informações de quais pessoas podem comparecer em quais datas, determine se o evento poderá ocorrer e, em caso positivo, sua data. Caso mais de uma data seja possível, o evento deve ocorrer o mais cedo possível.

##### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/2554

# Resolução:

A ideia do exercício é que você mostre na tela a data do encontro dos amigos e, caso não seja possível, escrever `Pizza antes de FdI`.

Nesse exercício vamos declarar oito variáveis do tipo `int`:
```c
  int n, d, p, num1, evento, conf, i, j;
```
`n` irá guardar o número de amigos que irão pra pizzaria. `d` é o número de datas que podem ser escolhidas para o evento, `p` é uma variável que será usada como resposta se uma pessoa vai (1) ou não (0). `num1` é uma variável auxiliar que vai ser usada para contar quantos "1" apareceram como resposta em `p`. `evento` vai indicar qual data foi escolhida. `conf` vai ser usada para marcar se o evento já foi marcado. `i` e `j` serão variáveis auxiliares para o `for`.


O exercício aborda um caso de leitura em que deve ser lido até o final do arquivo [EOF - End of File](https://pt.wikipedia.org/wiki/EOF). Fazemos a leitura do `n` e `d` no `scanf` dentro do `while`:
```c
  while (scanf("%d %d", &n, &d) != EOF) {
```
Um único `scanf` pode ler mais de um valor se usarmos mais de um `%d`. Dentro do `while`, fazemos a leitura e comparamos ao EOF, portanto o `while` irá rodar até chegar no final do arquivo. Este é simbolizado pela quebra de linha (`\n`).

Agora, criamos mais três variáveis do tipo `int`, elas representam vetores e cada uma delas vai guardar um vetor de dias, meses e anos, respectivamente:
```c
    int data_dia[d], data_mes[d], data_ano[d];
```
Para poder verificar se a data foi marcada e qual é a data, igualamos `evento` a -1 e `conf` a 0:
```c
    evento = -1;
    conf = 0;
```
Aqui usamos um `for` para repetição. dentro dela lemos as datas possíveis para o evento com `scanf`:
```c
    for (i=0;i<d;i++) {
      scanf("%d/%d/%d", &data_dia[i], &data_mes[i], &data_ano[i]);
```
Agora temos que verificar quem pode participar na data escrita acima. Marcamos inicialmente que o número de pessoas que participarão é 0 (`num1 == 0`) e criamos um novo `for`:
```c
      num1 = 0;
      for (j=0;j<n;j++) {
        scanf("%d", &p);
        if (p==1)
          num1++;
      }
```
Dentro do laço de repetição, verificamos a resposta de cada pessoa. Se `p` for 1, significa que a pessoa confirmou a sua presença nesse dia, então incrementamos o valor de `num1`.

Depois de ter a resposta de todos os convidados, podemos saber se o evento será nesse dia. O evento está confirmado se todas as pessoas responderem que podem ir (`num1 == n`). Além disso, devemos verificar sse já não tem uma outra data confirmada para o evento (`!conf`):
```c
      if ((num1 == n) && (!conf)) {
        evento = i;
        conf = 1;
      }
    } 
```
Nesse caso, `!conf` equivale à `conf == 0`. Dentro do `if` igualamos `evento` a `i`, já que os números guardados na posição `i` de `data_dia[]`, `data_mes[]` e `data_ano[]` representam a data do evento. Também igualamos `conf` a 1 para indicar que o evento já está marcado.

Por fim, mostramos na tela quando o evento vai ser realizado ou `Pizza antes do FdI` caso não tenha marcado o evento:
```c
      if (evento != -1)
        printf("%d/%d/%d\n", data_dia[evento], data_mes[evento], data_ano[evento]);

      else
        printf("Pizza antes de FdI\n");
  }
```
##### Para aprender um pouco mais sobre vetores: [Vetores](http://linguagemc.com.br/vetores-ou-arrays-em-linguagem-c/)
##### Para aprender um pouco mais sobre a estrutura for: [For](http://linguagemc.com.br/a-estrutura-de-repeticao-for-em-c/)
##### Para aprender um pouco mais sobre if: [Estruturas de decisão](http://linguagemc.com.br/estrutura-de-decisao-if-em-linguagem-c/)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
