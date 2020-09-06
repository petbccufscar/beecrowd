#include <stdio.h>
#include <string.h>

int placaValida(char *placa) {
    int i;

    if (strlen(placa) != 8)
        return 0;
    
    for (i = 0; i < 3; i++)
        if (placa[i] < 'A' || placa[i] > 'Z')
                return 0;
    
    if (placa[3] != '-')
        return 0;

    for (i = 4; i < 8; i++)
        if (placa[i] < '0' || placa[i] > '9')
            return 0;
    
    return 1;
}

int main() {

    int N, i;
    char placa[100];

    scanf("%d", &N);

    for (i = 0; i < N; i++) {
        scanf("%s", placa);

        if (placaValida(placa) == 1) {
            
            if (placa[7] == '1' || placa[7] == '2')
                printf("MONDAY\n");

            else if (placa[7] == '3' || placa[7] == '4')
                printf("TUESDAY\n");

            else if (placa[7] == '5' || placa[7] == '6')
                printf("WEDNESDAY\n");

            else if (placa[7] == '7' || placa[7] == '8')
                printf("THURSDAY\n");

            else if (placa[7] == '9' || placa[7] == '0')
                printf("FRIDAY\n");

        } else {
            printf("FAILURE\n");
        }
    }

    return 0;
}