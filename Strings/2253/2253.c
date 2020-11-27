#include <stdio.h>
#include <string.h>

int main()
{
    char senha[255];
    int i, tam;
    int maiuscula, minuscula, numero, ehInvalida;

    while (gets(senha) != NULL)
    {
        ehInvalida = 0;
        numero = 0;
        maiuscula = 0;
        minuscula = 0;
        tam = strlen(senha);

        for (i = 0; i < tam; i++)
        {
            if (senha[i] == 32)
            {
                ehInvalida = 1;
                break;
            }
            else if (strlen(senha) < 6 || strlen(senha) > 32)
            {
                ehInvalida = 1;
                break;
            }
            else if ((senha[i] < 48) || (senha[i] > 57 && senha[i] < 65) || senha[i] > 122 (senha[i] >= 91 && senha[i] < 97))
            {
                ehInvalida = 1;
                break;
            }
            else if (senha[i] >= 91 && senha[i] < 97)
            {
                ehInvalida = 1;
                break;
            }

            if (senha[i] > 47 && senha[i] < 58)
                numero = 1;
            else if (senha[i] > 64 && senha[i] < 91)
                maiuscula = 1;
            else if (senha[i] > 96 && senha[i] < 123)
                minuscula = 1;
        }

        if (ehInvalida == 1)
            printf("Senha invalida.\n");
        else if (numero == 0 || (maiuscula == 0 || minuscula == 0))
            printf("Senha invalida.\n");
        else
            printf("Senha valida.\n");
    }

    return 0;
}
