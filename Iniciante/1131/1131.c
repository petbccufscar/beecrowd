#include <stdio.h>
 
int main() {
 
    int gol_gre, gol_int, v_gre, v_int, e, jogos, x;
    
    v_gre = 0;
    v_int = 0;
    e = 0;
    jogos = 0;
    
    do {
        scanf("%d%d", &gol_int, &gol_gre);
        if (gol_int > gol_gre)
            v_int++;
        else if (gol_int < gol_gre)
            v_gre++;
        else
            e++;
        jogos++;
        printf("Novo grenal (1-sim 2-nao)\n");
        scanf("%d", &x);
    } while (x == 1);
    
    printf("%d grenais\n", jogos);
    printf("Inter:%d\n", v_int);
    printf("Gremio:%d\n", v_gre);
    printf("Empates:%d\n", e);
    
    if (v_int > v_gre)
        printf("Inter venceu mais\n");
    else if (v_int < v_gre)
        printf("Gremio venceu mais\n");
    else 
        printf("Nao houve vencedor\n");
 
    return 0;
}
