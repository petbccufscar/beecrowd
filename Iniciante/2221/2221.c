#include <stdio.h>

int main() {
	int T, B;
	int A[2], D[2], L[2], Golpe[2];
	int i;
	
	scanf("%d",&T);
	
	for(i=1; i<=T; i++){
		scanf("%d",&B);
		scanf("%d %d %d",&A[0], &D[0], &L[0]);
		scanf("%d %d %d",&A[1], &D[1], &L[1]);
		
		Golpe[0] = (A[0] + D[0])/2;
		Golpe[1] = (A[1] + D[1])/2;
		
		if(L[0]%2 == 0)
			Golpe[0] = Golpe[0] + B;
			
		if(L[1]%2 == 0)
			Golpe[1] = Golpe[1] + B;
			
		if(Golpe[0] == Golpe[1])
			printf("Empate\n");
		
		else{
			
			if(Golpe[0] > Golpe[1])
				printf("Dabriel\n");
			else
				printf("Guarte\n");
				
		}
	}
	
	return 0;
}
