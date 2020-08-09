#include <stdio.h>
#include <stdlib.h>
 
int main() {
    int n, i, algoz = 0, menor = 999;
    int *v;
    
    scanf("%d",&n);
    v = (int *) malloc(n * sizeof(int));
    for (i=0;i<n;i++){
        scanf("%d",&v[i]);
        if(v[i] < menor){
            menor = v[i];
            algoz = i + 1;
        }
    }
    printf("%d\n",algoz);

    return 0;
}