# Problema:

João e Maria criaram sua própria versão de jogar dardos, dardos por distância. Cada um jogava 3 dardos, escolhendo qual distância irão jogar do alvo. No jogo normal de dardos, se pontua um número x  pela distância entre onde o dardo acertou e o centro do alvo. No jogo de João e Maria se pontua x×d onde d é a distancia do atirador e o alvo.

João pede para você fazer um algorítimo que dado a pontuação e a distância de cada jogada devolve o vencedor

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/3037

# Resolução:

Para resolver este problema, receberemos a distância entre o dardo e o centro do alvo e, a distância entre João/Maria e o alvo. Multiplicaremos essas duas distâncias e comparamos quais dos jogadores fizeram mais pontos.

Para iniciar declaramos as variáveis:
`n`, que será a quantidades de jogos entre João e Maria;
`jogadas`, que representa a quantidade de rodadas que cada jogador pode fazer, por jogo;
`distanciaCentro` e `distanciaJogador`, que representam a distância entre o dardo e o centro do alvo e, a distância entre João/Maria e o alvo, respectivamente. 
`pontos` é um vetor, que irá armazenar as pontuações de João e Maria.
```c 
int n, jogadas, distanciaCentro, distanciaJogador;
int pontos[2];
```

Recebemos a quantidade de jogos (`n`) através do comando `scanf` e criamos um laço de repetição `while` onde será calculado quem venceu cada jogo. Em seguida, iniciamos a variável `jogadas` com 6 (3 rodadas para João e 3 para Maria) e os `pontos` de cada jogador em 0, pois ninguém pontuou; 
```c
scanf("%d", &n);

while (n--){
    jogadas = 6;
    pontos[0] = 0;
    pontos[1] = 0;

Então, criamos outros dois loops `while`, onde iremos calcular os pontos de João e Maria. No primeiro loop recebemos, através do `scanf`, as distâncias entre o dardo e o centro do alvo (`distanciaCentro`) e, entre João e o alvo (`distanciaJogador`). Depois multiplicamos esses valores e armazenamos os pontos de João em `pontos[0]`. No segundo `while` faremos o mesmo para Maria, mas guardaremos seus pontos em `pontos[1]`.
```c
while (jogadas>3){

	scanf("%d %d", &distanciaCentro, &distanciaJogador);
	pontos[0] += distanciaAlvo * distanciaAtirador;
	jogadas --;
}

while (jogadas--){

	scanf("%d %d", &distanciaCentro, &distanciaJogador);
	pontos[1] += distanciaAlvo * distanciaAtirador;
}
```

Por fim, com o comando `if-else` comparamos se a pontuação de João (`pontos[0]`) é maior do que a de Maria (`pontos[1]`). Caso seja maior, Joao ganhou e exibimos JOAO com o comando `printf`, caso contrário, Maria venceu e exibimos MARIA.
```c
if(pontos[0] > pontos[1])
	printf("JOAO\n");

else 
	printf("MARIA\n");
```

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
 * [Facebook](https://www.facebook.com/petbcc/),
 * [Instagram](https://www.instagram.com/petbcc.ufscar/)
 * ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
