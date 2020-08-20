#include <stdio.h>

int main()
{
    int casos, tam;
    char galopeira[10000];

    scanf("%d", &casos);
    
    while(casos>0)
    {
        scanf("%s", galopeira);
    
        tam = strlen(galopeira);
    
        printf("%.2lf\n", tam*.01);
    
        casos--;
    }
    return 0;
}