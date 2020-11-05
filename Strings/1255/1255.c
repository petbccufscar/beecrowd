#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int main() {
    int counter[26], vezes = 0, i, j;
    char texto[201];

    scanf("%d", &vezes);

    for (j = 0; j < vezes; j++){
        int maior = -1;
        memset(&counter, 0, 26*sizeof(int));
        scanf(" %[^\n]", texto);
        
        for(i = 0; texto[i]; i++)
			texto[i] = tolower(texto[i]);

        for (i = 0; i < strlen(texto); i++)
            counter[(texto[i])-97]++;
        
        for (i = 0; i < 26; i++)
            if (counter[i] > maior)
                maior = counter[i];
        
        for (i = 0; i < 26; i++)
            if (counter[i] == maior)
                printf("%c", i+97);

   		printf("\n");
    }
    
    return 0;
}