#include <stdio.h>
int main() {
    double total, M[12][12];
    char O;
    int i, j, offset;

    total = 0;
    offset = 0;

    scanf("%c", &O);

    for (i = 0; i < 12; i++) {
        for (j = 0; j < 12; j++) {
            scanf("%lf", &M[i][j]);
        }
    }

    for (i = 11; i >= 7; i--) {
        for (j = (1 + offset); j <= (10 - offset); j++) {
            total += M[i][j];
        }
        offset++;
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