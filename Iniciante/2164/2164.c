#include <math.h>
#include <stdio.h>

int main(){

    double part1, part2, part3, potencia1, potencia2;
    double n;
     
    scanf("%lf", &n);

    part1 = (1+sqrt(5))/2;
    part2 = (1-sqrt(5))/2;
    potencia1 = pow(part1, n);
    potencia2 = pow(part2, n);
    part3 = ((potencia1 - potencia2)/sqrt(5));


    printf("%.1lf\n", part3);      

    return 0;
}




   
