#include <stdio.h>

int main() {
    unsigned long long X;
    int max, seq, N;
    scanf("%d", &N);

    while(N--) {
        scanf("%llu", &X);
        max = 0;
        seq = 0;

        while (X > 0) {
            if ((X & 1) == 1) {
                seq++;
                if (seq > max) {
                    max = seq;
                }
            } else {
                seq = 0;
            }
            X >>= 1;
        }

        printf("%d\n", max);
    }

    return 0;
}