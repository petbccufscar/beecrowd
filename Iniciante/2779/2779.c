#include <stdio.h>

int main (){

	int i, aux;
	int qtdTotal, compradas;
    int album[101] = {0};
    int faltam = 0;
    
	scanf("%d", &qtdTotal);
	scanf("%d", &compradas);

	for (i = 0; i < compradas; i++){
		scanf("%d", &aux);
		album[aux] = 1;
	}

	for (i = 1; i <= qtdTotal; i++)
		if (!album[i])
			faltam++;

	printf("%d\n", faltam);

return 0;
}