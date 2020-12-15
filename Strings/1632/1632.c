#include <stdio.h>
#include <ctype.h>

void main () {

    int possibilidades;
    int T;
    int i, j;
    char senha[20];

    scanf("%d", &T);

    for (j = 0; j < T; j++){

        scanf(" %s", senha);
        possibilidades = 1;

        for (i = 0; senha[i]; i++){
            if (tolower(senha[i]) == 'a' || tolower(senha[i]) == 'e' || tolower(senha[i]) == 'i' || tolower(senha[i]) == 'o' || tolower(senha[i]) == 's')
                possibilidades *= 3;
            else
                possibilidades *= 2;    
        }

        printf("%d\n", possibilidades);

    }

}