# Problema:
Com o advento dos conceitos da Indústria 4.0 e a evolução da internet das coisas, se tornou simples acompanhar todas as etapas da produção de um produto em uma linha de montagem. De posse das informações, é possível otimizar a produção e diminuir o tempo gasto até que esteja pronta.

Sabendo o tempo gasto em cada estação, e o tempo para trocar entre as duas linhas de montagem, calcule o menor tempo em que é possível realizar a produção de um item.

##### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/2769

# Resolução:

Nesse exercício precisamos fazer um algoritmo capaz de calcular o menor tempo possível para a produção de um item.

Nesse exercício vamos declarar oito variáveis do tipo `int`:
```c
  int N, x1, x2, soma1, soma2, aux1, aux2, i;
```
`N` irá guardar o número de etapas para produzir o item. `x1` e `x2` representam os custos de saída da linha 1 e 2, respectivamente. `soma1` e `soma2` representam o menor custo de produção possível nas linha 1 e 2, respectivamente. `aux1` e `aux2` são variáveis auxiliares que guardarão os custos das etapas anteriores para calcular `soma1` e `soma2`. `i` é uma variável auxiliar para o `for`.

O exercício aborda um caso de leitura em que deve ser lido até o final do arquivo [EOF - End of File](https://pt.wikipedia.org/wiki/EOF). Fazemos a leitura do `N` no `scanf` dentro do `while`:
```c
  while(scanf("%d", &N) != EOF) {
```
Dentro do `while`, fazemos a leitura e comparamos ao EOF, portanto o `while` irá rodar até chegar no final do arquivo. Este é simbolizado pela quebra de linha (`\n`).

Sabendo o número de etapas para a produção, criamos quatro vetores de tamanho `N` do tipo `int`:
```c
    int a1[N], a2[N], t1[N], t2[N];
```
`a1` e `a2` são vetores responsáveis por guardar o custo de cada estação das linhas 1 e 2, respectivamente. `t1` e `t2` representam o custo de transição de uma linha para a outra, sendo `t1` o gasto envolvido na transição da linha 1 para 2 e `t2` o custo de ir da linha 2 para 1.

Agora é hora de escrever os custos de cada etapa de produção e cada transição. os primeiros valores a serem escritos são o custo de entrada para as linhas 1 e 2. Vamos usar um `scanf`:
```c
    scanf("%d %d", &t1[0], &t2[0]);
```
Um único `scanf` pode ler mais de um valor se usarmos mais de um `%d`. Os valores de entrada ficarão guardados em `t1[0]` e `t2[0]`, respectivamente.

Para escrever os outros custos usamos o laço de repetição `for`. Aqui preenchemos os vetores `a1`, `a2`, `t1` e `t2`:
```c
    for(i = 0; i < N; i++) {
      scanf("%d", &a1[i]);
    }

    for(i = 0; i < N; i++) {
      scanf("%d", &a2[i]);
    }

    for(i = 1; i < N; i++) {
      scanf("%d", &t1[i]);
    }

    for(i = 1; i < N; i++) {
      scanf("%d", &t1[i]);
    }
```
Por fim, escrevemos os valores de `x1` e `x2`, que são os custos de saída de cada linha:
```c
    scanf("%d %d", &x1, &x2);
```
Agora temos que descobrir o valor de `soma1` e `soma2`. Esse valor será o custo da entrada na linha e da primeira etapa dessa linha:
```c
    soma1 = t1[0]+a1[0];
    soma2 = t2[0]+a2[0];
```
Vamos criar outro laço de repetição. Aqui calcularemos a menor soma de custos em cada linha e a primeira parte é guardar as somas anteriores em `aux1` e `aux2`:
```c
    for(i = 1; i < N; i++) {
      aux1 = soma1;
      aux2 = soma2;
```
Como vamos calcular o menor custo possível, temos que usar os valores obtidos nas etapas anteriores para fazer a soma. Para atualizar `soma1` e `soma2` verificamos o menor valor possível nessa etapa:

```c
      if (aux1+a1[i] > aux2+t2[i]+a1[i])
        soma1 = aux2+t2[i]+a1[i];
      else
        soma1 += a1[i];
      
      if (aux2+a2[i] > aux1+t1[i]+a2[i])
        soma2 = aux1+t1[i]+a2[i];
      else
        soma2 += a2[i];
    }
```
Para a verificação usamos um `if`. Nele verificamos se o menor custo é mudar de linha e realizar a próxima etapa na outra linha (`aux2+t2[i]+a1[i]` e `aux1+t1[i]+a2[i]`) ou se é menos custoso manter a produção na mesma linha (`aux1+a1[i]` e `aux2+a2[i]`). Descobrindo o menor valor somamos ele a `soma1` ou `soma2`. 

Feitas as somas, resta saber qual o menor custo obtido. Aqui usaremos outro `if` levando em consideração o custo de saída de cada linha representados por `x1` e `x2`:
```c
    if (soma1+x1 < soma2+x2) {
      soma1 += x1;
      printf("%d\n", soma1);
    }
    else {
      soma2 += x2;
      printf("%d\n", soma2);
    }
  }
```
Sabendo qual é o menor custo de produção, incrementamos o custo de saída à soma e mostramos o valor na tela usando `printf`.

##### Para aprender um pouco mais sobre vetores: [Vetores](http://linguagemc.com.br/vetores-ou-arrays-em-linguagem-c/)
##### Para aprender um pouco mais sobre a estrutura for: [For](http://linguagemc.com.br/a-estrutura-de-repeticao-for-em-c/)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
