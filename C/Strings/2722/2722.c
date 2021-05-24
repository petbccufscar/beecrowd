#include <stdio.h>
#include <string.h>

int main(){ 
    char primeiraLinha[100], segundaLinha[100], nomeCerto[200];
    int n, j, i, k, tamPrimeiraLinha, tamSegundaLinha;

    scanf("%d ", &n);

    while(n--){
        i = 0;
        j = 0;
        k = 0;

        fgets(primeiraLinha, sizeof(primeiraLinha), stdin);
        fgets(segundaLinha, sizeof(segundaLinha), stdin);
        
        tamPrimeiraLinha = strlen(primeiraLinha);
        tamSegundaLinha = strlen(segundaLinha);

        while(j+3 < tamPrimeiraLinha + tamSegundaLinha){       
            nomeCerto[j++] = primeiraLinha[i++];
            nomeCerto[j++] = primeiraLinha[i++];
            nomeCerto[j++] = segundaLinha[k++];
            if(segundaLinha[k+1] != '\0')
                nomeCerto[j++] = segundaLinha[k++];
        }

        nomeCerto[j] = '\0';
        printf("%s\n", nomeCerto);
    }

    return 0;
}