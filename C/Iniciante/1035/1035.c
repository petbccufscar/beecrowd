#include <stdio.h>
#include <stdbool.h>

int main() {
	int A, B, C, D;
	int soma1=0, soma2=0;
	bool soma1_maior=false, par=false;

	scanf("%d %d %d %d", &A, &B, &C, &D);

	soma1 = C+D;
	soma2 = A+B;
	if(soma1 > soma2)
		soma1_maior = true;

	if(A%2 == 0)
		par = true;

	if(B>C && D>A && soma1_maior && C>=0 && D>=0 && par)
		printf("Valores aceitos\n");
	else
		printf("Valores nao aceitos\n");

	return 0;

}
