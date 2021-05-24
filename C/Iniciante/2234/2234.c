#include <stdio.h>

int main() {
	int H, P;
	float media;
	
	scanf("%d %d",&H, &P);
	
	media = (float) H/P;
	
	printf("%.2f\n",media);
	
	return 0;
}
