#include <stdio.h>
#include <string.h>

int main()
{
    char sentenca[50];
    int i, count;
    int tam;

    while (gets(sentenca) != NULL)
    {
        tam = strlen(sentenca);
        count = 1;
        for (i = 0; i < tam; i++)
        {
            if (sentenca[i] == ' ')
            {
                sentenca[i] = sentenca[i];
            }
            else if (count % 2 != 0 && (sentenca[i] >= 'a' && sentenca[i] <= 'z'))
            {
                sentenca[i] -= 32;
                count++;
            }
            else if (count % 2 == 0 && (sentenca[i] >= 'A' && sentenca[i] <= 'Z'))
            {
                sentenca[i] += 32;
                count++;
            }
            else
            {
                sentenca[i] = sentenca[i];
                count++;
            }
        }
        printf("%s\n", sentenca);
    }

    return 0;
}