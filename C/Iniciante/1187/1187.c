#include <stdio.h>
int main() {
    double total, M[12][12];
    char O;
    int i, j;

    total = 0;

    scanf("%c", &O);

    for (i = 0; i < 12; i++) {
        for (j = 0; j < 12; j++) {
            scanf("%lf", &M[i][j]);
        }
    }

    for (i = 0; i < 5; i++) {
        for (j = (i + 1); j <= (10 - i); j++) {
            total += M[i][j];
        }
    }

    if (O == 'S') {
        printf("%.1lf\n", total);
    }

    else if (O == 'M') {
        total = total / 30.0;
        printf("%.1lf\n", total);
    }

    return 0;
}