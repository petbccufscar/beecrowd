#include<stdio.h>
#include<math.h>

int main()
{
    int  x;
    long long int num;
    
    while (scanf("%lld", &num)!=EOF)
    {
        if (num==1) 
            printf("0\n");
        else{
            x = log2(num);
            printf("%d\n", x);       
        }
    }
    return 0;
}
