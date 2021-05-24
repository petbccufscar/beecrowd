#include <stdio.h>
#include <string.h>

int main() {
	char palavra[51][51], frase[51];
	int n, t, u, tam_frase, tam_palavra, posicao, perigo, i, j, k, l;

	scanf("%d", &n);
    while (n > 0) {
        scanf("%d", &t);

        for(i=0;i<t;i++)
            scanf(" %50[^\n]",&palavra[i]);

        scanf("%d", &u);

        for(i=0;i<u;i++) {
            scanf(" %50[^\n]",&frase);
            tam_frase = strlen(frase);
            perigo = 0;
            
            for(j = 0; j < t; j++) {
                for (k = 0; k < tam_frase; k++) {
                    if (palavra[j][0]==frase[k]) {
                        posicao = k;
                        tam_palavra = 0;

                        for(l = 0; l < strlen(palavra[j]); l++) {
                            if(palavra[j][l] == frase[posicao])
                                tam_palavra++;

                            posicao++;

                            if (tam_palavra == strlen(palavra[j])) {
                                if ((posicao >= strlen(frase)) || (frase[posicao] >= 65 && frase[posicao] <= 90)) {
                                    perigo = 1;
                                    l = strlen(palavra[j]);
                                    k = tam_frase;
                                    j = t;
                                }
                                else
                                    tam_palavra = 0;
                            }
                        }
                    }
                }
            }
            
           	if (perigo == 1)
        	    printf("Abortar\n");
        	else
        	    printf("Prossiga\n");

            memset(frase, ' ', strlen(frase));
    	}
        
        n--;
        if (n > 0)
            printf("\n");
	}

	return 0;
}

