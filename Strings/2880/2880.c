#include <stdio.h>
#include <string.h>

void main (){

	char cifra[10001], crib[10001];

	int igualdades, limite, qtsPosicoesPossiveis;
	int i, j, k;

	scanf("%s %s", cifra, crib);

	k = 0;
	qtsPosicoesPossiveis = 0;
	limite = strlen(cifra) - strlen(crib);

	while (k <= limite){

		j = 0;
		i = k;
		igualdades = 0;

		while ( j < strlen(crib) && !igualdades){

			if (cifra[i] == crib[j])
				igualdades = 1;

			else{

				j++;
				i++;
			}
		}

		k++;

		if (!igualdades)
			qtsPosicoesPossiveis++;

	}

	printf("%d\n", qtsPosicoesPossiveis);
	return 0;
}

