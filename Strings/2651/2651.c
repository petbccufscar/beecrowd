#include <stdio.h>
#include <string.h>

int temZelda(char *nome);

int main ()
{
	char nome[100001];

	scanf("%s", nome);

	if (!temZelda(nome))
		printf("Link Tranquilo\n");
	else
		printf("Link Bolado\n");

    return 0;
}

int temZelda(char *nome)
{
	int i, j, contador = 0;
	char comparacao[6] = "zelda";

	for (i = 0, j = 0; nome[i]; i++)
	{	
		if (nome[i] == comparacao[j] || nome[i] == comparacao[j] + 32 || nome[i] == comparacao[j] - 32)
		{
			j++;
			contador++;

			if (contador == 5)
				return 1;
		}
		else
		{
			contador = 0;
			j = 0;
		}
	}
	return 0;
}