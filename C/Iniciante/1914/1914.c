#include <stdio.h>

int main() {
    int QT;
    long long num, num2;
    char jogador[100], jogador2[100], escolha[6], resultado;

    scanf("%d", &QT);

    while (QT--) {
        scanf("%s", jogador);
        scanf("%s", escolha);
        scanf("%s", jogador2); 
        scanf("%s", escolha);
        scanf("%lld %lld", &num, &num2);

        if (num % 2 == num2 % 2) resultado = 'P';
        else resultado = 'I';

        if (escolha[0] == resultado) printf("%s\n", jogador2);
        else printf("%s\n", jogador);
    }

    return 0;
}