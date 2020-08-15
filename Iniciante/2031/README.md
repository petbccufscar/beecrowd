# Problema:   
Pedra, Papel, Ataque Aéreo é um jogo infantil muito popular, em que duas ou mais crianças formam um círculo e fazem gestos com a mão na tentativa de obter a vitória. As regras são surpreendentemente complexas para um jogo de crianças, mas mesmo assim é bastante popular por todo o mundo.
As partidas são muito simples. Os jogadores podem escolher entre o sinal de uma Pedra (o punho), o sinal de um Papel (a palma aberta), e o sinal para o Ataque Aéreo (igual o do Papel, mas com apenas o polegar e o mindinho estendidos).

Uma partida, com dois jogadores, possuem as seguintes regras para se definir um vencedor:

* Ataque Aéreo vs. Pedra: Neste caso, o jogador com o Ataque Aéreo derrota o jogador com a Pedra, por razões óbvias.
* Pedra vs. Papel: Neste caso, o jogador com a Pedra derrota o com Papel, porque a Pedra machuca muito mais.
* Papel vs. Ataque Aéreo: Aqui o Ataque Aéreo ganha, porque Ataque Aéreo sempre ganha e o Papel é patético.
* Papel vs. Papel: Nesta variação, ambos os jogadores ganham, porque o Papel é inútil e ninguém que enfrenta o Papel pode perder.
* Pedra vs. Pedra: Para este caso não há ganhador, porque depende do que os jogadores decidem fazer com a Pedra e normalmente não fazem nada.
* Ataque Aéreo vs. Ataque Aéreo: Quando isto acontece, todos os jogadores perdem, devido a Aniquilação Mútua.

Sua tarefa é escrever um programa que, dada as escolhas de dois jogadores, informe quem venceu o jogo.

**Problema Completo**: https://www.urionlinejudge.com.br/judge/pt/problems/view/2031

# Resolução:

Para a resolução deste problemas iremos precisar importar uma biblioteca com o nome de `<string.h>` com ela iremos trabalhar com strings, na forma de uma cadeia de caracteres, usaremos para armazenar o valor informado pelos jogadores.
```c
#include <string.h>
```
Nessa biblioteca temos a função `strcmp` a qual é usado da seguinte forma: ` strcmp(string1, string2); ` ela compara o conteúdo de duas strings e como retorno dessa função podemos ter

* 0: conteúdo das strings são iguais.
* < 0: conteúdo da string1 é menor do que string2.
* \> 0: conteúdo da string1 é maior do que string2.


Agora explicado a função dessa biblioteca adicional que importamos, podemos começar com a resolução do problema, para isso realizamos as declarações das variáveis, dentre essas temos `char jogador1[10]` que indica ser uma variável do tipo CHAR com tamanho de 10 caracteres, ou seja uma cadeia de caracteres (uma string). Assim como realizamos a leitura de `N` que será o números de casos de teste que nosso programa irá verificar.
```c
int N, aux;
char jogador1[10], jogador2[10];

scanf("%d", &N);
```


Para a repetição iremos utilizar a estrutura `for` realizando `N` iterações, nestas iremos realizar a leitura das duas strings que serão passadas, caracterizando os golpes dos jogadores.
```c
for(aux = 0; aux < N; aux++){
	scanf("%s %s", jogador1, jogador2);
```


Dentro de nosso `for` temos vários condicionais `if` que irão abordar todas as jogadas possíveis, para explicação trataremos de apenas uma. Nesse caso escolhido é verificado se a string contida em `jogador1` é igual a "pedra" e se a string contida em `jogador2` é igual a "papel", caso for positivo (pois a `strcmp` retorna 0 caso forem iguais) iremos imprimir na tela que o jogador 1 venceu pois segundo o problema, o jogador que escolheu pedra ganha por causar muito dano ao papel.
```c
if (strcmp(jogador1, "pedra") == 0 && strcmp(jogador2, "papel") == 0)
			printf("Jogador 1 venceu\n");
```


##### Para revisar sobre a biblioteca: [<string.h>](http://linguagemc.com.br/a-biblioteca-string-h/)
    
Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
