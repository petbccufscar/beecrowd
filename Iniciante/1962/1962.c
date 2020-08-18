#include <stdio.h>
#include <stdlib.h>

int main(){
    int N, T, antes, i;
    scanf("%d",&N);
    for(i=0;i<N;i++){
        scanf("%d",&T);
        if((2015-T) <= 0){
            antes = 1;
        }
        else{
            antes = 0;
        }
        if(antes){
            printf("%d A.C.\n",abs(2015-T+1));
        }
        else{
            printf("%d D.C.\n",abs(2015-T));
        }
    }

    return 0;
}
