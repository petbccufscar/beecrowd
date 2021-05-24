#include <stdio.h>

int main(){
	int nCasos, valor, i, j, soma;
	scanf("%d", &nCasos);

	for(i=0; i<nCasos; i++){
		scanf("%d", &valor);
		soma = 0;

		for(j=1; j<valor; j++)
			if(valor % j == 0)
				soma += j;
			
		if(soma == valor)
			printf("%d eh perfeito\n", valor);
		else
	 		printf("%d nao eh perfeito\n", valor);

	} 

	return 0;
}