#include <stdio.h>

int matriz[101][101], maux[101][101];

int main() {
	int tamMatriz, soma, inicio, fim, i, j;

	scanf("%d", &tamMatriz);

	for (i = 0; i < tamMatriz; i++)
		for (j = 0; j < tamMatriz; j++)
			scanf("%d", &matriz[i][j]);

    soma = 0;
    for(i = 0; i < tamMatriz; i++)
        maux[0][i] = matriz[0][i];
    
    i = 1;
    inicio = 0;
    fim = 1;
    
    while (i < tamMatriz-1) {
        for(j = inicio; j <= fim; j++) 
            maux[i][inicio] += matriz[i][j];
        
        if (maux[i-1][inicio] < maux[i-1][inicio+1])
            maux[i][inicio] += maux[i-1][inicio];
        else
            maux[i][inicio] += maux[i-1][inicio+1];
        inicio++;
        fim++;
        if (fim == tamMatriz) {
            i++;
            inicio = 0;
            fim = i;
        }
    }


    if (maux[tamMatriz-2][0] < maux[tamMatriz-2][1])
        soma = maux[tamMatriz-2][0];
    else
        soma = maux[tamMatriz-2][1];
        
    for(i = 0; i < tamMatriz; i++)
        soma += matriz[tamMatriz-1][i];
	printf("%d\n", soma);
	
	return 0;
}
