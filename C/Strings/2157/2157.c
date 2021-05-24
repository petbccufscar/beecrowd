#include <stdio.h>

int numSeparado[5];
int tamVet = 0;

void inverteNum (int num) {
    int i;
    
    i = 0;

    while(num != 0) {  
        numSeparado[i] = num % 10;
        num /= 10;
        tamVet++;
        i++;
    }

}

void exibirVetor() {
  int i;

  for (i = 0; i < tamVet; i++) {
    printf("%i", numSeparado[i]);
  }
  tamVet = 0;
}

void seqInverte (int ini, int fim) {
    int numSeq = (fim - ini + 1) * 2;
    int i = 0;
    while (i < numSeq) {
        if (ini <= fim) {
            printf("%i", ini);
            ini++;
        } else {
            inverteNum(fim);
            exibirVetor();
            fim--;
        }
        i++;
    }
}

int main()
{
    int quantSeq, inicio, fim;
    int i;

    scanf("%i", &quantSeq);
   
    for (i = 0; i < quantSeq; i++) {
        scanf("%i %i", &inicio, &fim);

        seqInverte(inicio, fim);
        printf( "\n");
    }

    return 0;
}