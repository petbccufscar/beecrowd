#include <stdio.h>

int main(){
	int A, B, terceiraCarta;
	scanf("%d %d",&A,&B);
	
	if(A == B)
		terceiraCarta = A;
	
	else{
		if(A>B)
			terceiraCarta = A;
		if(B>A)
			terceiraCarta = B;
	}
	
	printf("%d\n",terceiraCarta);
	
	return 0;
}
