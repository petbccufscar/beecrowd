#include <stdio.h>

int main() {
	int N, posicao=0, menorValor;
	
	scanf("%d",&N);
	int X[N], i;
	
	for(i=0;i<N;i++){
		scanf("%d",&X[i]);
		
		if(X[i] < X[posicao]){
      		menorValor = X[i];
      		posicao = i;
		}
		
		else{
			menorValor = X[posicao];
    	}
	}
	
	printf("Menor valor: %d\n",menorValor);
	printf("Posicao: %d\n",posicao);
	
	return 0;
}
