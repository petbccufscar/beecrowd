# Problema:
No depósito da fábrica, encostada numa parede, existe uma matriz de N linhas por N colunas de caixas empilhadas. Cada caixa possui um peso inteiro positivo associado. O inspetor da fábrica precisa retirar algumas caixas da matriz de modo a deixar uma espécie de pirâmide de caixas satisfazendo as seguintes restrições:

• Se uma caixa está na pirâmide, a caixa imediatamente abaixo dela também deve estar na pirâmide;

• Na i-ésima linha de caixas (a linha 1 é a do topo da matriz), a pirâmide deve ter exatamente i caixas consecutivas.

Dados os pesos de todas as caixas na matriz, seu programa deve calcular o peso total mínimo que uma pirâmide poderá ter, se o inspetor retirar algumas caixas segundo as restrições acima.

##### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/2785

# Resolução:

Nesse exercício vamos criar um algoritmo para calcular o menor valor de uma pirâmide montada a partir dos números dados na matriz.

Para poder manipular matrizes do tipo `int` de tamanho 100x100, vamos criá-las como variáveis globais, ou seja, antes do `int main()`:
```c
int matriz[101][101], maux[101][101];
```
`matriz` é a matriz contendo os números da pirâmide que vamos montar. `maux` é uma matriz auxiliar, que vai guardar a menor soma possível de cada linha da outra matriz.

Nesse exercício vamos declarar seis variáveis locais do tipo `int`:
```c
  int tamMatriz, soma, inicio, fim, i, j;
```
`tamMatriz` irá guardar o tamanho da matriz. `soma` é o peso total das caixas da pirâmide, `inicio` e `fim` representam as colunas cujas caixas serão verificadas para fazer a pirâmide. `i` e `j` são variáveis auxiliares para o `for`.

Começamos o algoritmo lendo a variável `tamMatriz` usando `scanf`:
```c
  scanf("%d", &tamMatriz);
```
Com o tamanho da matriz, podemos ler todos os valores da matriz criada usando dois laços de repetição `for`. Para cada elemento da matriz usamos o `scanf`:
```c
  for (i = 0; i < tamMatriz; i++)
    for (j = 0; j < tamMatriz; j++)
      scanf("%d", &matriz[i][j]);
```
Completando os dados da matriz, podemos começar a analisar os números para formar a pirâmide. Igualamos `soma` a 0 e copiamos a primeira linha de `matriz` em `maux`:
```c
  soma = 0;
  for (i = 0; i < tamMatriz; i++)
    maux[0][i] = matriz[0][i];
```
A partir de agora, o `maux` será preenchido apenas com as menores somas obtidas em cada linha, levando em conta os menores valores da linha anterior. Para começar a preencher o `maux`, igualamos `i` a 1, `inicio` a 0 e `fim` a 1:
```c
  i = 1;
  inicio = 0;
  fim = 1;
```
`i` vai representar a linha que vamos preencher, `inicio` e `fim` representam a primeira e última coluna que serão somadas para descobrir a menor soma. Aqui criamos um `while` para repetição. Dentro dele vamos preencher `maux`:
```c
  while (i < tamMatriz-1) {
    for (j = inicio; j <= fim; j++)
      maux[i][inicio] += matriz[i][j];
    
    if (maux[i-1][inicio] < maux[i-1][inicio+1])
      maux[i][inicio] += maux[i-1][inicio];
    else
      maux[i][inicio] += maux[i-1][inicio+1];
    inicio++;
    fim++;
    if (fim == tamMatriz) {
      i++;
      inicio = 0;
      fim = i;
    }
  }
```
O `while` vai preencher as linhas da `maux` até a penúltima linha da matriz. A cada linha da matriz a diferença entre `inicio` e `fim` aumenta. A repetição possui três etapas:
* Etapa 1: soma os números das colunas `inicio` ao `fim` da linha `i` e adiciona essa soma em `maux[i][inicio]`.
* Etapa 2: compara o valor de `maux[i-1][inicio]` e `maux[i-1][inicio+1]`, que são as somas dos números da linha anterior das colunas que podem ser incluídas na pirâmide.
* Etapa 3: atualiza o valor de `inicio` e `fim` para poder fazer descobrir o próximo valor de `maux`. Se `fim` for igual a `tamMatriz` (`fim == tamMatriz`), isso indica que todas as somas da linha `i` foram feitas, então atualizamos as variáveis `i`, `inicio` e `fim` para fazer as somas da próxima linha da `matriz`.

Agora temos dois valores para comparar. Esses valores são as menores somas possíveis com os números da `matriz` da linha 0 a `tamMatriz-2`. Comparamos os valores e o menor será atribuído à variável `soma`:
```c
  if (maux[tamMatriz-2][0] < maux[tamMatriz-2][1])
    soma = maux[tamMatriz-2][0];
  else
    soma = maux[tamMatriz-2][1];
```
Por fim, criamos um laço de repetição `for` para somar todos os valores da última linha da `matriz` com a `soma` e chegar ao resultado pedido pelo exercício:
```c
  for(i = 0; i < tamMatriz; i++)
    soma += matriz[tamMatriz-1][i];
```
Como é uma pirâmide, todos os valores da última linha estarão incluídos na soma. Agora que temos o resultado, precisamos mostrar esse valor na tela usando `printf`:
```c
  printf("%d\n", soma);
```

##### Para aprender um pouco mais sobre matrizes: [Matrizes](http://linguagemc.com.br/matriz-em-c/)
##### Para aprender um pouco mais sobre a estrutura for: [For](http://linguagemc.com.br/a-estrutura-de-repeticao-for-em-c/)
##### Para aprender um pouco mais sobre a estrutura while: [While](http://linguagemc.com.br/o-comando-while-em-c/)
##### Para aprender um pouco mais sobre o uso de variáveis globais e locais: [Variáveis globais](http://linguagemc.com.br/funcoes-e-escopo-de-variaveis/)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
