#include <stdio.h>
#include <stdio.h>

int main(){
	int T, N, i;
     
    scanf("%d", &T);

    while( T > 0){
        
        for(i=0; i < T; i++){
            scanf("%d", &N);
            
            if ( N%2 == 0 )
                printf("%d\n", N*2 - 2);
            else
                printf("%d\n", N*2 - 1);
        }

    scanf("%d", &T);
    }
     
    return 0;
}