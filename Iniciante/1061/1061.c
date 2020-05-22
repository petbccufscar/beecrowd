#include <stdio.h>

int main(){
    int diaInicial, horasInicial, minutosInicial, segundosInicial;
    int diaFinal, horasFinal, minutosFinal, segundosFinal;
    int diaResposta, horasResposta, minutosResposta, segundosResposta;

    scanf("Dia %d %d : %d : %d ", &diaInicial, &horasInicial, &minutosInicial, &segundosInicial);
    scanf("Dia %d %d : %d : %d", &diaFinal, &horasFinal, &minutosFinal, &segundosFinal);
    
    segundosResposta = segundosFinal - segundosInicial;
    minutosResposta = minutosFinal - minutosInicial;
    horasResposta = horasFinal - horasInicial;
    diaResposta = diaFinal - diaInicial;

    if(segundosResposta < 0){
        segundosResposta += 60;
        minutosResposta--;
    }

    if(minutosResposta < 0){
        minutosResposta += 60;
        horasResposta--;
    }

    if(horasResposta < 0){
        horasResposta += 24;
        diaResposta--;
    }

    printf("%d dia(s)\n", diaResposta);
    printf("%d hora(s)\n", horasResposta);
    printf("%d minuto(s)\n", minutosResposta);
    printf("%d segundo(s)\n", segundosResposta);

    
    return 0;
}