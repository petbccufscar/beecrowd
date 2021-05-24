#include <stdio.h>
#include <stdlib.h>

int main(){
	long long int N, total = 0, ataques = 0, i, j;
	long long int impar;
     
    scanf("%lld", &N);
	
	long long int* estrelas = (long long int*)malloc(N * sizeof(long long int));
	long long int* atacada = (long long int*)malloc(N * sizeof(long long int));

	for (i = 0; i < N; i++){
		scanf("%lld", &estrelas[i]);
		total += estrelas[i];
		atacada[i] = 0;

	}
	
	j = 0;
	while(j >= 0 && j < N ){

		impar = estrelas[j] % 2 ;
		
        if( estrelas[j] > 0){

			estrelas[j]--;
			total--;

			if(atacada[j] == 0){

				ataques++;
				atacada[j] = 1;
			}

		}

    	if(impar)
			j++;
        else
			j--;
		
	
    }

    printf("%lld %lld\n", ataques, total);
     
    return 0;
}