# Problema:

Pedra-papel-tesoura-lagarto-Spock é uma expansão do clássico método de seleção em jogo de pedra-papel-tesoura. Atua sob o mesmo princípio básico, mas inclui outras duas armas adicionais: o lagarto (formado pela mão igual a uma boca de fantoche) e Spock (formada pela saudação dos vulcanos em Star Trek). Isso reduz as chances de uma rodada terminar em um empate. O jogo foi inventado por Sam Kass e Karen Bryla, como "Rock Paper Scissors Lizard Spock". As regras de vantagem são as seguintes:

Tesoura corta papel

Papel cobre pedra

Pedra derruba lagarto

Lagarto adormece Spock

Spock derrete tesoura

Tesoura prende lagarto

Lagarto come papel

Papel refuta Spock

Spock vaporiza pedra

Pedra quebra tesoura

Um dia, dois amigos, Rajesh e Sheldon, decidiram apostar quem pagaria um almoço para o outro, com esta brincadeira. Sua missão será fazer um algoritmo que, baseado no que eles escolherem, informe quem irá ganhar ou se dará empate.

**Problema Completo**: https://www.urionlinejudge.com.br/judge/pt/problems/view/1873

# Resolução:

Para a resolução deste problema, além da biblioteca padrão `stdio.h`, é necessário incluir a biblioteca `string.h`.

```c
#include <stdio.h>
#include <string.h>
```

Após informar as bibliotecas, iniciamos o nosso algoritmo. Primeiramente, declaramos uma variável do tipo inteiro chamada `c`, pois é dito na entrada que haverá diversos casos de teste, e o primeiro número a ser lido será um inteiro C, representando a quantidade de casos de teste. Em seguida fazemos a leitura do número de casos testes, armazenando nesta variável `c` com o comando `scanf()`. Também declaramos as variáveis do tipo inteiro `i` e `comp` que serão utilizadas posteriormente.

Além destas, são declaradas as variáveis do tipo caractere `rajesh[15]` e `sheldon[15]` para representar a escolha de Rajesh e de Sheldon, respectivamente.

E ainda são declaradas as váriáveis do tipo caractere `pedra[] = "pedra"`, `papel[] = "papel"`, `tesoura[] = "tesoura"`, `lagarto[] = "lagarto"`, `spock[] = "spock"` na qual em cada uma delas é atribuida uma palavra que servirá para posterior comparação no decorrer do problema.

```c
int main() {

  char rajesh[15], sheldon[15];
  char pedra[] = "pedra", papel[] = "papel", tesoura[] = "tesoura", lagarto[] = "lagarto", spock[] = "spock";
  int c, i, comp;

  scanf("%d", &c);

    /**
     * restante do código aqui (informado abaixo)
    **/
    
  return 0;
}
```

É necessário fazer uma estrutura `for` para que haja vários casos testes. Após, para as duas variáveis do tipo caractere `rajesh[15]` e `sheldon[15]` é feita uma leitura com o comando `scanf()`, variáveis estas que passam a armazenar a escolha de Rajesh e de Sheldon, respectivamente. Em seguida, com o comando `strcmp()` as duas strings (escolhas de Rajesh e Sheldon) são comparadas.

```c
for(i = 0; i < c; i++) {
    
    scanf("%s %s", rajesh, sheldon);
    
    comp = strcmp(rajesh, sheldon);

    /**
     * restante do código aqui (informado abaixo)
    **/

}
```

Na sequência é feita uma estrutura `if` para o empate, encadeada de vários `else if` na qual em cada uma delas é definida uma determinada condição a vitória.

O `if` analiza através da váriavel `comp` se a escolha de Rajesh e Sheldon foram iguais, e em caso afirmativo, a frase exibida na tela é 'empate' através do comando `printf()`.

Caso o empate não ocorra, a estrutura encadeada `else if` analisa com o comando `strcmp()` juntamente com os operadores lógicos `AND (&&)` e `OR (||)` todos os possíveis resultado e diz qual foi a escolha vencedora, se Rajesh venceu a frase exibida na tela é 'rajesh' através do comando `printf()`, e se Sheldon venceu a frase exibida na tela é 'sheldon' através do comando `printf()`.

```c
    if (comp == 0) {
        printf("empate\n");
    } else if ((strcmp(rajesh, tesoura) == 0) && ((strcmp(sheldon, papel) == 0) || (strcmp(sheldon, lagarto) == 0))) {
        printf("rajesh\n");
    } else if ((strcmp(sheldon, tesoura) == 0) && ((strcmp(rajesh, papel) == 0) || (strcmp(rajesh, lagarto) == 0))) {
        printf("sheldon\n");
    } else if ((strcmp(rajesh, papel) == 0) && ((strcmp(sheldon, pedra) == 0) || (strcmp(sheldon, spock) == 0))) {
        printf("rajesh\n");
    } else if ((strcmp(sheldon, papel) == 0) && ((strcmp(rajesh, pedra) == 0) || (strcmp(rajesh, spock) == 0))) {
        printf("sheldon\n");
    } else if ((strcmp(rajesh, pedra) == 0) && ((strcmp(sheldon, lagarto) == 0) || (strcmp(sheldon, tesoura) == 0))) {
        printf("rajesh\n");
    } else if ((strcmp(sheldon, pedra) == 0) && ((strcmp(rajesh, lagarto) == 0) || (strcmp(rajesh, tesoura) == 0))) {
        printf("sheldon\n");
    } else if ((strcmp(rajesh, lagarto) == 0) && ((strcmp(sheldon, spock) == 0) || (strcmp(sheldon, papel) == 0))) {
        printf("rajesh\n");
    } else if ((strcmp(sheldon, lagarto) == 0) && ((strcmp(rajesh, spock) == 0) || (strcmp(rajesh, papel) == 0))) {
        printf("sheldon\n");
    } else if ((strcmp(rajesh, spock) == 0) && ((strcmp(sheldon, tesoura) == 0) || (strcmp(sheldon, pedra) == 0))) {
        printf("rajesh\n");
    } else if ((strcmp(sheldon, spock) == 0) && ((strcmp(rajesh, tesoura) == 0) || (strcmp(rajesh, pedra) == 0))) {
        printf("sheldon\n");
    }
```

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/),
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
