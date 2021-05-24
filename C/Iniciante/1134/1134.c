#include <stdio.h>

int main() {
    int alcool, gasolina, diesel, entrada;
    alcool = 0;
    gasolina = 0;
    diesel = 0;

    do {
        scanf("%d", &entrada);

        if(entrada == 1)
            alcool++;
        else if(entrada == 2)
            gasolina++;
        else if(entrada == 3)
            diesel++;
    }
    while(entrada != 4);

    printf("MUITO OBRIGADO\n");
    printf("Alcool: %d\n", alcool);
    printf("Gasolina: %d\n", gasolina);
    printf("Diesel: %d\n", diesel);

    return 0;
}