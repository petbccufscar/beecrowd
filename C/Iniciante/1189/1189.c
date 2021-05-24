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

    for (i = 1; i <= 10; i++) {
        for (j = 0; j <= offset; j++) {
            total += M[i][j];
        }

        if(i < 5) {
            offset++;
        } else if (i >= 6) {
            offset--;
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