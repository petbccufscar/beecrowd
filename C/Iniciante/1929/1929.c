#include <stdio.h>
 
int main() {
 
    int A, B, C, D, v[4], i, j, aux;
    
    scanf("%d%d%d%d", &A, &B, &C, &D);
    
    v[0] = A;
    v[1] = B;
    v[2] = C;
    v[3] = D;
    
    for(j=0;j<4;j++)
        for(i=0;i<3;i++) {
            if (v[i] > v[i+1]) {
                aux = v[i+1];
                v[i+1] = v[i];
                v[i] = aux;
            }
        }
    
    if ((((v[0] + v[1]) > v[3]) || ((v[0] + v[2]) > v[3])) || (((v[1] + v[2]) > v[3]) || ((v[0] + v[1]) > v[2])))
        printf("S\n");
    else
        printf("N\n");
        
    return 0;
}
