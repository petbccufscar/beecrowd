#include <stdio.h>

int main(){
    int i, copo, feijao_pos;

    for(i = 0; i < 4; i++){
        scanf("%d",&copo);
        if(copo == 1){
            feijao_pos = i + 1;
        }
    }

    printf("%d\n",feijao_pos);
    return 0;
}