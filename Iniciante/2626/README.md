# Problema:
Os garotos resolveram adotar uma estratégia para dividir as sessões de RPG igualmente entre os assuntos, de modo que eles possam especular cada um ao máximo e chegarem a conclusões astronômicas. Eles irão jogar “pedra, papel e tesoura” para decidir o assunto da sessão de hoje, e então irão alternar os assuntos nas próximas sessões. Dadas as jogadas de Dodô, Leo e Pepper, nesta ordem, você deve determinar o assunto da sessão de hoje.
Sendo que o assunto será:
- Dodo ganha : "Os atributos dos monstros vao ser inteligencia, sabedoria..." 
- Leo ganha : "Iron Maiden's gonna get you, no matter how far!"
- Pepper ganha : "Urano perdeu algo muito precioso..." 
- Empate : "Putz vei, o Leo ta demorando muito pra jogar..." 
 
##### Link do problema: https://www.urionlinejudge.com.br/judge/pt/problems/view/2626
 
# Resolução:
O exercício consiste em ler as jogadas do Dodô, Leo e Pepper, respectivamente; e imprimir o assunto com base no vencedor.
Lembrando que:
- Pedra ganha de Tesoura
- Tesoura ganha de Papel
- Papel ganha de Pedra

Primeiro devemos incluir a biblioteca `string.h` para termos a função de comparar `strings`.

```c
#include <string.h>
```

Antes de iniciarmos nosso `main()` vamos criar uma função `ganhar()` que retorna se um jogador **ganhou** do outro ou não; no caso do nosso código, se o `ganha` ganha ou não.
Para conferir se o jogador cumpre os requisitos de ganhar do outro iremos utilizar a função `strcmp()`; ela compara as duas strings passadas e se elas forem iguais ela retorna **0**, por isso as duas comparações devem ser iguais a **0** para o jogador ganhar.

```c
    int ganhar(char ganha[10], char n_ganha[10])
{
    if (strcmp(ganha, "pedra") == 0 && strcmp(n_ganha, "tesoura") == 0)
        return 1;
    if (strcmp(ganha, "papel") == 0 && strcmp(n_ganha, "pedra") == 0)
        return 1;
    if (strcmp(ganha, "tesoura") == 0 && strcmp(n_ganha, "papel") == 0)
        return 1;
    return 0;
}
```

Dentro no nosso `main` vamos começar instanciando 3 vetores do tipo `char`, que irão guardar as jogadas dos garotos.

```c
    char dodo[10], leo[10], pepper[10];
```

Agora iremos utilizar um `while()` para passar por todas as partidas, lendo o que cada um colocou por partida, ou seja, lendo 3 valores de cada vez.
Um único `scanf` pode ler mais de um valor se usarmos mais de um `%d`. Dentro do `while`, fazemos a leitura e comparamos ao `EOF`, portanto o `while` irá rodar até chegar no final do arquivo.

Obs: Como vamos ler um vetor completo de `char`, iremos ler utilizando `%s`.

```c
    while (scanf("%s %s %s", dodo, leo, pepper) != EOF)
```

Dentro do `while` iremos utilizar a função que criamos para verificar se um determinado jogador ganhou dos outros dois, pois quando são três jogadores um só ganha a partida se ele ganha dos outros dois, caso contrário a rodada será dada como empate.
Caso a condição para vencer seja satisfeita iremos imprimir a respectiva mensagem do vencedor, caso contrário imprima a mensagem de empate.

```c
    if (ganhar(dodo, leo) && ganhar(dodo, pepper))
            printf("Os atributos dos monstros vao ser inteligencia, sabedoria...\n");
        else if (ganhar(leo, dodo) && ganhar(leo, pepper))
            printf("Iron Maiden's gonna get you, no matter how far!\n");
        else if (ganhar(pepper, dodo) && ganhar(pepper, leo))
            printf("Urano perdeu algo muito precioso...\n");
        else
            printf("Putz vei, o Leo ta demorando muito pra jogar...\n");
```

##### Para aprender um pouco mais sobre a biblioteca *string.h*: [String](http://linguagemc.com.br/a-biblioteca-string-h/)
 
Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com

