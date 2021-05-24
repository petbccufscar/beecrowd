#include <stdio.h>

int main() {
	int N;
	
	while(scanf("%d",&N) != EOF){
		int matriz[N][N];

		int centro = N/2;
		int internoMin = N/3;
		int internoMax = (N-1) - internoMin;
		
		int linha, coluna;
		
		for(linha=internoMin; linha<=internoMax; linha++){
			for(coluna=internoMin; coluna<=internoMax; coluna++){
				matriz[linha][coluna] = 1;
			}
		}
		
		for(linha=0; linha<N; linha++){
			
			for(coluna=0; coluna<N; coluna++){
				
				if(linha<internoMin || linha>internoMax){
					if(linha == coluna){
						matriz[linha][coluna] = 2;
						
					}else if(linha+coluna == N-1){
						matriz[linha][coluna] = 3;

					}else{
						matriz[linha][coluna] = 0;
					}
				}
				
				else{
					if(coluna<internoMin || coluna>internoMax){
						matriz[linha][coluna] = 0;
					}
				}
			
			}
			
		}
		
		matriz[centro][centro] = 4;
		
		for(linha=0; linha<N; linha++){
			for(coluna=0; coluna<N; coluna++){
				printf("%d",matriz[linha][coluna]);
			}
			printf("\n");
		}
		printf("\n");
		
	}
	
	return 0;
}
