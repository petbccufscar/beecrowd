#include <stdio.h>
#include <math.h>

int main(){

    int a, b, c, area, lado;

    while(1)
    {
        scanf("%d", &a);
        
        if(a==0) 
            break;
        
        else
        {
            scanf("%d%d", &b,&c);
            area = a*b;
            lado = sqrt((area*100)/c);
            printf("%d\n", lado);
        }
    }
    return 0;
}