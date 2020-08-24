# Problema:

Prog e Cackto começaram recentemente a jogar um jogo de RPG chamado Fortaleza. Neste, para o jogador evoluir de nível o mesmo precisa derrotar monstros, nos quais dá um valor de experiência (XP) para o jogador.  

A produtora do jogo, Jogos Extremos, anunciou que na próxima semana irá realizar o primeiro evento XP no qual aumentará a experiência dos monstros em X vezes. Como Prog e Cackto estão em um nível muito alto no qual os monstros tem um valor muito alto de pontos de experiência, eles estão tendo dificuldades de calcular a quantidade de pontos de experiência que os monstros terão durante o evento. Você pode ajudá-los?


##### Link do problema: https://www.urionlinejudge.com.br/judge/pt/problems/view/2172
 
 
# Resolução:

O exercício resume-se em fazer uma multiplicação entre `M` e `X` e exibir seu resultado. Devemos notar que a entrada de `M` pode variar de 10 até 2<sup>31</sup>-1, ou seja, variáveis do tipo `int` não suportam a magnitude do valor.  
Dessa forma, utilizaremos uma variável do tipo `unsigned long int` para armazenar a experiência `exp` dos monstros e uma variável `int` para armazenar o fator de multiplicação `mult` do evento.

```c
int mult;
unsigned long int exp;
```

Em seguida, faremos a primeira leitura dos valores através da função `scanf()`. Note que, como utilizamos `unsigned long int`, devemos ler o valor de `exp` através do parâmetro `%lu`.

```c
scanf("%d %lu", &mult, &exp);
```

Utilizaremos um laço de repetição `while` para calcular a experiência final de cada monstro. Dentro do laço, exibimos o valor na própria função `printf()`, utilizando novamente o argumento `%lu` para exibir o resultado.  
Por último, fazemos novamente a leitura dos próximos valores através da função `scanf()`. Caso ambos sejam iguais a `0`, o laço é interrompido e o programa se encerra.

```c
while (exp != 0 && mult != 0) {
    printf("%lu\n", (exp * mult));
    
    scanf("%d %lu", &mult, &exp);
}
```

##### Para aprender um pouco mais sobre tipos de variáveis: [Tipos de Variáveis](http://linguagemc.com.br/tipos-de-dados-em-c/)
##### Para revisar a estrutura de repetição while: [while](http://linguagemc.com.br/o-comando-while-em-c/)


Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com