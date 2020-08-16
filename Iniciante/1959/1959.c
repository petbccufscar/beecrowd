#include <stdio.h>

int main(){

    int nroLados;
    long long int tamLados, perimetro;
    scanf("%d %lld", &nroLados, &tamLados);

    perimetro = nroLados * tamLados;

    printf("%lld\n", perimetro);

    return 0;
}