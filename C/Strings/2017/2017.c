#include <stdio.h>

int distancia_edicao(char *, char *);
int calcula_menor(int *);

int main(){
	int k, i, distancia[5], menor;
	char x[100001], y[5][100001];	

    scanf("%s", x);
    scanf("%d", &k);

    for(i=0;i<5;i++){
        scanf("%s", y[i]);
    }

    for(i=0;i<5;i++){
        distancia[i] = distancia_edicao(x, y[i]);
    }

    menor = calcula_menor(distancia);

    if(distancia[menor]>k){
        printf("-1\n");
    } else{
        printf("%d\n", menor+1);
        printf("%d\n", distancia[menor]);
    }

	return 0;
}

int distancia_edicao(char *x, char *y){
    int i = 0, contador = 0;
    while(x[i]!='\0')
    {
        if (x[i] != y[i])
            contador++;
        i++;
    }
    return contador;
}

int calcula_menor(int *distancia){
    int menor=distancia[0], index=0, i;

    for(i=1;i<5;i++){
        if(distancia[i] < menor){
            menor = distancia[i];
            index = i;
        }
    }

    return index;
}