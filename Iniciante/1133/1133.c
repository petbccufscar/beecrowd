#include <stdio.h>

int main() {
    int X, Y, i;
    
    scanf("%d %d", &X, &Y);
    
    if(X > Y)
        for(i = Y+1; i < X; i++)
            if(i % 5 == 2 || i % 5 == 3)
                printf("%d\n", i);

    else if(Y >= X)
        for(i = X+1; i < Y; i++)
            if(i % 5 == 2 || i % 5 == 3)
                printf("%d\n", i);
    
    return 0;
}