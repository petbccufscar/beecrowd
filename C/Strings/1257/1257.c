#include <stdio.h>

int main()
{
    char linha[51];
    int n, l, i, j, k, total;

    scanf("%d", &n);
    for(i=0;i<n;i++){
        scanf("%d%*c", &l);
        total = 0;
        for(j=0;j<l;j++){
            scanf("%s%*c", linha);
            for(k=0;k<linha[k] != '\0';k++){
                total += linha[k] - 65 + j + k;
            }  
        }
        printf("%d\n", total);
    }
    return 0;
}