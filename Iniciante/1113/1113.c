#include <stdio.h>

int main()
{   
    int X, Y;
    
    scanf("%d %d", &X, &Y);
        
    while(X!=Y){
        if(X>Y){
            printf("Decrescente\n");
        }
        else if(X<Y){
            printf("Crescente\n");
        }
        scanf("%d %d", &X, &Y);
    }
    
    return 0;
}
