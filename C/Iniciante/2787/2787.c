#include <stdio.h>

int matriz[1000][1000];
 
int main() {
 
    int L,C,i,j;
    
    scanf("%d %d",&L,&C);

    for ( i=0; i<L; i++ ) {
        for ( j=0; j<C; j++ )
        {
            if (i % 2 == 1){
                if (j % 2 == 1)
                {
                    matriz[i][j] = 1 ;
                }
                else
                {
                    matriz[i][j] = 0 ;
                }
            }
            else if (i % 2 == 0)
            {
                if (j % 2 == 1)
                {
                    matriz[i][j] = 0 ;
                }
                else
                {
                    matriz[i][j] = 1 ;
                }
            }
        }
    }

    printf ("%d\n",matriz[L-1][C-1]);

    return 0;
}