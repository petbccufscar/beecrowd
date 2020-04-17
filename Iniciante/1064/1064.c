#include <stdio.h>

int main() 
{
    int contPositivos = 0;
    float valor, soma = 0;

    int i ; // controlador da estrutura de repetição 
    for( i = 0; i < 6; i++){
      	scanf("%f", &valor);
       	if( valor > 0){
       		soma = soma + valor;
       		contPositivos++; //  contador++ equivale à contaddor = contador + 1 
       	}
    }

    printf("%d valores positivos\n", contPositivos);
    printf("%.1f\n", soma/contPositivos);

   return (0);
}
