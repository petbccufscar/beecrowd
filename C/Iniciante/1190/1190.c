#include <stdio.h>

int main (){
	double m[12][12], soma, media;
	char operacao;
	int i, j, cont;
	scanf("%c", &operacao);

	for(i = 0; i < 12; i++)
		for(j = 0; j < 12; j++)
			scanf("%lf", &m[i][j]);

	if (operacao == 'S'){
		soma = 0;
		for(i = 0; i < 12; i++)
			for(j = 0; j < 12; j++)
				if (i < j && i > 12 - j - 1)
					soma += m[i][j];

		printf("%.1lf\n", soma);
	}

	if (operacao == 'M'){
		media = 0;
		cont = 0;
		for(i = 0; i < 12; i++)
			for(j = 0; j < 12; j++)
				if (i < j && i > 12 - j - 1){
					media += m[i][j];
					cont++;
				}

		printf("%.1lf\n", media/cont);
	}
}