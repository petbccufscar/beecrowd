#include <stdio.h>
#include <stdlib.h>

typedef struct pacote{
    int valor;
    int tempo;

} pacote;

int main(){
    
    int N, i;

    while ((scanf("%d", &N)) != EOF){

        pacote *vetor;
        vetor = malloc (N * sizeof (pacote));

        for( i = 0; i < N; i++)
            scanf("%d", &vetor[i].valor);
        
        for( i = 0; i < N; i++)
            scanf("%d", &vetor[i].tempo);
        

        
        pacote aux;
        int alterado = 1;
        int soma = 0;
        while(alterado == 1){
            alterado = 0;
            for( i = 0; i < N - 1; i++){
                if( vetor[i].valor > vetor[i+1].valor){
                    soma += vetor[i].tempo + vetor[i+1].tempo;
                    aux = vetor[i];
                    vetor[i] = vetor[i+1];
                    vetor[i+1] = aux;
                    alterado = 1;
                }
            }
        }

        printf("%d\n", soma);
        
    }
    return 0;

}
