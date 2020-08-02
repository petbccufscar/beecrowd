#include <stdio.h>

int main(){
	int nCasos, valor, i, j, primo;
	scanf("%d", &nCasos);

	for(i=0; i<nCasos; i++){
		scanf("%d", &valor);
		primo = 1;
if(valor == 1)
    primo = 0;
		for(j=2; j<valor; j++)
			if(valor % j == 0)
				primo = 0;
			
		if(primo == 1)
			printf("%d eh primo\n", valor);
		else
	 		printf("%d nao eh primo\n", valor);

	} 

	return 0;
}
