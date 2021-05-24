#include <stdio.h>
#include <string.h>

int main(){

	int turistas, jipes = 0, turistasFaltantes = 0;
	char operacao[10];

	while (1){
		scanf("%s", operacao);

		if (strcmp(operacao, "ABEND") == 0)
			break;

		scanf("%d", &turistas);
		if (strcmp(operacao, "SALIDA") == 0)
			turistasFaltantes += turistas, jipes++;
		else
			turistasFaltantes -= turistas, jipes--;
	}

	printf("%d\n%d\n", turistasFaltantes, jipes);

	return 0;
}