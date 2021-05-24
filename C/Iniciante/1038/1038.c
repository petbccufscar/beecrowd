#include <stdio.h>

int main(){	
	int cod, quant;
	double total;
	
	scanf("%d %d", &cod, &quant);
	
	switch (cod)
	{
	case 1:
		total = quant * 4;
		break;
	case 2:
		total = quant * 4.5;
		break;
	case 3:
		total = quant * 5;
		break;
	case 4:
		total = quant * 2;
		break;
	case 5:
		total = quant * 1.5;
		break;
	default:
		break;
	}

	printf("Total: R$ %.2f\n", total);		
    return 0;
}
