#include <stdio.h>

int main()
{

	int X, Y, i, N, j;
	unsigned char vezes;
	scanf("%d", &N);

	for (i = 0; i < N; i++)
	{

		scanf("%d%c%d", &X, &vezes, &Y);

		if (X == Y)
			for (j = 5; j <= 10; j++)
				printf("%d x %d = %d\n", X, j, X*j);
		else
			for (j = 5; j <= 10; j++)
				printf("%d x %d = %d && %d x %d = %d\n", X, j, X*j, Y, j, Y*j);
	}
	return 0;
}