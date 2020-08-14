#include<stdio.h>

int main(){
	int i, j, numero, caso, quantNumeros;

	caso = 0;

	while(scanf("%d", &numero)!= EOF){

		quantNumeros = 1;
		caso++;

		quantNumeros += ((numero*(numero+1))/2);

		if(numero == 0)
			printf("Caso %d: %d numero\n", caso, quantNumeros);
		else
			printf("Caso %d: %d numeros\n", caso, quantNumeros);

		printf("0");

		for(i=1;i<=numero;i++){
			for(j=1; j<=i; j++)
				printf(" %d", i);
		}
		printf("\n\n");
	}
	return 0;
}
