#include <stdio.h>

int main() {

    int n, d, p, num1, evento, conf, i, j;

    while (scanf("%d %d", &n, &d) != EOF) {
        int data_dia[d], data_mes[d], data_ano[d];

        evento = -1;
        conf = 0;

        for (i=0;i<d;i++) {
            scanf("%d/%d/%d", &data_dia[i], &data_mes[i], &data_ano[i]);

            num1 = 0;
            for (j=0;j<n;j++) {
                scanf("%d", &p);
                if (p==1)
                    num1++;
            }

            if ((num1 == n) && (!conf)) {
                evento = i;
                conf = 1;
            }
        }

        if (evento != -1)
            printf("%d/%d/%d\n", data_dia[evento], data_mes[evento], data_ano[evento]);

        else
            printf("Pizza antes de FdI\n");
    }

    return 0;
}
