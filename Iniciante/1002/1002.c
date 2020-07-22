#include <stdio.h>


int main(){
    
    double area, raio, pi;
    
    pi = 3.14159;

    scanf("%lf",&raio);
    area = raio*raio * pi;
    printf("A=%.4lf\n",area);

    return 0;
}