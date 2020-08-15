# Problema:

Um novo jogo chamado Ímpar, Par ou Roubo (IPR) está se tornando muito popular. Esse jogo surgiu quando alguns amigos estavam sem conexão com a internet, sem celular, sem computador e bastante desocupados. O jogo está tão popular que irá acontecer um campeonato mundial de IPR e cada país do mundo irá escolher um representante para competir.

O jogo funciona da seguinte forma: dois jogadores participam, o jogador 1 escolhe entre par ou ímpar, então cada jogador escolhe um inteiro positivo, se a soma desses números for par e o jogador 1 tiver escolhido par então o jogador 1 ganha, se a soma for ímpar o jogador 2 ganha. Caso o jogador 1 tivesse escolhido ímpar ele ganharia se a soma fosse ímpar, caso a soma fosse par o jogador 2 ganharia. Nada de diferente de um jogo de par ou ímpar convencional, correto?

A diferença do jogo é que o jogador 1 pode roubar e assim assegurar sua vitória independentemente do resultado do jogo de ímpar ou par convencional, já o jogador 2 pode ou não acusar o jogador 1 de roubo. Com essas adições no jogo se o jogador 1 roubar e o jogador 2 acusar o roubo então o jogador 2 ganha, caso o jogador 2 não acuse o roubo e o jogador 1 roubar então o jogador 1 ganha, caso o jogador 2 acuse o roubo, mas o jogador 1 não tiver roubado então o jogador 1 ganha, se o jogador 1 não roubar e o jogador 2 não acusar o roubo o jogo segue como descrito anteriormente.

Você foi contratado pela OIIPR (Organização Internacional de Ímpar, Par ou Roubo) para desenvolver um programa que dada a escolha do jogador 1 entre par ou ímpar, os números escolhidos como jogada e as ações dos jogadores (roubo/acusação) mostre quem foi o vencedor.

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/2059

# Resolução

O exercício é meio confuso em sua descrição, porém a ideia ao final é saber organizar os `if`. O exercício trabalha com várias condições usando a ideia de que a variável é verdadeira quando o valor dela é 1 e falsa quando é 0, ou como chamamos na computação de [Boolean](https://pt.wikipedia.org/wiki/Boolean#:~:text=Chamado%20boolean%20em%20homenagem%20a,das%20operações%20da%20álgebra%20booliana.).

Para isso iniciamos declarando as variáveis que serão utilizadas:

```c
        int p, j1, j2, r, a, vencedor, soma;
```
`p` representa a escolha do jogador 1 (se `p = 1` então o jogador 1 escolheu par, se `p = 0` então o jogador 1 escolheu ímpar). Os valores `j1, j2`, representam respectivamente o número escolhido pelo jogador 1 e pelo jogador 2. `r` representa se o jogador 1 roubou (se `r` = 1 então o jogador 1 roubou, se `r = 0` então o jogador 1 não roubou), `a` representa se o jogador 2 acusou o roubo (se `a = 1` então o jogador 2 acusou o jogador 1 de roubo, se `a = 0` então ele não acusou o jogador 1 de roubo). `vencedor` variável que ira armazenar 1 caso o jogador 1 venceu e 2 para o jogador 2 e `soma` é a variável que armazena o valor da soma das jogadas dos jogadores 1 e 2.

Fazemos a leitura das variáveis no `scanf`:

```c
        scanf("%d %d %d %d %d", &p, &j1, &j2, &r, &a);
```

Fazemos a soma das jogadas dos jogadores 1 e 2 e atribuímos a variável `soma`:

```c
        soma = j1 + j2;
```

Criamos os `if` responsáveis pelas verificações, explicarei cada um abaixo usando a ordem deles de cima pra baixo, portando `if((soma%2==0 && p==1) || (soma%2==1 && p==0))` é o primeiro:

```c
        if((soma%2==0 && p==1) || (soma%2==1 && p==0)) 
                vencedor = 1;
        else 
                vencedor = 2;
        if((r==1 && a==0) || (r==0 && a==1)) 
                vencedor = 1;
        else if(r==1 && a==1) 
                vencedor=2;
```
**1º** `if`: Fazemos a verificação se a rodada saio par e(`&&`) verificamos se o jogador 1 excolheu par, ou(`||`) se a jogada resultou em ímpar e(`&&`) o jogador 1 escolheu ímpar.
Portanto a variável `vencedor` recebe 1, jogador 1 ganhou. O seu `else` será o inverso, por exemplo jogador 1 escolher par e a `soma` for um valor ímpar.

**2º** `if`: Será verificado a condição do jogar 1 roubar `r=1` e(`&&`) o jogador 2 não acusar `a=0`, ou(`||`) o jogador 1 não roubar `r=0` e o jogador 2 acusá-lo `a=1`, portanto resultando na vitória do jogar 1 `vencedor=1`. E o seu `else if` é a condição onde o jogador 1 rouba `r=1` e o jogador 2 acusa ele `a=1`, pego no flagra!

Terminamos printando o resultado:

```c
        printf("Jogador %d ganha!\n", vencedor);
```
##### Para aprender um pouco mais sobre operadores lógicos: [Operadores Lógicos](https://pt.wikipedia.org/wiki/Operadores_em_C_e_C%2B%2B)
##### Para aprender um pouco mais sobre variáveis booleanas: [Boolean](https://pt.wikipedia.org/wiki/Boolean#:~:text=Chamado%20boolean%20em%20homenagem%20a,das%20operações%20da%20álgebra%20booliana.)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para petbcc.ufscar@gmail.com