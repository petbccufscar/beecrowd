#include <stdio.h>

int main(){
    int i = 1, j = 7;
    int k ;

    while(i<=9){
        for(k=0;k<3;k++){
            printf("I=%d J=%d\n",i,(j-k));
        }
        i += 2;
        j += 2;
    }

    return 0;
}