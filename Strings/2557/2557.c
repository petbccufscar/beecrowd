#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    char equacao[50]={'0'}, valores[2][10] = {{'0'}};
    int soma=0, i=0, j=0, k=0, lado_esquerdo1=1, lado_esquerdo2=1, valor1, valor2, tamanho;
    while (scanf(" %s", equacao) != EOF) {
        tamanho =(strlen(equacao));
        while (i<tamanho) {
            j=0;
            while (equacao[i] != 'R' && equacao[i] != 'L' && equacao[i] != 'J' && equacao[i] != '+' && equacao[i] != '=' && equacao[i] != '-' && i<tamanho) {
                valores[k][j] = equacao[i];
                if(equacao[i+1] == '+' || equacao[i+1] == '=' ||equacao[i+1] == '-' ) {
                    k++;
                }
                i++;
                j++;
            }
            if(i==0) {
                lado_esquerdo1 = 0;
            }
            else if(equacao[i] == '+') {
                soma++;
            }
            if((equacao[i+1] == 'R' || equacao[i+1] == 'L' ||equacao[i+1] == 'J') && lado_esquerdo1 == 1 && i<tamanho-2) {
                lado_esquerdo2 = 0;
            }
            i++;
        }
        valor1 = atoi(valores[0]);
        valor2 = atoi(valores[1]);
        if(soma == 1 && lado_esquerdo1==1 && lado_esquerdo2 == 1) {
            printf("%d\n", valor1 + valor2);
        }
        else if(soma == 1 && (lado_esquerdo1==0 || lado_esquerdo2 ==0)) {
            printf("%d\n", valor2 - valor1);
        }
        else if(soma == 0 && lado_esquerdo1 == 1 && lado_esquerdo2 == 1) {
            printf("%d\n", valor1 - valor2);
        }
        else if(soma==0 && (lado_esquerdo1==0 || lado_esquerdo2 ==0)){
            printf("%d\n", valor1 - valor2);
        }
        soma = 0;
        i = 0;
        k = 0;
        j = 0;
        lado_esquerdo1 = 1;
        lado_esquerdo2 = 1;
        memset(valores[0], 0, 10);
        memset(valores[1], 0, 10);
    }
    return 0;
}