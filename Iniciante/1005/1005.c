#include <stdio.h>
#include <stdlib.h>


int main(int argc, char *argv[]) 
{
	float A, B;
	scanf("%f%f", &A, &B);
	
	printf("MEDIA = %.5f\n", ((A*3.5)+(B*7.5))/11);
	
	
	return 0;
}