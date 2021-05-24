#include <stdio.h>
 
int main() {
 
    int dia_que_foi_entregue, data_final_pra_entregar;

    scanf("%d %d",&dia_que_foi_entregue,&data_final_pra_entregar);

    if (dia_que_foi_entregue > data_final_pra_entregar)
    {
    printf("Eu odeio a professora!\n");
    }
    else if (dia_que_foi_entregue+2 <= data_final_pra_entregar)
    {
    printf("Muito bem! Apresenta antes do Natal!\n");
    }
    else if ( data_final_pra_entregar-dia_que_foi_entregue < 2 )
    {
    printf("Parece o trabalho do meu filho!\n");
        
        if ( data_final_pra_entregar+2 <= 24)
        {
        printf("TCC Apresentado!\n");
        }
        else
        {
        printf("Fail! Entao eh nataaaaal!\n");
        }
       
    }

    return 0;
}