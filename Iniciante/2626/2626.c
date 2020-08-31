#include <stdio.h>
#include <string.h>

int ganhar(char ganha[10], char n_ganha[10])
{
    if (strcmp(ganha, "pedra") == 0 && strcmp(n_ganha, "tesoura") == 0)
        return 1;
    if (strcmp(ganha, "papel") == 0 && strcmp(n_ganha, "pedra") == 0)
        return 1;
    if (strcmp(ganha, "tesoura") == 0 && strcmp(n_ganha, "papel") == 0)
        return 1;
    return 0;
}

int main()
{

    char dodo[10], leo[10], pepper[10];

    while (scanf("%s %s %s", dodo, leo, pepper) != EOF)
    {

        if (ganhar(dodo, leo) && ganhar(dodo, pepper))
            printf("Os atributos dos monstros vao ser inteligencia, sabedoria...\n");
        else if (ganhar(leo, dodo) && ganhar(leo, pepper))
            printf("Iron Maiden's gonna get you, no matter how far!\n");
        else if (ganhar(pepper, dodo) && ganhar(pepper, leo))
            printf("Urano perdeu algo muito precioso...\n");
        else
            printf("Putz vei, o Leo ta demorando muito pra jogar...\n");
    }

    return 0;
}
