#include <stdio.h>

int main() {
	double X, N[100];
	int i;
	
	scanf("%lf",&X);
	
	N[0] = X;
	printf("N[0] = %.4lf\n",N[0]);
	
	for(i=1;i<100;i++){
		N[i] = X/2;
		printf("N[%d] = %.4lf\n",i,N[i]);
		X = X/2;
	}
	
	return 0;
}
