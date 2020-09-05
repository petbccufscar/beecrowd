#include <stdio.h>

int main() {
	int X, Y, Z, D;
	
	scanf("%d.%d.%d-%d", &X, &Y, &Z, &D);
	
	if(X<10)
		printf("00%d\n",X);
	else{
		if(X<100)
			printf("0%d\n",X);
		
		else
			printf("%d\n",X);
	}
	
	if(Y<10)
		printf("00%d\n",Y);
	else{
		if(Y<100)
			printf("0%d\n",Y);
		
		else
			printf("%d\n",Y);
	}
	
	if(Z<10)
		printf("00%d\n",Z);
	else{
		if(Z<100)
			printf("0%d\n",Z);
		
		else
			printf("%d\n",Z);
	}
	
	if(D<10)
		printf("0%d\n",D);
	else
		printf("%d\n",D);
	
	return 0;
}
