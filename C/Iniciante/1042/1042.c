#include <stdio.h>

void bubbleSort(int *vetor) {
    int i, j, aux;

    for (i = 0; i < 2; i++) {
        for(j = 0; j < 2; j++) {
            
            if(vetor[j] > vetor[j + 1]) {
                aux = vetor[j];
                vetor[j] = vetor[j + 1];
                vetor[j + 1] = aux;
            }
        }
    }
}

int main() {
    int vetorOriginal[3], vetorOrdenado[3];
    int i;
    
   for(i = 0; i < 3; i++) {
       scanf("%d", &vetorOriginal[i]);

       // copiando o valor lido para o vetorOrdenado
       vetorOrdenado[i] = vetorOriginal[i];
   }

    bubbleSort(vetorOrdenado);

    for(i = 0; i < 3; i++)
        printf("%d\n", vetorOrdenado[i]);

    printf("\n");

    for(i = 0; i < 3; i++)
        printf("%d\n", vetorOriginal[i]);

    return 0;
}