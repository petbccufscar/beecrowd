#include <stdio.h>

int main(){

	int numAtributos, tamBaralhoL, tamBaralhoM, cartasMarcos[100][100], cartasLeonardo[100][100], escolhidaM, escolhidaL, atributoSorteado, i, j;

	while(scanf("%d", &numAtributos) != EOF){

		scanf("%d %d", &tamBaralhoM, &tamBaralhoL);

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

		scanf("%d %d", &escolhidaM, &escolhidaL);
		scanf("%d", &atributoSorteado);

		if(cartasMarcos[escolhidaM-1][atributoSorteado-1] > cartasLeonardo[escolhidaL-1][atributoSorteado-1])
			printf("Marcos\n");

		else if(cartasMarcos[escolhidaM-1][atributoSorteado-1] < cartasLeonardo[escolhidaL-1][atributoSorteado-1])
			printf("Leonardo\n");

		else	
			printf("Empate\n");
	} 

	return 0;
}