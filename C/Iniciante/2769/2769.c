#include <stdio.h>
 
int main() {
    int N, x1, x2, soma1, soma2, aux1, aux2, i;
    
    while(scanf("%d", &N) != EOF) {
        int a1[N], a2[N], t1[N], t2[N];
        
        scanf("%d %d", &t1[0], &t2[0]);
        for(i = 0; i < N; i++) {
            scanf("%d", &a1[i]);
        }
        
        for(i = 0; i < N; i++) {
            scanf("%d", &a2[i]);
        }
        
        for(i = 1; i < N; i++) {
            scanf("%d", &t1[i]);
        }
        
        for(i = 1; i < N; i++) {
            scanf("%d", &t2[i]);
        }
        
        scanf("%d %d", &x1, &x2);
        
        soma1 = t1[0]+a1[0];
        soma2 = t2[0]+a2[0];

        for(i = 1; i < N; i++) {
            aux1 = soma1;
            aux2 = soma2;
            
            if (aux1+a1[i] > aux2+t2[i]+a1[i])
                soma1 = aux2+t2[i]+a1[i];
            else
                soma1 += a1[i];

            if (aux2+a2[i] > aux1+t1[i]+a2[i])
                soma2 = aux1+t1[i]+a2[i];
            else
                soma2 += a2[i];
        }
        
        if (soma1+x1 < soma2+x2) {
            soma1 += x1;
            printf("%d\n", soma1);
        }
        else {
            soma2 += x2;
            printf("%d\n", soma2);
        }
    }
 
    return 0;
}
