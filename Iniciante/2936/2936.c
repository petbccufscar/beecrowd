#include <stdio.h>
 
int main() {

    int Curupira_come,Boitata_come,Boto_come,Mapinguari_come,Iara_come,DonaChica_come;
    int Curupira_porcao,Boitata_porcao,Boto_porcao,Mapinguari_porcao,Iara_porcao;
    int Soma_total;

    scanf("%d %d %d %d %d",&Curupira_porcao,&Boitata_porcao,&Boto_porcao,&Mapinguari_porcao,&Iara_porcao);

    Curupira_come = 300 * Curupira_porcao;
    Boitata_come = 1500 * Boitata_porcao;
    Boto_come = 600 * Boto_porcao;
    Mapinguari_come = 1000 * Mapinguari_porcao;
    Iara_come = 150 * Iara_porcao;
    DonaChica_come = 225;

    Soma_total = Curupira_come+Boitata_come+Boto_come+Mapinguari_come+Iara_come+DonaChica_come;

    printf("%d\n",Soma_total);

    return 0;
}