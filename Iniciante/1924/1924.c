#include <stdio.h>
 
int main() {
 
    int n, i;
    char S[100];
    
    scanf("%d", &n);
    
    for(i=0;i<n;i++)
        fgets(S, sizeof(S), stdin);
        
    printf("Ciencia da Computacao\n");
 
    return 0;
}
