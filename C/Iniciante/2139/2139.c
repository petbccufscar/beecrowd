 #include <stdio.h>

int main()
{
    int mes, dia, total, i;
    int dias_mes[12] = {31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 25};

    while(scanf("%d%d", &mes, &dia) != EOF)
    {
        if(mes == 12 && dia == 25) 
            printf("E natal!\n");

        else if(mes == 12 && dia == 24) 
            printf("E vespera de natal!\n");

        else if(mes == 12 && dia > 25) 
            printf("Ja passou!\n");

        else
        {
            total = dias_mes[mes-1] - dia;
            
            for(i = mes; i < 12; i++)
                total = total + dias_mes[i];

            printf("Faltam %d dias para o natal!\n", total);
        }
    }
    return 0;
}