#include <stdio.h>
 
int main() {
 
    int X, Y;
    
    do {
        scanf("%d%d", &X, &Y);
        
        if (X > 0) {
            if (Y > 0)
                printf("primeiro\n");
            else if (Y < 0)
                printf("quarto\n");
        }
        
        else if (X < 0) {
            if (Y > 0)
                printf("segundo\n");
            else if (Y < 0)
                printf("terceiro\n");
        }
    } while (X != 0 && Y != 0);
    
    return 0;
}
