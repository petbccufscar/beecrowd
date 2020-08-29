# Problema:

Por ser bastante habilidoso, os vídeos de suas jogadas (seus famosos gameplays) vivem aparecendo na Jogatina UFPR, uma página na internet que publica gameplays de alunos da universidade.

A página publica muitos vídeos diariamente. Por isso, pode ser dificil encontrar e contar todos os seus vídeos na página. Entretanto, como você também é programador, você decidiu escrever um programa para auxiliá-lo nesta tarefa. Dada a lista de gameplays publicados na página, determine quantos gameplays seus de Contra-Strike foram publicados

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/2543

# Resolução:

O objetivo desse problema é verificar e exibir quantos gameplays de um determinado jogo e jogador foram postados em uma página da internet. Isto é feito recebendo o código de identificação de um jogador, a quantidade de gameplays postadas na página e uma lista das gameplays postadas, contendo a identificação do jogador e o jogo.

Para resolve-lo, começamos declarando as variáveis: `totalGameplays`, que armazenará a quantidade de gameplays postados na página; `idAutor`, que receberá o cógido do jogador a ser buscado; `idPublicado`, que guadará a identificação dos jogadores nos jogos postados; `jogo`, que irá receber `0` se a gameplay postada é de Contra-Strike, ou `1` se é de Liga of Legendas; `contador`, que vai incrementar a medida que achamos uma determinada gameplay e código do jogador e `i` que servirá para iterar sobre um loop `for`.
```c
int totalGameplays, idAutor, idPublicado, jogo, contador, i;
```

Em seguida, criamos um laço de repetição `while` para buscarmos a quantidade de gameplays de Contra-Strike de um determinado jogador. A condição de parada do laço possui o comando `scanf`, que fará a leitura das variáveis `totalGameplays` e `idAutor` até que receba o [final de arquivo (EOF)](https://pt.wikipedia.org/wiki/EOF), encerrando o laço de repetição. 
```c
while(scanf("%d %d", &totalGameplays, &idAutor) != EOF){
```

Dentro do `while` iniciamos a variável contador em 0, pois em cada busca precisamos contar novamente quantos gameplays de determinado jogo foram postados.
```c
contador = 0;
```

Criamos um laço de repetição `for` para receber, através do comando `scanf`, o identificador e o jogo referente aos gameplays postados, e com o comando `if` verificamos se o gameplay possui o código de jogador igual a `idAutor` *e* se é de Contra-Strike(`jogo == 0`). Caso seja, incrementamos `contador` em 1.
```c
for(i = 0; i < totalGameplays; i++){
	scanf("%d %d", &idPublicado, &jogo);

	if(idAutor == idPublicado && jogo == 0)
		contador++;
}
```

Por fim, exibimos com `printf` a quantidade de gameplays de Contra-Strike por determinado jogador.
```c
printf("%d\n", contador);
```

##### Para aprender um pouco mais sobre o laço de repetição `for` : [for](http://linguagemc.com.br/a-estrutura-de-repeticao-for-em-c/)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
 * [Facebook](https://www.facebook.com/petbcc/),
 * [Instagram](https://www.instagram.com/petbcc.ufscar/)
 * ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
