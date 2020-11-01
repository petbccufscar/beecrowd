#include <stdio.h>
 
int main() {
    int x1, y1, x2, y2, n, x, y, numTestes, contador, i;
    
    numTestes = 0;
    while (!(x1 == 0 && y1 == 0 && x2 == 0 && y2 == 0)) {
        scanf("%d", &x1);
        scanf("%d", &y1);
        scanf("%d", &x2);
        scanf("%d", &y2);
        contador = 0;
        if (!(x1 == 0 && y1 == 0 && x2 == 0 && y2 == 0)) {
            scanf("%d", &n);
            for(i=0;i<n;i++) {
                scanf("%d", &x);
                scanf("%d", &y);
                if (x >= x1 && x <= x2) {
                    if (y <= y1 && y >= y2) {
                        contador++;
                    }
                }
            }
            
            numTestes++;
            printf("Teste %d\n%d\n", numTestes, contador);
        }
    }
 
    return 0;
}
