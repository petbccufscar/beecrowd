#include <stdio.h>
#include <stdlib.h>

int main(){

    int i, j;
    int N, M, cidade[100][100], dist;
    int pos_i_jogador, pos_j_jogador, pos_i_analogimon, pos_j_analogimon;

    while(scanf("%d %d",&N,&M) != EOF){
        
        for(i = 0; i < N; i++){
            for(j = 0; j < M; j++){
                scanf("%d", &cidade[i][j]);
                if(cidade[i][j] == 1){
                    pos_i_jogador = i;
                    pos_j_jogador = j;
                }
                if(cidade[i][j] == 2){
                    pos_i_analogimon = i;
                    pos_j_analogimon = j;
                }
            }
        }

        dist = abs(pos_i_jogador - pos_i_analogimon) + abs(pos_j_analogimon - pos_j_jogador);

        printf("%d\n",dist);


    }
    return 0;
}