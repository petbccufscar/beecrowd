#include <stdio.h>
#include <string.h>

int main() {
    char numero[200];
    int n, numLed, i, j;
    
    scanf("%d", &n);
    
    for(i = 0; i < n; i++) {
        numLed = 0;
        scanf(" %200[^\n]", numero);
        for(j = 0; j < strlen(numero); j++) {
            switch (numero[j]) {
                case '0':
                    numLed += 6;
                    break;
                case '1':
                    numLed += 2;
                    break;
                case '2':
                    numLed += 5;
                    break;
                case '3':
                    numLed += 5;
                    break;
                case '4':
                    numLed += 4;
                    break;
                case '5':
                    numLed += 5;
                    break;
                case '6':
                    numLed += 6;
                    break;
                case '7':
                    numLed += 3;
                    break;
                case '8':
                    numLed += 7;
                    break;
                case '9':
                    numLed += 6;
            }
        }
        
        printf("%d leds\n", numLed);
    }
 
    return 0;
}
