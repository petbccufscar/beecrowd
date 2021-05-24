#include <stdio.h>
int main()
{
    int cont, n, valor, dentro = 0, fora = 0;
    scanf("%d", &n);
    for (cont = 1; cont <= n; cont++)
    {
        scanf("%d", &valor);
        if (valor >= 10 && valor <= 20)
            dentro++;
        else
            fora++;
    }
    printf("%d in\n", dentro);
    printf("%d out\n", fora);
    return 0;
}
