#include <stdio.h>
 
int main() {
 
    int Largura,Comprimento,tipo1,tipo2;

    scanf("%d %d",&Largura,&Comprimento);

    tipo1 = (Largura+Largura-1)*(Comprimento-1)+Largura;
    tipo2 = ((Largura-1)*2) + ((Comprimento-1)*2);

    printf("%d\n", tipo1);
    printf("%d\n", tipo2);

    return 0;
}
