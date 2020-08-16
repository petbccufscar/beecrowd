#include <stdio.h>
#include <string.h>

int main() {
    char numero[10];
    int i;

    scanf("%s", numero);

    for (i = (strlen(numero) - 1); i >= 0; i--) {
        printf("%c", numero[i]);
    }

    printf("\n");

    return 0;
}