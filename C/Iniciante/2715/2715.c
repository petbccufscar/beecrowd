#include <stdio.h>

int main(){

	long long int N, X[1000000], somaGugu, somaRangel, i, j;

	while(scanf("%lld", &N) != EOF){

		for(i = 0; i < N; i++){
			scanf("%lld", &X[i]);
		}
		
		i = 0;
		j = N-1;
		somaGugu = 0;
		somaRangel = 0;

		while(i<=j){
			
			if((somaRangel + X[i]) <= (somaGugu + X[j])){

				somaRangel += X[i];
				i++;
			}

			else{
				somaGugu += X[j];
				j--;
				
			}
		}

		if(somaRangel >= somaGugu)
			printf("%lld\n", somaRangel - somaGugu);

		else
			printf("%lld\n", somaGugu - somaRangel);
	}

	return 0;
}