#include <stdio.h>
#include <string.h>

int eye(int R, int G, int B) {
    return (0.3 * R) + (0.59 * G) + (0.11 * B);
}

int mean(int R, int G, int B) {
    return (R + G + B) / 3;
}

int max(int R, int G, int B) {
    if (R >= G && R >= B) {
        return R;
    }
    else if (G >= R && G >= B) {
        return G;
    }
    else {
        return B;
    }
}

int min(int R, int G, int B) {
    if (R <= G && R <= B) {
        return R;
    }
    else if (G <= R && G <= B) {
        return G;
    }
    else {
        return B;
    }
}
 
int main() {
 
    int casos, i;
    int R, G, B, P;
    char abordagem[4];

    scanf("%d", &casos);

    for (i = 1; i <= casos; i++) {
        scanf("%s", abordagem);
        scanf("%d %d %d", &R, &G, &B);

        if (strcmp(abordagem,"eye") == 0) {
            P = eye(R, G, B);
        }
        else if (strcmp(abordagem, "mean") == 0) {
            P = mean(R, G, B);
        }
        else if (strcmp(abordagem, "max") == 0) {
            P = max(R, G, B);
        }
        else if (strcmp(abordagem, "min") == 0) {
            P = min(R, G, B);
        }

        printf("Caso #%d: %d\n", i, P);
    }

    return 0;
}