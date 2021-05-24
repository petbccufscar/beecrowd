#include <stdio.h>

int main(){
    int numero, horasTrabalhadas;
    float valorPorHora;

    scanf("%d %d %f", &numero, &horasTrabalhadas, &valorPorHora);

    printf("NUMBER = %d\n", numero);
    printf("SALARY = U$ %.2f\n", horasTrabalhadas*valorPorHora);

    return 0;
}
