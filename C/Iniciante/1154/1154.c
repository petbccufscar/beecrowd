#include <stdio.h>

int main() {

    int idade, n = 0;
    double soma = 0;

    scanf("%d", &idade);

    while (idade >= 0) {
        
        soma += idade;
        n++;
        scanf("%d", &idade);
    }
    
    printf("%.2f\n", soma/n);

    return 0;
}