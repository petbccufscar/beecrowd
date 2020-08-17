#include <stdio.h>
#include <string.h>

void main (){
	int N, aux;
	char jogador1[10], jogador2[10];

	scanf("%d", &N);

	for(aux = 0; aux < N; aux++){
		scanf("%s %s", jogador1, jogador2);

		if (strcmp(jogador1, "ataque") == 0 && strcmp(jogador2, "ataque") == 0)
			printf("Aniquilacao mutua\n");

		if (strcmp(jogador1, "papel") == 0 && strcmp(jogador2, "papel") == 0)
			printf("Ambos venceram\n");

		if (strcmp(jogador1, "pedra") == 0 && strcmp(jogador2, "pedra") == 0)
			printf("Sem ganhador\n");

		if (strcmp(jogador1, "pedra") == 0 && strcmp(jogador2, "papel") == 0)
			printf("Jogador 1 venceu\n");

		if (strcmp(jogador2, "pedra") == 0 && strcmp(jogador1, "papel") == 0)
			printf("Jogador 2 venceu\n");

		if (strcmp(jogador1, "ataque") == 0 && strcmp(jogador2, "papel") == 0)
			printf("Jogador 1 venceu\n");

		if (strcmp(jogador2, "ataque") == 0 && strcmp(jogador1, "papel") == 0)
			printf("Jogador 2 venceu\n");

		if (strcmp(jogador1, "ataque") == 0 && strcmp(jogador2, "pedra") == 0)
			printf("Jogador 1 venceu\n");

		if (strcmp(jogador2, "ataque") == 0 && strcmp(jogador1, "pedra") == 0)
			printf("Jogador 2 venceu\n");

	}

	return 0;
}