#include <stdio.h>

int main ()
{

	int distancia;

	scanf("%d", &distancia);

	if (distancia <= 800)
		printf("1\n");
	else if (distancia <= 1400)
		printf("2\n");
	else
		printf("3\n");

return 0;
}