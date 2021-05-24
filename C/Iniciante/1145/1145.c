#include <stdio.h>

int main() {

    int X, Y, i;

    scanf("%d %d", &X, &Y);

    for (i = 1; i <= Y; i++) {
        printf("%d", i);

        if (i % X == 0)
            printf("\n");
        else
            printf(" ");
    }

    return 0;
}