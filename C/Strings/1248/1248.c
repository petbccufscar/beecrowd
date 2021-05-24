#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void insertionSort(char *array, int length)
{
    int i, j;
    char tmp;

    for (i = 1; i < length; ++i) {
        tmp = array[i];
        j = i - 1;
        while (tmp < array[j]) {
            array[j + 1] = array[j];
            --j;
        }
        array[j + 1] = tmp;
    }
}

int main()
{
    int N;
    char diet[28], alreadyEaten[54], dinner[28];
    int dietLength, alreadyEatenLength, dinnerLength;
    int i, j, k, cheater;
    int isInDiet[26], shouldEat[26];

    scanf("%d", &N);
    getchar();

    for (i = 0; i < N; ++i) {
        memset(shouldEat, 1, sizeof(shouldEat));
        memset(isInDiet, 0, sizeof(isInDiet));

        fgets(diet, 28, stdin);
        dietLength = strlen(diet) - 1;

        fgets(alreadyEaten, 28, stdin);
        alreadyEatenLength = strlen(alreadyEaten) - 1;

        fgets(alreadyEaten + alreadyEatenLength, 28, stdin);
        alreadyEatenLength = strlen(alreadyEaten) - 1;

        for (j = 0; j < dietLength; ++j)
            isInDiet[diet[j] - 'A'] = 1;

        cheater = 0;
        for (j = 0; j < alreadyEatenLength && !cheater; ++j) {
            k = alreadyEaten[j] - 'A';

            if (!(isInDiet[k] && shouldEat[k]))
                cheater = 1;
            else
                shouldEat[k] = 0;
        }

        if (cheater)
            puts("CHEATER");
        else {
            insertionSort(diet, dietLength);

            dinnerLength = 0;
            for (j = 0; j < dietLength; ++j) {
                if (shouldEat[diet[j] - 'A'])
                    dinner[dinnerLength++] = diet[j];
            }
            dinner[dinnerLength] = '\0';

            puts(dinner);
        }
    }

    return 0;
}