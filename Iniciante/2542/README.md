# Problema:

Uma partida de Iu-di-oh! é sempre jogada por dois jogadores. Ao iniciar a partida, cada jogador escolhe exatamente uma carta de seu baralho. Após as escolhas, um atributo é sorteado. Vence o jogador cujo atributo sorteado em sua carta escolhida é maior que na carta escolhida pelo adversário. Caso os atributos sejam iguais, a partida empata.

Marcos e Leonardo estão na grande final do campeonato brasileiro de Iu-di-oh!, cujo prêmio é um Dainavision (que é quase um Plaisteition 2!). Dados os baralhos de ambos, a carta escolhida por cada um e o atributo sorteado, determine o vencedor!

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/2542

# Resolução:

O objetivo desse problema é verificar qual atributo é maior, dado as cartas escolhidas por Marcos e Leonardo, e exibir o vencedor da partida.

Para resolvê-lo, começamos declarando as variáveis: 
- `numAtributos`, que irá armazenar a quantidade de atributos a serem considerados de cada carta;
- `tamBaralhoM` e `tamBaralhoL`, que irão armazenar a quantidade de cartas de Marcos e Leonardo, respectivamente; 
- `cartasMarcos[100][100]` e `cartasLeonardo[100][100]` são matrizes, que guardarão os atributos de cada carta de Marcos e Leonardo, respectivamente; 
- `escolhidaM` e `escolhidaL`, que irão receber as cartas escolhidas por Marcos e Leonardo; 
- `atributoSorteado`, que receberá a posição do atributo a ser considerado das cartas que Marcos e Leonardo escolheram;
- `i` e `j`, que irão iterar sobre laços de repetição.
```c
int numAtributos, tamBaralhoL, tamBaralhoM, cartasMarcos[100][100], cartasLeonardo[100][100];
int escolhidaM, escolhidaL, atributoSorteado, i, j;
```

Em seguida, criamos um laço de repetição `while` que irá calcular o resultado de cada partida. A condição de parada do laço possui o comando `scanf`, que fará a leitura da variável `numAtributos` até que receba o [final de arquivo (EOF)](https://pt.wikipedia.org/wiki/EOF), encerrando o laço de repetição.
Dentro do `while` realizamos a leitura com `scanf` da quantidade de cartas de Marcos de Leonardo.
```c
while(scanf("%d", &numAtributos) != EOF){

	scanf("%d %d", &tamBaralhoM, &tamBaralhoL);
```

Com dois loops `for` aninhados, iremos receber os atributos de cada carta de Marcos com o comando `scanf`, repetindo o mesmo processo para cada carta de Leonardo.
```c
for (i = 0; i < tamBaralhoM; i++)
{
	for(j = 0; j <numAtributos; j++)
		scanf("%d", &cartasMarcos[i][j]);
}

for (i = 0; i < tamBaralhoL; i++)
{
	for(j = 0; j <numAtributos; j++)
		scanf("%d", &cartasLeonardo[i][j]);
}
``` 

Então, recebemos com o `scanf` quais cartas foram escolhidas por Marcos e Leonardo, e qual o atributo será sorteado para a partida.
```c
scanf("%d %d", &escolhidaM, &escolhidaL);
scanf("%d", &atributoSorteado);
```

Por fim, a partir das cartas escolhidas e do atributo selecionado, verificamos com a estrutura `if` qual é o maior atributo das cartas escolhidas por Marcos e Leonardo. 
Caso o maior atributo seja da carta de Marcos, exibimos o nome dele; 
```c
if(cartasMarcos[escolhidaM-1][atributoSorteado-1] > cartasLeonardo[escolhidaL-1][atributoSorteado-1])
	printf("Marcos\n");
```

Caso contrário exibimos o nome de Leonardo. 
```c
else if(cartasMarcos[escolhidaM-1][atributoSorteado-1] < cartasLeonardo[escolhidaL-1][atributoSorteado-1])
	printf("Leonardo\n");
```
 * Note que todas as posições da matriz são subtraídas em 1. Fazemos isso pois suas posições se iniciam em 0 e em liguagem natural iniciamos em 1.

Caso os atributos sejam iguais, exibimos: Empate.
```c
else	
	printf("Empate\n");
```

##### Para aprender um pouco mais sobre o laço de repetição `for` : [for](http://linguagemc.com.br/a-estrutura-de-repeticao-for-em-c/)
##### Para aprender um pouco mais sobre matriz em C : [Matriz em C](http://linguagemc.com.br/matriz-em-c/)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
 * [Facebook](https://www.facebook.com/petbcc/),
 * [Instagram](https://www.instagram.com/petbcc.ufscar/)
 * ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com