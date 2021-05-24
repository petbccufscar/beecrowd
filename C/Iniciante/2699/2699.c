#include <stdio.h>
#include <string.h>

char s[1001], d[1001];
int verificador[1001][1001];

int divisao(int posicao, int resto, int divisor) {
    int i;
    
    if (posicao == strlen(s)) {
        if (resto == 0)
            return 1;
        else
            return 0;
    }
        
    if (verificador[posicao][resto] != -1)
        return verificador[posicao][resto];
        
    if (s[posicao] != '?')
        return divisao(posicao+1, (resto*10 + s[posicao] - '0') % divisor, divisor);

    if (posicao == 0)
        i = 1;
    else
        i = 0;
            
    while (i < 10) {
        if (divisao(posicao+1, (resto*10+i) % divisor, divisor) == 1) {
            d[posicao] = '0' + i;
            return 1;
        }
        i++;
    }
    
    verificador[posicao][resto] = 0;
    return 0;
}

int main() {
    int n, i, j;
    
    while (scanf(" %s %d ", s, &n) != EOF) {
        strcpy(d, s);
        
        for (i = 0; i < 1001; i++)
            for (j = 0; j < 1001; j++)
                verificador[i][j] = -1;
        
        if (divisao(0, 0, n) == 1) 
            printf("%s\n", d);
        else
            printf("*\n");
    }
    return 0;
}
