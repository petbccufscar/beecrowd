#include <stdio.h>
#include <math.h>

int main() {
    int C, N, M, i;

    scanf("%d", &C);
    
    for(i = 0; i < C; i++) {
        scanf("%d %d", &N, &M);
        printf("%.f\n", (floor(M * log10(N))) + 1);
    }
    
    return 0;
}
