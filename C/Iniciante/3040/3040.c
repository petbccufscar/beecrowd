#include <stdio.h>

int main()
{

    int casos, altura, tronco, galhos, i;

    scanf("%d", &casos);

    for (i = 0 ; i < casos; ++i)
    {

        scanf("%d %d %d", &altura, &tronco, &galhos);

        if (altura >= 200 && altura <= 300)
            if (tronco >= 50)
                if (galhos >= 150)
                {
                    printf("Sim\n");
                    continue;
                }

        printf("Nao\n");

    }

    return 0;

}