# Problema:
No tower defense Magic and Sword, o jogador pode lançar magias de área para derrotar as unidades inimigas. As magias são elementais: fogo, água, ar e terra, e a região afetada é determinada por um círculo cujo raio depende do nível da magia. 

As unidades inimigas são delimitadas por um retângulo de largura w e altura h, com canto inferior esquerdo posicionado no ponto (x0, y0). O inimigo sofrerá dano caso seu retângulo delimitador tenha qualquer intercessão com a área deﬁnida pelo círculo da magia.

Dada a posição e o retângulo delimitador da unidade inimiga, o centro da explosão e o identiﬁcador e o nível da magia, determine o dano sofrido pela unidade. Caso a unidade esteja fora do alcance da magia, o dano sofrido é igual a zero.

##### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/2632

# Resolução:
Esse exercício é uma aplicação do cálculo de [distância entre dois pontos](https://brasilescola.uol.com.br/matematica/distancia-entre-dois-pontos.htm). Aqui temos uma área em forma de retângulo e um círculo e precisamos saber se em algum ponto o círculo passa pela área retangular.

Nesse exercício precisamos de quatro variáveis do tipo `int`, onze do tipo `float` e uma do tipo `char`:
```c
  int t, level, dano, i;
  float w, h, x, y, xc, yc, raio;
  float distx, disty, pontomediox, pontomedioy;
  char magia[10];
```
`t` representa o número de testes. `level` vai ser o nível da magia usada. `dano` indica o dano causado pela magia. `i` é uma variável auxiliar para o `for`. `w` e `h` representam a altura e largura do retângulo, respectivamente. `x` e `y` são as coordenadas do ponto inferior esquerdo do retângulo. `xc` e `yc` representam as coordenadas do centro do círculo. `raio` é o raio do círculo. `distx` e `disty` são as coordenadas do ponto do retângulo que está mais próximos do centro do círculo. `pontomediox` e `pontomedioy` são as coordenadas do ponto médio do retângulo. Por fim, `magia` é um vetor de caracteres que vai guardar o nome do elemento da magia.

Pra começar o exercício fazemos a leitura do `t` no `scanf` para determinar quantos testes vão ser realizados:
```c
  scanf("%d", &t);
```
Sabendo o número de testes, fazemos um `for` para ler os dados desse teste:
```c
  for(i=0;i<t;i++) {
    scanf("%f %f %f %f", &w, &h, &x, &y);
    scanf("%s %d %f %f", magia, &level, &xc, &yc);
```
No primeiro `scanf` lemos as informações do retângulo, sendo elas a altura (`w`), largura (`h`), posição x (`x`) e posição y (`y`). No segundo lemos os dados do círculo, sendo elas o elemento da magia (`magia`), nível (`level`), posição x (`xc`) e posição y (`yc`).

Precisamos descobrir o `dano` e `raio` da magia que será usada. Isso pode ser obtido com as variáveis `magia` e `level`. Usamos a função `strcmp` da biblioteca [string.h](http://linguagemc.com.br/a-biblioteca-string-h/) no `if` para descobrir qual o elemento da magia e, dentro dele, usamos outro `if` para determinar o raio do círculo de acordo com o `level`:
```c
    if (strcmp(magia, "fire") == 0) {
      dano = 200;
      if (level == 1)
        raio = 20;
      else if (level == 2)
        raio = 30;
      else
        raio = 50;
    }
        
    else if (strcmp(magia, "water") == 0) {
      dano = 300;            
      if (level == 1)
        raio = 10;
      else if (level == 2)
        raio = 25;
      else
        raio = 40;
    }
        
    else if (strcmp(magia, "earth") == 0) {
      dano = 400;
      if (level == 1)
         raio = 25;
      else if (level == 2)
         raio = 55;
      else
         raio = 70;
    }
        
    else if (strcmp(magia, "air") == 0) {
      dano = 100;
      if (level == 1)
        raio = 18;
      else if (level == 2)
        raio = 38;
      else
        raio = 60;
    }
```
Sabendo o `raio` e o `dano`, vamos calcular a distância entre o retângulo e o círculo para descobrir se a magia acertou o inimigo. Para isso precisamos atribuir valores a `distx`, `disty`, `pontomediox` e `pontomedioy`:
```c
    distx = 0;
    disty = 0;
    pontomediox = x + w/2;
    pontomedioy = y + h/2;
```
`distx` e `disty` serão 0 no momento para calcular o ponto mais próximo entre o retângulo e o círculo. `pontomediox` e `pontomedioy` serão os pontos médios da largura e da altura, respectivamente. Agora calcularemos o ponto de coordenadas `distx` e `disty`:
```c
    if (pontomediox - xc >= 0) {
      if (pontomediox - xc - w/2 > 0)
        distx = pontomediox - xc - w/2;
    }
    else {
      if (-pontomediox + xc - w/2 > 0)
        distx = -pontomediox + xc - w/2;
    }
        
    if (pontomedioy - yc >= 0) {
      if (pontomedioy - yc - h/2 > 0)
        disty = pontomedioy - yc - h/2;
    }
    else {
      if (-pontomedioy + yc - h/2 > 0)
        disty = -pontomedioy + yc - h/2;
    }
```
Para calcular `distx` verificamos com um `if` se `pontomediox - xc` é positivo para poder usar o valor positivo dessa subtração. Feito isso comparamos `pontomediox - xc - w/2` com 0 e, se for maior, atualizamos `distx`, senão o valor se mantém 0. O mesmo processo se repete para `disty`.

Agora que temos as coordenadas do ponto do retângulo mais próximo ao círculo, vamos calcular a distância deles usando o cálculo da distância entre dois pontos:
```c
    if (raio * raio >= distx * distx + disty * disty)
      printf("%d\n", dano);
    else
      printf("0\n");
  }
```
A fórmula original utiliza a raiz quadrada da distância entre (`distx`,`disty`) e (0,0). No entanto, se elevarmos a distância `raio` ao quadrado a raiz não é necessária. Se `raio` ao quadrado for maior ou igual à soma de `distx` ao quadrado e `disty` ao quadrado (`raio * raio >= distx * distx + disty * disty`), isso quer dizer que parte do círculo está dentro do retângulo e a magia acertou, então mostramos na tela o valor do `dano`. Se não acertou (`else`), a resposta dada é 0.

##### Para aprender um pouco mais sobre a estrutura for: [For](http://linguagemc.com.br/a-estrutura-de-repeticao-for-em-c/)
##### Para aprender um pouco mais sobre vetor de caracteres: [Strings](http://linguagemc.com.br/string-em-c-vetor-de-caracteres/)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
