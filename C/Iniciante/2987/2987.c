#include <stdio.h>

int main(){
    int numero;
    char letra;
    scanf("%c",&letra);
    numero = letra;
    numero = numero - 64;
    printf("%d\n",numero);
    return 0;
}