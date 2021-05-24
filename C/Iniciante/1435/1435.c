#include <stdio.h>

int main (){
	int tamanho, coluna, linha;
	int inicioMatriz, fimMatriz;
	int elemento;

	do{
		scanf("%d", &tamanho);
		if (tamanho == 0)
			return 0;

		int m[tamanho][tamanho];

		inicioMatriz = 0;
		fimMatriz = tamanho;
		elemento = 1;

		while(fimMatriz>0){
			for (linha = inicioMatriz; linha < fimMatriz; linha++)
				for (coluna = inicioMatriz; coluna < fimMatriz; coluna++)
					m[linha][coluna] = elemento;

			inicioMatriz++;
			fimMatriz--;
			elemento++;
		}

		for (linha = 0; linha < tamanho; linha++){
			for (coluna = 0; coluna < tamanho; coluna++){
				if (coluna == 0)
					printf("%3d", m[linha][coluna]);
				else
					printf(" %3d", m[linha][coluna]);
			}

			printf("\n");
		}

		printf("\n");
	}while(1);
}