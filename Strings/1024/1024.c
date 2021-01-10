#include <stdio.h>

int main() {
    
    int n, i = 0, j;
    char *palavra = (char *) malloc(sizeof(char) * 1000);
    int tamanho[n];

    scanf("%d ", &n);
    
    while (i < n) {
        gets(palavra); 
        tamanho[i] = 0;
        while(palavra[tamanho[i]] != '\0')
        tamanho[i]++;

        j = 0;            
        while (j < tamanho[i]) {
            if ((palavra[j] >= 97 && palavra[j] <= 122) || ((palavra[j] >= 65 && palavra[j] <= 90)))
                palavra[j] = (char) (palavra[j] + 3);
            
            j++;
        }
        
        j = 0;
        while (j < tamanho[i] >> 1) {
            
            char letra = palavra[j];
            palavra[j] = palavra[tamanho[i]-j-1];
            palavra[tamanho[i]-j-1] = letra;
            
            j++;
        }
        
        j = tamanho[i] >> 1;
        while (j < tamanho[i]) {
            
            palavra[j] = (char) (palavra[j] - 1);
            
            j++;
            
        } 
        printf("%s\n", palavra);   
        i++;
    }
    return 0;
}
