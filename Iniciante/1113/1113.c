#include <stdio.h>

int main()
{   
    int X, Y;
    
    scanf("%d %d", &X, &Y);
    if(X>Y){
            printf("Decrescente\n");
        }
    else if(X<Y){
            printf("Crescente\n");
        }
    else if(X==Y){
        return 0;
    }
        
    while(X!=Y){
        scanf("%d %d", &X, &Y);
        if(X>Y){
            printf("Decrescente\n");
        }
        else if(X<Y){
            printf("Crescente\n");
        }
    }
    
    return 0;
}
