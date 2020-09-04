#include <stdio.h>

int main ()
{
	int alturaPlaca, larguraPlaca, qtsPedidos;
	int alturaPci, larguraPci, i;

	while (scanf("%d %d %d", &alturaPlaca, &larguraPlaca, &qtsPedidos) != EOF)
	{
		for (i = 0; i < qtsPedidos; i++)
		{
			scanf("%d %d", &alturaPci, &larguraPci);

			if ((alturaPci <= alturaPlaca && larguraPci <= larguraPlaca) || (alturaPci <= larguraPlaca && larguraPci <= alturaPlaca))
				printf("Sim\n");
			else
				printf("Nao\n");
		}

	}
    return 0;
}