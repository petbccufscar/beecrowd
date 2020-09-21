# Problema:
Uma brincadeira muito comum e divertida entre dois jogadores usa uma moeda e três copos opacos (ou seja, não é possível ver o que está dentro do copo olhando pela lateral do copo). Os três copos são colocados com a boca para baixo, em uma linha, um ao lado do outro, em posições que vamos chamar de A, B e C. Uma moeda é colocada embaixo de um dos copos. Na brincadeira, um jogador chamado banca realiza um movimento para trocar a posição de dois copos, arrastando os copos de tal modo que se a moeda está em baixo de um dos copos envolvidos no movimento, ela continua embaixo do mesmo copo após a troca de posição. O jogador banca pode realizar três tipos de movimento, ilustrados na figura abaixo:

1. Trocar o copo na posição A com o copo na posição B.

2. Trocar o copo na posição B com o copo na posição C.

3. Trocar o copo na posição A com o copo na posição C.

O jogador banca realiza vários movimentos de troca tentando confundir o outro jogador, chamado espectador. Ao final o jogador espectador deve dizer em qual posição está a moeda. Por exemplo, considere que inicialmente a moeda está embaixo do copo na posição A e que o jogador banca realiza uma sequência de apenas três trocas, executando um movimento do tipo 1, após o qual moeda termina embaixo do copo na posição B, seguido de um movimento do tipo 2, após o qual a moeda termina embaixo do copo na posição C, seguido de um movimento do tipo 3, após o qual a moeda termina embaixo do copo na posição A.

Nesta tarefa, dadas a descrição da sequência de movimentos e a posição inicial da moeda, você deve escrever um programa que determine a posição final da moeda após todos os movimentos.

<img src="https://resources.urionlinejudge.com.br/gallery/images/problems/UOJ_3040.png" />
 
##### Link do problema: https://www.urionlinejudge.com.br/judge/pt/problems/view/3053
 
 
# Resolução:
 
Para determinar a posição final da moeda após todos os movimentos, após determinarmos o estado inicial, trocamos a moeda de lugar, a cada movimento lido. Ao fim de todos os movimentos, imprimimos qual copo a moeda está.

Iremos declarar uma variável do tipo inteiro `N`, indicando o número de movimentos, um caracter `moeda`, indicando o copo inicial da moeda, um vetor de 3 caracteres `copos[3]`, para representar os copos A, B e C,** em ordem**, um caracter `aux`, para auxiliar na troca de copo da moeda e duas variáveis do tipo inteiro, `movimento` e `i`. A variável `movimento` será utilizada na leitura do movimento a ser realizado e `i` será utilizada nos laços de repetição.

```c
int N;
char moeda;

char copos[3], aux;
int movimento, i;
```

Depois, lemos o número de movimentos `N` e o copo inicial em que a moeda está `moeda`. Utilizamos "%s" na leitura de `moeda` pois "%c" ou "%[^\n]" levam a erro por motivos desconhecidos.

```c
scanf("%d", &N);
scanf("%s", &moeda);
```

Em seguida, definimos o estado inicial dos copos, utilizando a estrutura condicional `if`, conforme o valor lido de `moeda`. Caso seja `A`, significa que a moeda está no copo A. De forma análoga, ocorre o mesmo caso o valor seja `B` ou `C`.

```c
if(moeda == 'A')
	copos[0] = 'A';
			
else if( moeda == 'B')
	copos[1] = 'B';
			
else if( moeda == 'C')
	copos[2] = 'C';
```

Depois, realizaremos `N` movimentos de troca e, para isso, utilizaremos o laço de repetição `for`. A cada iteração do laço, lemos o movimento a ser realizado por meio da função `scanf()` e, de acordo com o movimento lido, trocamos a moeda de lugar:
- Se o movimento lido for `1`, trocamos o conteúdo do copo A (`copos[0]`) pelo do copo B (`copos[1]`), utilizando um auxiliar `aux`.
- Se o movimento lido for `2`, trocamos o conteúdo do copo B (`copos[1]`) pelo do copo C (`copos[2]`), utilizando um auxiliar `aux`.
- Se o movimento lido for `3`, trocamos o conteúdo do copo A (`copos[0]`) pelo do copo C (`copos[2]`), utilizando um auxiliar `aux`.


```c
for(i = 0; i < N; i++){
	scanf("%d", &movimento);
		
	if( movimento == 1){

		aux = copos[0];
		copos[0] = copos[1];
		copos[1] = aux; 

	}else if(movimento == 2){
		    
	    aux = copos[1];
		copos[1] = copos[2];
		copos[2] = aux;
			
	}else if(movimento == 3){

		aux = copos[0];
		copos[0] = copos[2];
		copos[2] = aux;
	}

}
```

Em seguida, imprimimos o resultado. Para isto, iremos utilizar um laço de repetição `for`, para percorrer o vetor `copos`. A cada iteração, verificamos se o valor contido no endereço atual, `copos[i]` é `A` ou `B` ou `C`.
Porém, ao invés de exibirmos este valor (A ou B ou C), iremos trabalhar com o endereço do vetor, pois este sim indica qual a posição em que a moeda está. Caso qualquer letra lida esteja no endereço 0, significa que a moeda está no copo A e que letra a ser exibida é `A`.

**Para imprimir um caracter a partir de um número inteiro, utilizaremos a tabela ASCII. Nesta tabela, o caracter `A` é representado pelo número decimal `65`, o caracter `B` é representado pelo número decimal `66` e assim por diante, logo, o caracter `C` é representado pelo número decimal `67`. Por isso, para exibirmos em qual copo a moeda está, utilizamos a função `printf("%c\n", i + 65)`.**

```c
for(i = 0; i < 3; i++)
	if(copos[i] == 'A' || copos[i] == 'B' || copos[i] == 'C')
	    printf("%c\n", i + 65);

```

##### Mais a tabela ASCII: [utilização tabela ASCII](https://pt.wikipedia.org/wiki/ASCII)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
