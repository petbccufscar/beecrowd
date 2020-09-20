#include <stdio.h>
 
int main() {
    int angulo_horas, angulo_minutos;
 
    while(scanf("%d %d", &angulo_horas, &angulo_minutos) != EOF)
        printf("%02d:%02d\n", (angulo_horas/30), (angulo_minutos/6));
    
    return 0;
}