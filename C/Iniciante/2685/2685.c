#include <stdio.h>
 
int main() {
 
    int m;
    
    while (scanf("%d", &m) != EOF) {
        if ((m >= 0) && (m < 90))
            printf("Bom Dia!!\n");
        else if ((m >= 90) && (m < 180))
            printf("Boa Tarde!!\n");
        else if ((m >= 180) && (m < 270))
            printf("Boa Noite!!\n");
        else if ((m >= 270) && (m < 360))
            printf("De Madrugada!!\n");
        else
            printf("Bom Dia!!\n");
    }
 
    return 0;
}
