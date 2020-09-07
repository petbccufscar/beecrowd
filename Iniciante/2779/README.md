# Problema:
Em ano de Copa do Mundo de Futebol, o álbum de figurinhas oficial é sempre um grande sucesso entre crianças e também entre adultos. Para quem não conhece, o álbum contém espaços numerados de 1 a N para colar as figurinhas; cada figurinha, também numerada de 1 a N, é uma pequena foto de um jogador de uma das seleções que jogará a Copa do Mundo. O objetivo é colar todas as figurinhas nos respectivos espaços no álbum, de modo a completar o álbum (ou seja, não deixar nenhum espaço sem a correspondente figurinha).

As figurinhas são vendidas em envelopes fechados, de forma que o comprador não sabe quais fi- gurinhas está comprando, e pode ocorrer de comprar uma figurinha que ele já tenha colado no álbum.

Para ajudar os usuários, a empresa responsável pela venda do álbum e das figurinhas quer criar um aplicativo que permita gerenciar facilmente as figurinhas que faltam para completar o álbum e está solicitando a sua ajuda.

Dados o número total de espaços e figurinhas do álbum, e uma lista das figurinhas já compradas (que pode conter figurinhas repetidas), sua tarefa é determinar quantas figurinhas faltam para completar o álbum.
 
##### Link do problema: https://www.urionlinejudge.com.br/judge/pt/problems/view/2779
 
 
# Resolução:
 
Para calcular o número de figurinhas que faltam, em suma, iremos:
Declarar um vetor de tamanho 101 (`album[101]`) e inicializá-lo com 0, indicando que nenhuma figurinha foi obtida ainda. 
Durante a leitura, a cada figurinha comprada, atribuímos 1 à respectiva posição dela no vetor.
Ao fim deste processo, percorremos o album até o tamanho dele e, caso o valor lido for 0, significa que esta figurinha está faltando e adicionamos 1 ao contador de figurinhas faltando.

Dessa forma, iremos declarar as seguintes variáveis:

```c
int i, aux;
int qtdTotal, compradas;
int album[101] = {0};
int faltam = 0;
```

A variável `qtdTotal` indica o número total de figurinhas do álbum, `compradas` indica o número de figurinhas já compradas e `album[101] = {0}` indica o álbum. Note que o vetor é declarado com 101 posições pois o número de figurinhas começa em 1 e termina em 100 e, caso declarássemos com tamanho 100, nosso vetor iria da posição 0 a 99. Além disso, cada posição deste é iniciado com `0`, indicando que nenhuma figurinha foi obtida ainda.

Em seguida, lemos `qtdTotal` e `compradas`.

```c
scanf("%d", &qtdTotal);
scanf("%d", &compradas);
```

Depois, iremos atribuir `1` às posições do àlbum que possuem figurinha. Por exemplo, a posição album[10] refere-se a figurinha número 10 e, que o valor `0` indica que não a temos e `1` que temos.

Para isso, utilizaremos a estrutura de repetição `for`, em que a cada iteração, lemos a figurinha comprada e a utilizamos como índice do vetor `album`,para atribuirmos `1` à posição. 

```c
for (i = 0; i < compradas; i++){
		scanf("%d", &aux);
		album[aux] = 1;
	}
```

Em seguida, vamos percorrer o vetor `album`, de `1` até `qtdTotal`, por meio da estrutura de repetição `for` e, caso o valor da posição vigente for 0, adicionamos 1 à `faltam`, nosso contador de figurinhas faltantes.

```c
for (i = 1; i <= qtdTotal; i++)
		if (!album[i])
			faltam++;

```

Em seguida, vamos exibir o resultado, utilizando a função `printf()`.

```c
printf("%d\n", faltam);
```
 
Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com