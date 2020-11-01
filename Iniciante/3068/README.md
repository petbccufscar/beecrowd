# Problema:
Zé Felício é um fazendeiro que adora astronomia e descobriu um portal na Internet que fornece uma lista das posições onde caíram meteoritos.Com base nessa lista, e conhecendo a localização de sua fazenda, Zé Felício deseja saber quantos meteoritos caíram dentro de sua propriedade. Ele precisa de sua ajuda para escrever um programa de computador que faça essa verificação automaticamente.

São dados:

• uma lista de pontos no plano cartesiano, onde cada ponto corresponde à posição onde caiu um meteorito;

• as coordenadas de um retângulo que delimita uma fazenda. As linhas que delimitam a fazenda são paralelas aos eixos cartesianos. Sua tarefa é escrever um programa que determine quantos meteoritos caíram dentro da fazenda (incluindo meteoritos que caíram exatamente sobre as linhas que delimitam a fazenda).

##### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/3068

# Resolução:

O objetivo do exercício é escrever um código que responda quantos meteoros caíram na fazenda.

Nesse exercício vamos declarar dez variáveis do tipo `int`:
```c
  int x1, y1, x2, y2, n, x, y, numTestes, contador, i;
```
`x1` e `y1` são as coordenadas do canto superior esquerdo do retângulo. `x2` e `y2` são as coordenadas do canto inferior direito do retângulo. `n` indica quantos meteoros caíram no teste. `x` e `y` representam as coordenadas onde caiu o meteoro. `numTestes` representa o número do teste que está sendo mostrado. `contador` é a variável responsável por guardar o número de meteoros que caíram na fazenda em um teste. `i` é uma variável auxiliar para o `for`.

Para começar vamos igualar `numTestes` a 0, pois nenhum teste foi feito. Também criaremos um laço de repetição `while` para verificar se as coordenadas da fazenda não são 0. Se uma delas for 0, o programa deve ser encerrado.
```c
  numTestes = 0;
  while (!(x1 == 0 && y1 == 0 && x2 == 0 && y2 == 0)) {
```
A primeira coisa a se fazer é ler `x1`, `y1`, `x2` e `y2`. Para isso vamos usar o `scanf`:
```c
    scanf("%d", &x1);
    scanf("%d", &y1);
    scanf("%d", &x2);
    scanf("%d", &y2);
```
Sabendo as coordenadas da fazenda, igualamos `contador` a 0 para iniciar a contagem dos meteoros. Vale ressaltar que a contagem só será feita se nenhuma das coordenadas for 0:
```c
    contador = 0;
    if (!(x1 == 0 && y1 == 0 && x2 == 0 && y2 == 0)) {
      scanf("%d", &n);
```
A primeira coisa a se fazer para começar a contagem é saber quantos meteoros caíram naquele teste. Depois de ler o valor `n` criamos um laço de repetição e para cada meteoro lemos as coordenadas dele e comparamos com as coordenadas da fazenda:
```c
      for(i=0;i<n;i++) {
        scanf("%d", &x);
        scanf("%d", &y);
        if (x >= x1 && x <= x2) {
          if (y <= y1 && y >= y2) {
            contador++;
          }
        }
      }
```
Para comparar a coordenada onde o meteoro caiu com as coordenadas da fazenda, utilizamos dois `if`. No primeiro comparamos apenas os valores de `x`, `x1` e `x2` e no segundo comparamos `y`, `y1` e `y2`. Se o valor de `x` estiver entre `x1` e `x2` verificamos `y`, e se `y` estiver entre `y1` e `y2`, incrementamos o contador.

Depois de fazer as comparações com todos os meteoros, incrementamos `numTestes` e mostramos na tela o resultado usando `printf`:
```c
      numTestes++;
      printf("Teste %d\n%d\n", numTestes, contador);
    }
  }
```
O resultado deve mostrar o número do teste e quantos meteoros caíram na fazenda.

##### Para aprender um pouco mais sobre a estrutura for: [For](http://linguagemc.com.br/a-estrutura-de-repeticao-for-em-c/)
##### Para aprender um pouco mais sobre a estrutura while: [While](http://linguagemc.com.br/o-comando-while-em-c/)
##### Para aprender um pouco mais sobre o uso de incremento: [Incremento](http://linguagemc.com.br/operadores-de-auto-incremento-e-auto-decremento/)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
