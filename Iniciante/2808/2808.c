#include <stdio.h>

int diferenca(int a, int b)
{
	int aux;

	if(a>b)
		aux = a-b;
	else
		aux = b-a;
	
    return aux;
}

int main()
{
	char inicial[3], final[3];
	int coluna, linha;

    scanf("%s %s", inicial, final);

    coluna = diferenca( inicial[0], final[0]);
    linha = diferenca( inicial[1], final[1]);

    if((coluna == 1 && linha == 2) || (coluna == 2 && linha == 1))
    	printf("VALIDO");

    else 
    	printf("INVALIDO");
        
    return 0;
}