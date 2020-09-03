#include <stdio.h>

int main() { 

    float a, b;
    double c, d;
    
    scanf("%f %f %lf %lf", &a, &b, &c, &d);
    
    printf("A = %f, B = %f\n", a, b);
    printf("C = %lf, D = %lf\n", c, d);
    
    printf("A = %.1f, B = %.1f\n", a, b);
    printf("C = %.1lf, D = %.1lf\n", c, d);
    
    printf("A = %.2f, B = %.2f\n", a, b);
    printf("C = %.2lf, D = %.2lf\n", c, d);
    
    printf("A = %.3f, B = %.3f\n", a, b);
    printf("C = %.3lf, D = %.3lf\n", c, d);
    
    printf("A = %.3E, B = %.3E\n", a, b);
    printf("C = %.3E, D = %.3E\n", c, d);
    
    printf("A = %.0f, B = %.0f\n", a, b);
    printf("C = %.0lf, D = %.0lf\n", c, d);
    
    return 0;
}
