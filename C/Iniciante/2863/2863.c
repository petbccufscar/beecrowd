#include <stdio.h>

int main ()
{

	int T, i;
	float numero, menor;

	while (scanf("%d", &T) != EOF)
	{

		menor = 100.0;
		for (i = 0; i < T; i++)
		{
			scanf("%f", &numero);
			if (numero < menor)
				menor = numero;

		}

		printf("%.2f\n", menor);

	}
	
	return 0;
}