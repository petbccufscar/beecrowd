#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main()
{   
    int n, q, i, achou, tam ;
    char consulta[100];
    
    scanf("%d", &n);

    char **pesquisa; 
    pesquisa = malloc (n * sizeof (char *));
    for ( i = 0; i < n; i++)
        pesquisa[i] = malloc (100 * sizeof (char));


    for( i = 0; i < n ; i++){
        scanf("%s", pesquisa[i]);
    }

    scanf("%d", &q);

    while(q--){
        achou = 0;
        tam = 0;

        scanf("%s", consulta);
        for( i = 0; i < n ; i++){
            
            if(strncmp(consulta, pesquisa[i], strlen(consulta)) == 0 ){

                achou++;
                if(tam < strlen(pesquisa[i]))
                    tam = strlen(pesquisa[i]);
            }
        }
        
        if(achou == 0)
            printf("-1\n");
        else
            printf("%d %d\n", achou, tam);
    }

    return 0;
}