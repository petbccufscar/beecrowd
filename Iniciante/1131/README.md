# Problema:

Escreva um programa para ler o número de gols marcados pelo Inter e pelo Grêmio em um GRENAL. Logo após escrever a mensagem "Novo grenal (1-sim 2-nao)" e solicitar uma resposta. Se a resposta for 1, o algoritmo deve ser executado novamente solicitando o número de gols marcados pelos times em uma nova partida, caso contrário deve ser encerrado imprimindo:

- Quantos GRENAIS fizeram parte da estatística.
- O número de vitórias do Inter.
- O número de vitórias do Grêmio.
- O número de Empates.
- Uma mensagem indicando qual o time que venceu o maior número de GRENAIS (ou "Nao houve vencedor", caso termine empatado).

##### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/1131

# Resolução:

O objetivo desse exercício é comparar uma série de resultados de jogos de futebol entre Inter e Grêmio e mostrar quem venceu mais vezes. Para isso vamos definir o vencedor de cada partida e comparar o número de vitórias de cada time.

Vamos precisar de 7 variáveis do tipo `int` nesse exercício:
```c
    int gol_gre, gol_int, v_gre, v_int, e, jogos, x;
```
As primeiras variáveis `gol_gre` e `gol_int` representam a quantidade de gols que Grêmio e Inter fizeram em um mesmo jogo, respectivamente. `v_gre` e `v_int` representam o número de vitórias de cada time, `e` representa o número de empates, `jogos` o número total de jogos disputados e `x` é a variável que será usada para saber se haverá outro jogo.

A primeira coisa a se fazer para começar o algoritmo é igualar `v_gre`, `v_int`, `e` e `jogos` a 0:
```c
    v_gre = 0;
    v_int = 0;
    e = 0;
    jogos = 0;
```

Como não sabemos quantos jogos serão realizados, usaremos a função `do... while`, e dentro desse laço de repetição colocamos o número de gols que cada time fez em um único jogo:
```c
    do {
      scanf("%d%d", &gol_int, &gol_gre);
```
É possível inserir mais de um dado dentro do mesmo `scanf` usando vários `%d`. Após ler os valores das duas variáveis, vamos comparar os dados e ver quem venceu a partida. Em uma partida de futebol, vence o time que marcar mais gols. Sendo assim, comparamos os valores `gol_int` e `gol_gre` e, se o valor de `gol_int`for maior (`gol_int > gol_gre`), significa vitória do Inter:
```c
      if (gol_int > gol_gre)
        v_int++;
```
Se o valor de `gol_gre`for maior (`gol_int < gol_gre`), significa vitória do Grêmio:
```c
      else if (gol_int < gol_gre)
        v_gre++;
```
Quando o número de gols é igual, significa que houve empate:
```c
      else
        e++;
```
Dentro de cada `if` há um símbolo `++` depois de uma variável. Esse símbolo é usado para somar o valor da variável em 1.
```c
      jogos++;
```
Independente do número de gols de cada partida, a variável `jogos` sempre vai ser incrementado pois cada leitura de dados feita com `scanf` representa um jogo.

Depois de atualizar o número de vitórias e empates, devemos perguntar se terá outro jogo. Aqui usamos a função `printf` para mostrar a mensagem `Novo grenal (1-sim 2-nao)` na tela:
```c
      printf("Novo grenal (1-sim 2-nao)\n");
      scanf("%d", &x);
    } while (x == 1);
```
O `\n` no fim serve para pular uma linha na tela depois de mostrar o texto. Depois da mensagem a variável `x` será lida e, se ela for 1 (`x == 1`), significa que haverá outro jogo e o primeiro `scanf` vai se repetir. Caso `x` seja 2. O programa sai do laço de repetição criado pelo `do` no começo de código.

Finalizada a obtenção de dados dos jogos, vamos iniciar a apresentação dos resultados:
```c
   printf("%d grenais\n", jogos);
   printf("Inter:%d\n", v_int);
   printf("Gremio:%d\n", v_gre);
   printf("Empates:%d\n", e);
```
Com `printf`, estamos indicando o número total de jogos, o número de vitórias de cada time e o número de empates que aconteceram. A mensagem final deve mostrar quem ganhou mais.

Para saber quem venceu mais, comparamos o número de vitórias do Inter (`v_int`) e do Grêmio (`v_gre`) usando `if` e `else`. Se `v_int` for maior (`v_int > v_gre`), vai aparecer na tela a mensagem `Inter venceu mais`:
```c
   if (v_int > v_gre)
       printf("Inter venceu mais\n");
```
Se `v_gre` for maior (`v_int < v_gre`), aparecerá `Gremio venceu mais`:
```c
   else if (v_int < v_gre)
       printf("Gremio venceu mais\n");
 ```
Caso os dados sejam iguais, o texto mostrado vai ser `Nao houve vencedor`:
```c
   else 
       printf("Nao houve vencedor\n");
```

##### Para aprender um pouco mais sobre if e else: [Estruturas de decisão](http://linguagemc.com.br/estrutura-de-decisao-if-em-linguagem-c/)
##### Para aprender um pouco mais sobre o operador ++: [Auto-incremento](http://linguagemc.com.br/operadores-de-auto-incremento-e-auto-decremento/)
##### Para aprender um pouco mais sobre a estrutura do.. while: [Do... While](http://linguagemc.com.br/comando-do-while/)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para petbcc.ufscar@gmail.com
