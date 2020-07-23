#include <stdio.h>

int main() {
	int X, contador;
	scanf("%d",&X);

	for(contador = 1; contador<=X; contador++)
		if(contador%2!=0)
			printf("%d\n",contador);

	return 0;
}