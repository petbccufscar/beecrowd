#include <stdio.h>

int main() {
	int X, Y, Z, D;
	
	scanf("%d.%d.%d-%d", &X, &Y, &Z, &D);
	
	printf("%03d\n",X);
	printf("%03d\n",Y);
	printf("%03d\n",Z);
	printf("%02d\n",D);
	
	return 0;
}
