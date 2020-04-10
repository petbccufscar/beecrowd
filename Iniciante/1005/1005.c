#include <stdio.h>
#include <stdlib.h>


int main(int argc, char *argv[]) 
{
	float a,b;
	scanf("%f%f", &a, &b);
	
	printf("MEDIA = %.5f\n", ((a*3.5)+(b*7.5))/11);
	
	
	return 0;
}