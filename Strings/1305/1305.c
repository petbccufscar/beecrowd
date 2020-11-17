#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main (){

	char numero[10];
	char corte[7];

	int inteiro;
	double fracionario, cutoff;

	while( scanf("%s %s", numero, corte) != EOF){
		
		inteiro = atoi(numero);
		fracionario = atof(numero) - inteiro;
		cutoff = atof(corte); 

		if(fracionario > cutoff)
			inteiro++; 

		printf("%d\n", inteiro);
	}

return 0;
}
