#include <stdio.h>
 
int main() {
 
    int Nota_A, Nota_B, Media;

    scanf("%d %d",&Nota_A,&Media);

    Nota_B = 2*Media - Nota_A;

    printf("%d\n",Nota_B);

    return 0;
}