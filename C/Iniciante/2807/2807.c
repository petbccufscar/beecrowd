#include <stdio.h>
 
int main() {
    
    int N, i; 
    int fibonacci[40];
    
    scanf("%d", &N);
    
    fibonacci[0]=1;
    fibonacci[1]=1;
    
    for(i=2; i<N; i++)
        fibonacci[i] = fibonacci[i-1] + fibonacci[i-2];
    
    for(i = N-1; i>=0; i--){
        
        if(i>0)
            printf("%d ", fibonacci[i]);
            
        else 
            printf("%d\n", fibonacci[i]);
    }
        
    return 0; 
}