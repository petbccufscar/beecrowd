#include <stdio.h>

int main() {
    int produtos, codigo, quantidade, i;
    float total = 0;

    scanf("%d", &produtos);

    for (i = 0; i < produtos; i++) {
        scanf("%d %d", &codigo, &quantidade);

        if (codigo == 1001)
            total += quantidade * 1.5;

        else if (codigo == 1002)
            total += quantidade * 2.5;

        else if (codigo == 1003)
            total += quantidade * 3.5;

        else if (codigo == 1004)
            total += quantidade * 4.5;

        else if (codigo == 1005)
            total += quantidade * 5.5;
    }

    printf("%.2f\n", total);

    return 0;
}