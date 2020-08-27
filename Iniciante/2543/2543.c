#include <stdio.h>

int main(){

	int totalGameplays, idAutor, idPublicado, jogo, contador, i;

	while(scanf("%d %d", &totalGameplays, &idAutor) != EOF){

		contador = 0;

		for(i = 0; i < totalGameplays; i++){
			scanf("%d %d", &idPublicado, &jogo);

			if(idAutor == idPublicado && jogo == 0)
				contador++;
		}

		printf("%d\n", contador);
	}
	return 0;
}