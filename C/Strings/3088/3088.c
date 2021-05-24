#include <stdio.h>


int main()
{

    char string[1000];
    int i = 0;
    while (~scanf("%[^\n]%*c", string))
    {

        i = 0;
        while (string[i])
        {

            if (string[i] == ' ')
                if (string[i + 1] == ',' || string[i + 1] == '.')
                    putchar_unlocked(string[i + 1]), ++i;
                else
                    putchar_unlocked(string[i]);
            else
                putchar_unlocked(string[i]);

            ++i;

        }

        putchar_unlocked('\n');

    }

    return 0;
}