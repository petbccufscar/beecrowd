#include <stdio.h>

int main()
{
    int jogos, carro, ganhou;

    ganhou = 0;

	scanf("%d", &jogos);
	while (jogos--)
	{
		scanf("%d", &carro);
		if (carro != 1)
			++ganhou;
	}

	printf("%d\n", ganhou);

	return 0;

}