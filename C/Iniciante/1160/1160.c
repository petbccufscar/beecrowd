#include <stdio.h>

int main(){
	int contador, T, PA, PB, anos;
	double G1, G2; 

	scanf("%d", &T);

	for(contador=0; contador<T; contador++){
    scanf("%d %d %lf %lf", &PA, &PB, &G1, &G2);
    anos = 0;

    G1 = (G1 / 100.0) + 1.0;
    G2 = (G2 / 100.0) + 1.0;

    while(PA <= PB){
      PA *= G1;
      PB *= G2;
      anos++;
      if (anos > 100){
          printf("Mais de 1 seculo.\n");
          break;
      }
    }
    
    if (anos <= 100)
        printf("%d anos.\n", anos);
	}

	return 0;
}
