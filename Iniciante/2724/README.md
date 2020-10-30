# Problema:
Patatatitu sabe muito sobre química, e conhece todos os compostos perigosos que podem ser feitos com os elementos disponíveis no kit de Juvenal. Assim, decidiu enviar um cd junto com o presente, contendo um programa que afira a segurança dos experimentos de Juvenal. Todos concordam que a criança mais bem-comportada do planeta nunca faria uma experiência sem antes checar sua segurança conforme as instruções. Porém Patatatitu não sabe programar e está atrás de ajuda. Você poderia ajudá-lo?

Para facilitar, Patatatitu explica que um composto perigoso é formado a partir da mistura de elementos na ordem de sua fórmula atômica e respeitando as devidas proporções. Neste kit de química é possível apenas adicionar um elemento por vez, em diferentes quantidades. Assim para formar trifluoreto de cloro (ClF3), um composto muito perigoso, deve-se adicionar um átomo cloro (Cl) e três de flúor (F3), independentemente do que for adicionado antes ou depois. ClF4 não é um composto perigoso, pois está fora de proporção. De forma similar caso Mg2F seja um composto perigoso, Mg2Fe será seguro, visto que flúor (F) é um elemento distinto de ferro (Fe).

##### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/2724

# Resolução:

Nesse exercício precisamos verificar se o experimento contém compostos perigosos ou não. Se for perigoso a resposta deve ser `Abortar` e se for seguro a mensagem será `Prossiga`.

Vamos declarar duas variáveis do tipo `char` e onze variáveis do tipo `int`:
```c
  char palavra[51][51], frase[51];
  int n, t, u, tam_frase, tam_palavra, posicao, perigo, i, j, k, l;
```
`palavra` é uma matriz que irá guardar a lista de compostos perigosos. `frase` é uma matriz de caracteres que representa o composto de experimento. `n` indica o número de casos de teste. `t` indica o número de compostos perigosos. `u` indica o número de experimentos a serem analisados. `tam_frase` indica o tamanho da `frase`. `tam_palavra` indica o tamanho em caracteres de um composto. `posicao` representa a posição da `frase` que está sendo verificada. `perigo` representa se o experimento é perigoso. `i`, `j`, `k`, `l` são variáveis auxiliares para o `for`.

Primeiro vamos ler o número de casos de teste. Aqui usaremos `scanf`:
```c
  scanf("%d", &n);
```
Sabendo o número de testes, criamos um laço de repetição `while` para realizar as experiências e escrevemos quantos compostos perigosos podem aparecer e quais são:
```c
  while (n > 0) {
    scanf("%d", &t);
    
    for(i=0;i<t;i++)
      scanf(" %50[^\n]",&palavra[i]);
```
Dentro do `scanf` usamos `%50[^\n]` para representar a leitura de um vetor de caracteres até um `\n` ou até chegar a 50 caracteres. Depois de obter os compostos perigosos vamos ler quantos experimentos vão ser feitos:
```c
    scanf("%d", &u);
```
Para verificar cada experimento, vamos criar um laço de repetição `for` para ler os elementos do experimento verificar se é perigoso ou não:
```c
    for(i=0;i<u;i++) {
      scanf(" %50[^\n]",&frase);
      tam_frase = strlen(frase);
      perigo = 0;
```
Depois de ler `frase`, igualamos `tam_frase` ao tamanho desse vetor obtido usando a função `strlen` da biblioteca [string.h](http://linguagemc.com.br/a-biblioteca-string-h/) e igualamos `perigo` a 0. Padronizando essas variáveis, vamos criar um outro laço de repetição para verificar se cada composto perigoso descrito está contido no experimento:
```c
      for(j = 0; j < t; j++) {
        for (k = 0; k < tam_frase; k++) {
          if (palavra[j][0]==frase[k]) {
            posicao = k;
            tam_palavra = 0;
```
Para cada um dos `t` compostos perigosos, vamos passar por todas as posições da `frase` e, se `frase[k]` é igual ao primeiro elemento do composto a ser verificado (`palavra[j][0]`), igualamos `tam_palavra` a 0 e `posicao` a `k` para verificar se os próximos elementos coincidem:
```c
            for(l = 0; l < strlen(palavra[j]); l++) {
              if(palavra[j][l] == frase[posicao])
                tam_palavra++;
                
              posicao++;
              
              if (tam_palavra == strlen(palavra[j])) {
                if ((posicao >= strlen(frase)) || (frase[posicao] >= 65 && frase[posicao] <= 90)) {
                  perigo = 1;
                  l = strlen(palavra[j]);
                  k = tam_frase;
                  j = t;
                }
                else
                  tam_palavra = 0;
              }
            }
          }
        }
      }
```
Criamos um outro laço de repetição para verificar cada elemento de `palavra[j]`. Se o elemento coincide com o termo em `frase[posicao]`, incrementamos `tam_palavra`. Depois incrementamos o valor de posição e, se `tam_palavra` for igual ao comprimento de `palavra[j]` (`strlen(palavra[j])`), verificamos se a frase chegou ao fim ou se o próximo termo é uma letra maiúscula. Se for, descobrimos que há um composto perigoso no experimento, então encerramos as repetições e podemos mostrar a mensagem `Abortar`.

Terminada a repetição, fazemos um `if` para verificar se perigo é 1 ou 0. Se for 1 escrevemos a mensagem `Abortar`, senão mostramos na tela `Prossiga`:
```c
      if (perigo == 1)
        printf("Abortar\n");
      else
        printf("Prossiga\n");

      memset(frase, ' ', strlen(frase));
    }
    n--;
    if (n > 0)
      printf("\n");
  }
```
Terminada a verificação desse experimento, usamos a função [memset](https://www.tutorialspoint.com/c_standard_library/c_function_memset.htm) para limpar o vetor `frase` e continuamos a repetição. Para cada sequência de experimentos decrementamos o valor de `n` e, para escrever a resposta com o padrão do URI, mostramos na tela uma linha em branco depois do caso de teste.

##### Para aprender um pouco mais sobre vetores: [Vetores](http://linguagemc.com.br/vetores-ou-arrays-em-linguagem-c/)
##### Para aprender um pouco mais sobre matrizes: [Matrizes](http://linguagemc.com.br/matriz-em-c/)
##### Para aprender um pouco mais sobre a estrutura for: [For](http://linguagemc.com.br/a-estrutura-de-repeticao-for-em-c/)
##### Para aprender um pouco mais sobre a estrutura while: [While](http://linguagemc.com.br/o-comando-while-em-c/)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
