#include <stdio.h>

int main() 
{

   char nome[]="";
   float salario, vendas, salariofinal; 

   scanf("%s %f %f", nome, &salario, &vendas);

   salariofinal = salario + (vendas * 0.15f);

   printf("TOTAL = R$ %.2f\n", salariofinal);

   return (0);
}