# Problema

Samu Elmito adora criar jogos peculiares para desafiar seus amigos. Desta vez, ele inventou um jogo chamado "Jogo do Operador", em que ele cria expressões básicas e cada jogador deve escolher uma expressão e preencher a lacuna com o operador correto para validá-la. Os jogadores poderão escolher operadores de somente três tipos: adição, subtração e multiplicação. Porém, se o jogador achar que não há operador entre os três tipos que valide a expressão, poderá responder Impossível.

Sua tarefa é simples: dadas as expressões e as respostas dos jogadores, determinar os jogadores que não passarão para a outra fase do jogo.

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/2493

# Resolução:

Para resolver esse problema, vamos receber uma quantidade N de jogadores, uma quantidade N de expressões, o nome e a resposta de cada jogador para uma determinada expressão. Com isso, verificamos se a respostas dadas satisfazem as expressões e exibimos se todos os jogadores acertaram, se todos erraram ou os que erraram.

Começamos inserindo a bibliote `stdlib.h`, que contém a função [`qsort`](http://www.galirows.com.br/meublog/programacao/utilizacao-funcao-qsort/) que junto a função auxiliar `compara` será utilizada posteriormente para ordenar alfabeticamente os nomes dos jogadores.
```c
#include <stdlib.h>
```

Depois declaramos uma [variável global](http://linguagemc.com.br/funcoes-e-escopo-de-variaveis/) `nomeJogador`, que é um vetor de `string` para armazenar o nome de cada jogador. Ela é declarada globalmente pois será utilizada em todas as funções do programa. Por exemplo, na função `compara` que, como foi dito, é uma função auxiliar ao `qsort` que servirá para ordenar o nome dos jogadores.
```c
char nomeJogador[50][50];

int compara(const void *a, const void *b)
{
    const int *p1 = (const int *) a;
    const int *p2 = (const int *) b;

    return strcmp(nomeJogador[*p1], nomeJogador[*p2]);
}
```

Agora podemos iniciar as outras variáveis normalmente: `quantJogadores` é um vetor de inteiros, que armazenará a quantidade de jogadores; `x`, `y` e `z` são vetores de inteiros, que juntos representam cada expressão; `expressao` que será um vetor para armazenar a qual expressão um jogador está se referindo; `naoProsseguira` é um vetor que irá armazenar 0's ou 1's dependendo se a resposta do jogador esta errada ou certa, respectivamente; `flag` que servirá para saber se todos ou nenhum jogador venceu a rodada; `i` itera sobre o loop `for` e `resposta`, que é um vetor de caracteres que amazena cada resposta referente a um jogador.
```c
int quantJogadores, x[50], y[50], z[50], expressao[50], naoProsseguira[50], flag, i;
char resposta[50];
```

Iremos iniciar um loop `while` para testar cada rodada que será jogada. A condição de parada do laço possui o comando `scanf`, que fará a leitura da variável `quantJogadores` até que receba o [final de arquivo (EOF)](https://pt.wikipedia.org/wiki/EOF), encerrando o loop.
```c
while(scanf("%d", &quantJogadores) != EOF){}
```

Dentro do `while` iniciamos a variável `flag`, que será incrementada a cada resposta errada que os jogadores dão.
```c
	flag = 0;
```

Em seguida, faremos a leitura das expressões e das respostas dos jogadores. Estas leituras serão divididas entre duas estruturas de repetição `for` para cada jogador em `quantJogadores` e serão feitas pela função `scanf`.
```c
		for(i=0; i<quantJogadores; i++)
			scanf("%d %d=%d", &x[i], &y[i], &z[i]);

		for(i = 0; i < quantJogadores; i++)
			scanf("%s %d %c", &nomeJogador[i], &expressao[i], &resposta[i]);
```

Depois, iremos criar outra estrutura `for` para abrigar todos os possíveis casos de respostas. 
Esses casos serão tratados pela estrutura `switch case`. Cada `case` é uma situação diferente, similar à estrutura do `if... else`. Caso algum destes casos seja satisfeito, o programa, através do `if`, verifica se a resposta dada pelo jogador está incorreta e, caso esteja, acrescenta a posição do jogador na lista `nomeJogador` ao vetor `naoProsseguira`, incrementa o variável de erros `flag` e sai do laço pelo `break`. Trataremos os possíveis casos de soma `+`, subtração `-`, multiplicação `*` e impossível `I`.
```c
		for (i = 0; i < quantJogadores; i++)
		{
			switch(resposta[i]){
				case '+':
					if(x[expressao[i]-1] + y[expressao[i]-1] != z[expressao[i]-1])
						naoProsseguira[flag++] = i;
					break;

				case '-':
					if(x[expressao[i]-1] - y[expressao[i]-1] != z[expressao[i]-1])
						naoProsseguira[flag++] = i;
					break;

				case '*':
					if(x[expressao[i]-1] * y[expressao[i]-1] != z[expressao[i]-1])
						naoProsseguira[flag++] = i;
					break;

				case 'I':
					if(x[expressao[i]-1] + y[expressao[i]-1] == z[expressao[i]-1] ||
					   x[expressao[i]-1] - y[expressao[i]-1] == z[expressao[i]-1] ||
					   x[expressao[i]-1] * y[expressao[i]-1] == z[expressao[i]-1])
						naoProsseguira[flag++] = i;
					break;
				}
		}
```

Caso não ocorra nenhum erro e, portanto, a variável `flag` continua 0, exibimos a mensagem de que todos passarão com a função `printf`.
```c
		if(flag == 0)
		 printf("You Shall All Pass!\n");
```

Caso `flag` tenha o número de jogadores, significa que todos os jogadores erraram e, desta forma, exibimos a mensagem de que nenhum jogador passará.
```c
		else if (flag == quantJogadores)
			 printf("None Shall Pass!\n");
```

Caso contrário, alguns jogadores acertaram e outros erraram. 
Utilizamos a função `qsort` para ordenar a lista de nomes que não passarão em ordem alfabética. Essa função recebe como parâmetros o vetor que irá ser ordenado(`naoProsseguira`), o tamanho desse vetor(`flag`), o tamanho de cada elemento de vetor(`sizeof(int)`) e uma função auxiliar `compara`, que mostramos no início da explicação.
```c
		else{
			qsort(naoProsseguira, flag, sizeof(int), compara);
```

E, por fim, exibimos os nomes dos jogadores que erraram. Usaremos uma estrutura `for` para passar por todas as posições do vetor de nomes `naoProsseguira` e exibiremos os nomes com `printf`. Lembre-se de incluir o último nome fora da estrutura `for`, pois este deverá ser exibido com uma quebra de linha `\n` no final.
```c
			for(i = 0; i < flag -1; i++)
				printf("%s ", nomeJogador[naoProsseguira[i]]);

			printf("%s\n", nomeJogador[naoProsseguira[i]] );
```

##### Para aprender um pouco mais sobre a estrutura switch: [`switch case`](http://linguagemc.com.br/o-comando-switch-case-em-c/)
##### Para aprender um pouco mais sobre a função qsort: [`qsort`](http://www.galirows.com.br/meublog/programacao/utilizacao-funcao-qsort/)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
* [Facebook](https://www.facebook.com/petbcc/),
* [Instagram](https://www.instagram.com/petbcc.ufscar/)
* ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com