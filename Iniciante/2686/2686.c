#include <stdio.h>
 
int main() {
 
    float m, tempo;
    int hora, minuto;
    
    while (scanf("%f", &m) != EOF) {
        if (m < 90) {
            printf("Bom Dia!!\n");
            
            hora = 6;
            tempo = m/0.5;
            minuto = tempo*2;
            
            if (minuto >= 60) {
                hora = hora + (minuto/60);
                minuto = minuto%60;
            }
            printf("%02d:%02d:00\n", hora, minuto);
        }
        else if (m < 180) {
            printf("Boa Tarde!!\n");
            
            hora = 12;
            m = m-90;
            tempo = m/0.5;
            minuto = tempo*2;
            
            if (minuto >= 60) {
                hora = hora + (minuto/60);
                minuto = minuto%60;
            }
            printf("%02d:%02d:00\n", hora, minuto);            
        }
        else if (m < 270) {
            printf("Boa Noite!!\n");
            
            hora = 18;
            m = m-180;
            tempo = m/0.5;
            minuto = tempo*2;
            
            if (minuto >= 60) {
                hora = hora + (minuto/60);
                minuto = minuto%60;
            }
            printf("%02d:%02d:00\n", hora, minuto);
        }
        else if (m < 360) {
            printf("De Madrugada!!\n");
            
            hora = 0;
            m = m-270;
            tempo = m/0.5;
            minuto = tempo*2;
            
            if (minuto >= 60) {
                hora = hora + (minuto/60);
                minuto = minuto%60;
            }
            printf("%02d:%02d:00\n", hora, minuto);
        }
        else
            printf("Bom Dia!!\n06:00:00\n");
    }
 
    return 0;
}
