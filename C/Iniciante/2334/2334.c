#include <stdio.h>

int main (){
	long double qntPatinhos;

	while (1){
		scanf("%LF", &qntPatinhos);

		if (qntPatinhos == -1)
			break;

		if (qntPatinhos == 0)
			printf("0\n");
		else
			printf("%.LF\n", --qntPatinhos);
	}

	return 0;
}