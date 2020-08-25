#include <stdio.h>
#include <string.h>

int main()
{
    char entrada[500];
    scanf("%[^\n]", entrada);

    if(strlen(entrada) > 80)
        printf("NO\n");
    else
        printf("YES\n");
    return 0;
}