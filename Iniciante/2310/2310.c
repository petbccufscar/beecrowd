#include <stdio.h>

int main()
{
    int N, S, B, A, S1, B1, A1, contagem;
    double soma_S = 0.00, soma_B = 0.00, soma_A = 0.00;
    double soma_S1 = 0.00, soma_B1 = 0.00, soma_A1 = 0.00;
    double resultado_S, resultado_B, resultado_A;
    char nome[200];
    scanf("%d", &N);
    for (contagem = 1; contagem <= N; contagem++)
    {
        scanf("%S", nome);
        scanf("%d%d%d", &S, &B, &A);
        scanf("%d%d%d", &S1, &B1, &A1);
        soma_S += S;
        soma_B += B;
        soma_A += A;
        soma_S1 += S1;
        soma_B1 += B1;
        soma_A1 += A1;
    }
    resultado_S = (soma_S1 / soma_S) * 100.00;
    resultado_B = (soma_B1 / soma_B) * 100.00;
    resultado_A = (soma_A1 / soma_A) * 100.00;
    printf("Pontos de Saque: %.2lf %%.\n", resultado_S);
    printf("Pontos de Bloqueio: %.2lf %%.\n", resultado_B);
    printf("Pontos de Ataque: %.2lf %%.\n", resultado_A);
    return 0;
}