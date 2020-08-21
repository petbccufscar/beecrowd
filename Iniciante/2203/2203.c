#include <stdio.h>
#include <math.h>
 
int main() {

    int Xf, Yf, Xi, Yi, V, R1, R2;
    double distancia, distX, distY;
 
    while (scanf("%d %d %d %d %d %d %d", &Xf, &Yf, &Xi, &Yi, &V, &R1, &R2) != EOF) {

        distX = pow((Xi - Xf), 2);
        distY = pow((Yi - Yf), 2);

        distancia = sqrt(distX + distY);

        distancia += V * 1.5;

        if (distancia <= (R1 + R2)) {
            printf("Y\n");
        } else {
            printf("N\n");
        }
    }
 
    return 0;
}