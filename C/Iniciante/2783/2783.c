#include <stdio.h>
#include <stdlib.h>


int main(void) {
    int *carimbadas, compradas, carimbadas_restantes;
    int n_figurinhas, c_carimbadas, m_compradas, i, j;
    
    scanf("%d", &n_figurinhas);
    scanf("%d", &c_carimbadas );
    scanf("%d", &m_compradas);
    carimbadas_restantes = c_carimbadas;

    carimbadas = (int *) malloc(c_carimbadas   * sizeof(int));
    for (i = 0; i < c_carimbadas  ; i++) {
        scanf("%d", &carimbadas[i]);
    }

    for (i = 0; i < m_compradas; i++) {
        scanf("%d", &compradas);
        for (j = 0; j < c_carimbadas; j++) {
            if (compradas == carimbadas[j]) {
                carimbadas_restantes = (carimbadas_restantes - 1);
                carimbadas[j] = carimbadas[j] + n_figurinhas;  
            }
        }
    }

    printf("%d\n", carimbadas_restantes);
    return 0;
}