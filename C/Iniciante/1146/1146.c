#include <stdio.h>

int main() {

    int X, i;

    scanf("%d", &X);

    while (X != 0) {

        for(i = 1; i < X; i++)
            printf("%d ", i);
        
        printf("%d\n", X);

        scanf("%d", &X);
    }

    return 0;
}