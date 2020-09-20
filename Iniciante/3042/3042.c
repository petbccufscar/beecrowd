#include <stdio.h>

int main() {
	int M, L, C, R;
	int numToques, posicao, i;
		
	scanf("%d",&M);
	
	while(M != 0){
		posicao = 0;
		numToques = 0;
		
		for(i=1; i<=M; i++){
			scanf("%d %d %d", &L, &C, &R);
			
			if(posicao == 1){
				
				if(L == 1){
					
					if(C == 1){
						numToques = numToques + 2;
						posicao = 2;
					}
					
					if(R == 1){
						numToques = numToques + 1;
						posicao = 0;
					}
					
				}
			}
			
			if(posicao == 0){
				
				if(C == 1){
					
					if(L == 1){
						numToques = numToques + 1;
						posicao = 2;
					}
					
					if(R == 1){
						numToques = numToques + 1;
						posicao = 1;
					}
					
				}
			}
			
			if(posicao == 2){
				
				if(R == 1){
					
					if(L == 1){
						numToques = numToques + 1;
						posicao = 0;
					}
					
					if(C == 1){
						numToques = numToques + 2;
						posicao = 1;
					}
					
				}
			}
				
		}
		
		printf("%d\n",numToques);
		
		scanf("%d",&M);
		
	}
	
	return 0;
}
