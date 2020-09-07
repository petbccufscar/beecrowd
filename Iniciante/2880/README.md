# Problema:
A organização da OIBR, Olimpíada Internacional de Basquete de Robô, está começando a ter problemas com dois times: os Bit Warriors e os Byte Bulls. É que os robôs desses times acertam quase todos os lan- çamentos, de qualquer posição na quadra! Pensando bem, o jogo de basquete ficaria mesmo sem graça se jogadores conseguissem acertar qualquer lançamento, não é mesmo? Uma das medidas que a OIBR está implantando é uma nova pontuação para os lançamentos, de acordo com a distância do robô para o início da quadra. A quadra tem 2000 centímetros de comprimento, como na figura.

Dada a distância D do robô até o início da quadra, onde está a cesta, a regra é a seguinte:

• Se D ≤ 800, a cesta vale 1 ponto;

• Se 800 < D ≤ 1400, a cesta vale 2 pontos;

• Se 1400 < D ≤ 2000, a cesta vale 3 pontos.

A organização da OIBR precisa de ajuda para automatizar o placar do jogo. Dado o valor da distância D, você deve escrever um programa para calcular o número de pontos do lançamento
 
##### Link do problema: https://www.urionlinejudge.com.br/judge/pt/problems/view/2780
 
 
# Resolução:
 
Para calcular a pontuação da cesta, iremos declarar a variávei inteira distancia.

```c
int distancia;
```

Depois, lemos o `distancia`.

```c
scanf("%d", &distancia);
```

Em seguida, imprimimos o resultado. Caso o valor lido seja menor ou igual a 800, imprimimos 1. Caso seja maior que 800 e menor que 1400, imprimirmos 2. Caso seja maior que 1400, imprimimos 3.

```c
if (distancia <= 800)
		printf("1\n");
	else if (distancia <= 1400)
		printf("2\n");
	else
		printf("3\n");

```
 
Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com