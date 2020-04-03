#include <stdio.h>
 
int main() {
 
    double a, b, c, media;
    scanf("%lf%lf%lf", &a, &b, &c);
    media = (2*a + 3*b + 5*c)/10;
    printf("MEDIA = %.1lf\n", media);
 
    return 0;
}
