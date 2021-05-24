#include <stdio.h>

//dividir a distância entre os dois Palantír’s, pela soma do diâmetro dos mesmos.

int main(){
    float N, X, Y;
    float icm;

    scanf("%f %f %f",&N,&X,&Y);
    icm = (N / (X + Y));
    printf("%.2f\n",icm);

    return 0;
}