#include <stdio.h>

int main() {
	int N, i;
	long double soma=0;
	
	scanf("%d",&N);
	
	int custo[N], periodo[N];
	
	for(i=0; i<N; i++){
		scanf("%d %d",&custo[i],&periodo[i]);
		soma = soma + ( (float)custo[i] / (float)periodo[i] );
	}
	
	if(soma <= 1)
		printf("OK\n");
	
	else
		printf("FAIL\n");
	
	return 0;
}
