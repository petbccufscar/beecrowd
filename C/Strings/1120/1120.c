#include <stdio.h>
#include <string.h>


int main (){
    char digito, valor[200];
    int n, i, j;

    scanf("%c", &digito);
    scanf("%s", valor);

    while (digito != '0'){
        n = strlen(valor);
        for (i = 0; i < n; i++) {
            if (valor[i] == digito) {
                for (j = i; j < n; j++)
                    valor[j] = valor[j+1];
                valor[n-1] = 0;
                n--;
                i--;
            }
        }

        for (i = 0; i < n-1; i++) {
            if (valor[i] == '0') {
                for (j = i; j < n; j++)
                    valor[j] = valor[j+1];
                valor[n-1] = 0;
                n--;
                i--;
            }
            
            else
                break;
        }

        if (n == 0) {
            valor[0] = '0';
            valor[1] = '\0';
        }

        printf("%s\n", valor);

        scanf(" %c", &digito);
        scanf("%s", valor);
    }
    return 0;
}