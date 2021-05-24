#include <stdio.h>
 
int main() {
 
    float salario, reajuste;
    int pct;
    scanf("%f", &salario);
    
    if (salario <= 400)
        pct = 15;
    else if (salario <= 800)
        pct = 12;
    else if (salario <= 1200)
        pct = 10;
    else if (salario <= 2000)
        pct = 7;
    else
        pct = 4;
 
    reajuste = salario * pct / 100;
    salario = salario + reajuste;
    printf("Novo salario: %0.2f\nReajuste ganho: %0.2f\nEm percentual: %d %%\n", salario, reajuste, pct);
    return 0;
}
