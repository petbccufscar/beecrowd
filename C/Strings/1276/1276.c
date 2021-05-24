#include <stdio.h>
#include <stdlib.h>

void encontra_faixa(char letras[50], int tam_vetor);

void ordena_letras(char letras[50], int n);

int main()
{
    int i, j;
    char letras_espaco[50], letras[50];

    while ( gets(letras_espaco) ){
        for (i = 0, j = 0; i < 50 && letras_espaco[i] != '\0'; i++){
            
            if (letras_espaco[i] >= 'a' && letras_espaco[i] <= 'z')
                letras[j++] = letras_espaco[i];
                
        }
        letras[j] = '\0';

        ordena_letras(letras, j);
        encontra_faixa(letras, j);
    }
}

void encontra_faixa(char letras[50], int tam_vetor)
{
    int inicio, meio, fim;

    inicio = 0;
    for (inicio = 0; inicio < tam_vetor;){
        meio = inicio;
        fim = inicio + 1;
        while (fim < tam_vetor && letras[fim] <= letras[meio]+1){
            meio++;
            fim++;
        }

        printf("%c:%c", letras[inicio], letras[fim-1]);
        inicio = fim;

        if (fim < tam_vetor)
            printf(", ");
    }
    printf("\n");
}

void ordena_letras(char letras[50], int n)
{
    int i, j;
    char aux;

    for (j = 1; j < n; j++){
        aux = letras[j];
        for (i = j - 1; i >= 0 && aux < letras[i]; i--)
            letras[i + 1] = letras[i];
        letras[i + 1] = aux;
    }
}