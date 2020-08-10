#include <stdio.h>

int buscaMaiorValor(int *V, int L){
	int posicao = 0;
	int maiorValor, i;
	
	for(i=0; i<L; i++){
		if(V[i] > V[posicao]){
      		maiorValor = V[i];
      		posicao = i;
		}
		
		else{
			maiorValor = V[posicao];
    	}
	}
	
	return maiorValor;
}

int main() {
	int L;
	
	while(scanf("%d",&L) != EOF){
		int V[L];
		int i;
	
		for(i=0; i<L; i++){
			scanf("%d",&V[i]);
		}
		
		int maiorValor = buscaMaiorValor(V, L);
		
		if(maiorValor < 10)
			printf("1\n");
			
		if(maiorValor >= 10 && maiorValor < 20)
			printf("2\n");
			
		if(maiorValor >= 20)
			printf("3\n");
	}
	
	return 0;
}
