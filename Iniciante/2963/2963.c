#include <stdio.h>
 
int main() {
    int candidatos, carlos, i;
    
    scanf("%d %d", &candidatos, &carlos);
        candidatos = candidatos - 1;
    while (candidatos--) {
        scanf("%d", &i);
        if (i>carlos) {
            carlos = -1;
        }
    }
    if (carlos > -1) {
        printf("S\n");
    }
    else {
        printf("N\n");
    }

    return 0;
}