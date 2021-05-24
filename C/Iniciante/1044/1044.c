#include <stdio.h>
#include <stdlib.h>


int main(int argc, char *argv[]) 
{
	int A,B;
	scanf("%d%d", &A, &B);
	if (B==0||A==0)
	{
		return 0;
	}
	
	if (((A%B)==0||(B%A)==0))
	{
		printf("Sao Multiplos\n");
	}
	else 
	{
		printf("Nao sao Multiplos\n");
	}
	return 0;
}