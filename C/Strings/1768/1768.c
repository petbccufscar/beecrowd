#include <stdio.h>

void repetirCar(int n, char c) {
  int i;
  for(i = 0; i < n; i++) {
    printf("%c", c);
  }
}

void baseArvore(int n) {
  repetirCar(n, ' ');
  printf("*\n");
  repetirCar(n - 1, ' ');
  printf("***\n\n");
}

void desenArvore(int n) {
    int i, quantEsp;

    quantEsp = n;

    for(i = 1; i <= n; i += 2) {
      repetirCar(quantEsp/2, ' ');
      repetirCar(i, '*');
      printf("\n");

      quantEsp -= 2;
    }

    baseArvore(n/2);
}


int main(){
    int entrada;

    while(scanf("%d", &entrada) != EOF) {
      desenArvore(entrada);
    }

    return 0;
}
