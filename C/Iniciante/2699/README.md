# Problema:
Preocupado que seu mapa pudesse acabar nas mãos erradas, “Cabeça Queijosa” usou suas habilidades em matemática como seguro contra ladrões. Em vez de escrever na carta o número indicando a distância, ele multiplicou-o por um segundo número N, e escreveu o resultado D na carta, junto com o valor de N e uma explicação de como o cálculo deveria ser feito. Ele sabia que mesmo se uma pessoa indesejada obtivesse a carta, ela deveria saber como dividir dois números, coisa que poucos criminosos conseguiam fazer naquele tempo. Infelizmente, quando a carta chegou em seu destino na Europa, a sobrinha de Cabeça Queijosa havia entrado em um convento e nem se importou em abrir a carta.

Exatamente quatro séculos após o ocorrido, Maria por ventura veio a obter um baú com os pertences de sua ancestral freira. E você pode imaginar sua surpresa quando ela descobriu a carta, ainda lacrada! Maria está planejando uma viagem para buscar o tesouro de Cabeça Queijosa, mas ela precisa de sua ajuda. Apesar do valor de N estar intacto e ela poder lelo, o número D foi parcialmente comido por traças de forma que apenas alguns dos dígitos estão visíveis . A única pista que Maria tem é que o digito mais à esquerda de D não é zero pois Cabeça Queijosa disse em sua carta.

Dada a representação parcial de D e o valor de N, você deve determinar o menor valor possível de D de forma que este seja um múltiplo de N e que não comece com zeros.

##### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/2699

# Resolução:

O objetivo desse exercício é descobrir o menor múltiplo de N dado os dígitos presentes na carta. No código vamos precisar saber como funciona a [divisão de números grandes usando vetor de caracteres](https://www.geeksforgeeks.org/divide-large-number-represented-string/).

Nesse exercício vamos usar variáveis que serão modificadas dentro de uma função fora do `int main()`. Por isso criaremos três variáveis globais, sendo duas do tipo `char` e uma do tipo `int`:
```c
char s[1001], d[1001];
int verificador[1001][1001];
```
`s` e `d` são dois vetores de caracteres, eles representam a entrada e a resposta, respectivamente. `verificador` é uma matriz auxiliar que vai controlar se o programa já passou por uma determinada posição do vetor `s`, o que é importante para não ocorrer loop infinito.

Esse código foi dividido em duas partes: o `int main()` e a função `divisao`. Vamos começar explicando o `int main()`.

Dentro do main vamos criar três variáveis do tipo `int`:
```c
  int n, i, j;
```
`n` representa o divisor que será usado na divisão. `i` e `j` são variáveis auxiliares para a estrutura `for`.

O exercício aborda um caso de leitura em que deve ser lido até o final do arquivo [EOF - End of File](https://pt.wikipedia.org/wiki/EOF). Fazemos a leitura do `s` e `n` no `scanf` dentro do `while`:
```c
  while(scanf(" %s %d ", s, &n) != EOF) {
```
Dentro do `while`, fazemos a leitura e comparamos ao EOF, portanto o `while` irá rodar até chegar no final do arquivo. Este é simbolizado pela quebra de linha (`\n`). Obtendo o vetor `s` usamos a função strcpy da biblioteca [string.h](http://linguagemc.com.br/a-biblioteca-string-h/) para copiar a informação obtida para o vetor `d`:
```c
    strcpy(d, s);
```
Agora vamos padronizar a matriz `verificador` igualando todos os valores dela para -1. Dessa forma poderemos controlar quais verificações já foram feitas na função `divisao`:
```c
    for (i = 0; i < 1001; i++)
      for (j = 0; j < 1001; j++)
        verificador[i][j] = -1;
```
Aqui usamos um `for` dentro de outro para passar por todas as colunas de todas as linhas da matriz. Agora vamos chamar a função `divisao` para descobrir se existe valor `d` que pode ser múltiplo de `n`:
```c
    if (divisao(0, 0, n) == 1) 
      printf("%s\n", d);
    else
      printf("*\n");
```
Se a saída da função for 1 (`divisao(0, 0, n) == 1`), significa que um valor foi encontrado e mostraremos ele na tela. Senão, a resposta deve ser `*`. Com isso concluímos o `int main()`.

Para explicar o funcionamento da função `divisao`, é importante mencionar que a função chama ela mesma. Isso é chamado de [recursão](http://linguagemc.com.br/recursividade-em-c/) e permite que a divisão seja feita independente do tamanho do vetor `s`.

A função `divisao` tem como entradas três valores do tipo `int`:
```c
int divisao(int posicao, int resto, int divisor) {
```
`posicao` representa qual elemento do vetor `s` vai ser analisado, começando sempre pela posição 0. `resto` é o resto da divisão do número guardado em `s` pelo `divisor`. `divisor` é o divisor do cálculo que será sempre o `n` utilizado anteriormente.

Para o funcionamento da função criamos uma variável `i` do tipo `int`. Ela será usada como auxiliar no laço de repetição:
```c
  int i;
```
Como o programa funciona usando recursão, precisamos criar condições de retorno, ou seja, situações em que a chamada da função para e a recursão se encerra:
```c
  if (posicao == strlen(s)) {
    if (resto == 0)
      return 1;
    else
      return 0;
  }
        
  if (verificador[posicao][resto] != -1)
    return verificador[posicao][resto];
```
O primeiro `if` trata da situação em que chegamos na última posição do vetor `s`. Dada essa situação a função retorna 1 se `resto` for 0 ou 0 se for diferente de 0. O segundo caso de parada é se a mesma verificação está sendo feita pela segunda vez. Se isso ocorrer o valor `verificador[posicao][resto]` será 0 e a função retornará 0.

Criadas as condições de retorno, vamos criar a recursão. Nessa função ela pode ocorrer de duas formas, sendo a primeira caso o valor presente em `s[posicao]` não for `?`:
```c
  if (s[posicao] != '?')
    return divisao(posicao+1, (resto*10 + s[posicao] - '0') % divisor, divisor);
```
Se temos `s[posicao]`, não podemos alterá-lo na função, então usamos ele para descobrir o `resto` que servirá de entrada para a recursão. Ao chamar `divisao`, avançamos uma posição (`posicao+1`) e calculamos o novo resto (`(resto*10 + s[posicao] - '0') % divisor`). Aqui multiplicamos por 10 o resto que temos e somamos com o dígito presente em `s[posicao]`. Ao subtrair o valor por `'0'`, obtemos o valor numérico do dígito escrito.

Outra forma de fazer a recursão é mudando o valor de `?` por números de 0 a 9, chamando a função dentro do `if`:
```c
  if (posicao == 0)
    i = 1;
  else
    i = 0;
            
  while (i < 10) {
    if (divisao(posicao+1, (resto*10+i) % divisor, divisor) == 1) {
      d[posicao] = '0' + i;
      return 1;
    }
    i++;
  }
```
Criamos um laço de repetição `while` para mudar o valor determinado como `?` em `s[posicao]`. Para a recursão feita dentro do `if` avançamos uma posição (`posicao+1`) e calculamos o novo resto (`(resto*10+i) % divisor`), aqui multiplicamos por 10 o resto que temos e somamos com o dígito presente em `i`. Sabemos que o primeiro dígito não pode ser 0 então fazemos uma verificação antes do `while`. Dentro do laço, verificamos se o valor `s` é múltiplo de `divisor` e, se for, substituímos o `?` de `d[posicao]` pelo dígito representado por `i` e finalizamos a função retornando 1.

Caso o `while` passe por todos os valores sem encontrar um número múltiplo de `divisor`, atualizamos o `verificador[posicao][resto]` para indicar que passamos por esse caso e não achamos a resposta. Por fim encerramos a função retornando 0:
```c
  verificador[posicao][resto] = 0;
  return 0;
}
```
A recursão feita possibilita o tratamento de todos os `?` presentes no vetor `s`, mudando os valores do vetor da unidade em diante.

##### Para aprender um pouco mais sobre vetores: [Vetores](http://linguagemc.com.br/vetores-ou-arrays-em-linguagem-c/)
##### Para aprender um pouco mais sobre matrizes: [Matrizes](http://linguagemc.com.br/matriz-em-c/)
##### Para aprender um pouco mais sobre a estrutura for: [For](http://linguagemc.com.br/a-estrutura-de-repeticao-for-em-c/)
##### Para aprender um pouco mais sobre a estrutura while: [While](http://linguagemc.com.br/o-comando-while-em-c/)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
