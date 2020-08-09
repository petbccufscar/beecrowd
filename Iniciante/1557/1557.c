
#include <stdio.h>

int main ()
{

	int N, linha, coluna, valor;

	while (1)
	{

		scanf("%d", &N);

		if (N == 0)
			return 0;

		int M[N][N];

		valor = 1;

		for (linha = 0; linha < N; linha++)
		{
			for (coluna = 0; coluna < N; coluna++)
			{
				M[linha][coluna] = valor;
				valor *= 2;
			}

			valor = (M[linha][0]) * 2;

		}

		int maior, digitos = 0;

		maior = (M[N - 1][N - 1]);

		do
		{
			maior = maior/10;
			digitos++;
		} while (maior > 0);

		for (linha = 0; linha < N; linha++)
		{
			for (coluna = 0; coluna < N; coluna++)
			{
				if (coluna == 0)
					//Prints com N variado para o campo de espaços;
					printf("%*d", digitos, M[linha][coluna]);
				else
					printf(" %*d", digitos, M[linha][coluna]);
			}

			printf("\n");
		}

		printf("\n");

	}
}