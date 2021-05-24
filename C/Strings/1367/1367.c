#include <stdio.h>
#include <string.h>

int main(int argc, char const *argv[])
{
    int n, tempo, i, corretos, tempo_total;
    int incorrect[26], correct[26];
    char identificador, julgamento[10];

    while(scanf("%d", &n) && n) {

        corretos = 0; tempo_total = 0;
        memset(incorrect, 0, sizeof(incorrect));
        memset(correct, 0, sizeof(correct));

        for (i = 0; i < n; ++i) {
            getchar();
            scanf("%c %d %s", &identificador, &tempo, julgamento);

            if(strcmp("correct", julgamento) == 0 && correct[(int)identificador - 65] == 0)
                correct[(int)identificador - 65] = tempo;

            if(strcmp("incorrect", julgamento) == 0 && correct[(int)identificador - 65] == 0)
                incorrect[(int)identificador - 65] += 20;
        }

        for (i = 0; i < 26; ++i) {
            if(correct[i] != 0){
                corretos++;
                tempo_total += (correct[i] + incorrect[i]);
            }
        }

        printf("%d %d\n", corretos, tempo_total);
    }

    return 0;
}