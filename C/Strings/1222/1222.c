#include <stdio.h>
#include <string.h>

int main () {
    int n, l, c;
    int i;
    int linhas, paginas, letras, tamanho;
    char palavra[71];

    while (scanf("%d %d %d", &n, &l, &c) != EOF) {

        paginas = linhas = 1;
        scanf("%s", palavra);
        letras = strlen(palavra);
        for (i = 0; i < n-1; ++i)   {
            scanf("%s", palavra);

            tamanho = strlen(palavra);

            if ((letras + tamanho + 1) <= c){
                letras += tamanho + 1;
            }else{
                ++linhas;
                if (linhas > l){
                    ++paginas;
                    linhas = 1;
                }
                letras = tamanho;
            }

        }

        printf("%d\n", paginas);
    }

    return 0;
}