#include <stdio.h>
 
int main() {
    int horas, minutos;
 
    while(scanf("%d %d", &horas, &minutos) != EOF)
        printf("%02d:%02d\n", (horas/30), (minutos/6));
    
    return 0;
}