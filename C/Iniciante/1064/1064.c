#include <stdio.h>

int main() 
{
    int contPositivos = 0;
    float valor, soma = 0;

    int i;  
    for( i = 0; i < 6; i++){
      	scanf("%f", &valor);
       	if( valor > 0){
       		soma = soma + valor;
       		contPositivos++;  
       	}
    }

    printf("%d valores positivos\n", contPositivos);
    printf("%.1f\n", soma/contPositivos);

   return (0);
}