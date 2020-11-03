#include <stdio.h>

int main()
{

    int i, j, t1, t2, m, n;
    char n1[55], n2[55];
    scanf("%d", &n);
    for (i = 0; i < n; i++)
    {
        scanf("%s %s", &n1, &n2);
        t1 = strlen(n1);
        t2 = strlen(n2);
        if (t1 < t2)
            m = t2;
        else
            m = t1;
        for (j = 0; j < m; j++)
        {
            if (j < t1)
                printf("%c", n1[j]);
            if (j < t2)
                printf("%c", n2[j]);
        }
        printf("\n");
    }
    return 0;
}
