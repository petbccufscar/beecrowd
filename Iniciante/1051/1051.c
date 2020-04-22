/*
Para printar apenas duas casas: %.2f
f por ser Float e .2 para printar 2 casas após a virgula
*/

#include <stdio.h>

int main(){
	float salario, imposto;
    	scanf("%f", &salario);

	if (salario >= 0 && salario <= 2000.01)
		printf("Isento\n");

	// Desconsidera os 2000 que são isentos e calcula 8% do que sobrou
	if (salario > 2000 && salario <= 3000){
	    imposto = ((salario-2000) * 0.08);
	    printf("R$ %.2f\n", imposto); 
	}

	// Calcula 8% dentro da parte do salario que esta entre 2000.01 e 3000.00 (1000.00)
	// E calcula 18% do que sobrou, que está entre 3000.01 e 4500.00
	if ( salario > 3000 && salario <= 4500){
	    imposto =( (1000*0.08) + ((salario-3000)*0.18) );
	    printf("R$ %.2f\n", imposto);
	}

	// Calcula 8% dentro da parte do salario que esta entre 2000.01 e 3000.00 (1000.00)
	// Calcula 18% dentro da parte do salario que esta entre 3000.01 e 4500.00 (1500.00)
	// E calcula 28% do que sobrou, que é maior que 4500.00
    if ( salario > 4500){
	    imposto = ( (1000*0.08) + (1500*0.18) + ((salario-4500)*0.28) );
	    printf("R$ %.2f\n", imposto);
	}

    return 0;
}
