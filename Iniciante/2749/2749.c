#include <stdio.h>
#include <string.h>

int main() {
    char tela[39][7];
    char expressao1[] = "|x = 35                               |";
    char expressao2[] = "|               x = 35                |";
    char expressao3[] = "|                               x = 35|";
    int i = 0, j = 0;
    
        for(j = 0; j <= 6; j++) {
            for(i = 0; i <= 38; i++) { 
                tela[i][j] = ' ';
            }
        }

    for (i=0; i<=38; i++) {
        tela[i][0] = '-';
        tela[i][6] = '-';
    }

    for (j=1; j<=5; j++) {
        tela[0][j] = '|';
        tela[38][j] = '|';
    }

    for(j = 0; j <= 6; j++) {
            if (j == 1) {
                printf("%s", expressao1);
            }
            else if (j == 3) {
                printf("%s", expressao2);
            }
            else if (j == 5) {
                printf("%s", expressao3);
            }
            else {
                for(i = 0; i <= 38; i++) {   
                    printf("%c", tela[i][j]);
                }
            }
            printf("\n");
    } 
    return 0;
}