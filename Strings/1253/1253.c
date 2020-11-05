#include <stdio.h>
#include <stdlib.h>
 
int main()
{
    int i, deslocamento = 0, casos = 0, aux = 0;
    char cifra[50];
    scanf("%d", &casos);
    while(casos--){
        scanf("%s", cifra);
        scanf("%d", &deslocamento);
        for (i = 0; i < 50; i++){
            if (cifra[i] == '\0')
                break;
            if ((cifra[i] - deslocamento) < 65)
                aux = (cifra[i] - deslocamento) + 26;
            else
                aux = cifra[i] - deslocamento;
        printf("%c", aux);
        }
        printf("\n");
    }
    return 0;
}