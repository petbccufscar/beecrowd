# Problema:
Leia 3 valores de ponto flutuante A, B e C e ordene-os em ordem decrescente, de modo que o lado A representa o maior dos 3 lados. A seguir, determine o tipo de triângulo que estes três lados formam, com base nos seguintes casos, sempre escrevendo uma mensagem adequada:
    - se A ≥ B+C, apresente a mensagem: NAO FORMA TRIANGULO
    - se A2 = B2 + C2, apresente a mensagem: TRIANGULO RETANGULO
    - se A2 > B2 + C2, apresente a mensagem: TRIANGULO OBTUSANGULO
    - se A2 < B2 + C2, apresente a mensagem: TRIANGULO ACUTANGULO
    - se os três lados forem iguais, apresente a mensagem: TRIANGULO EQUILATERO
    - se apenas dois dos lados forem iguais, apresente a mensagem: TRIANGULO ISOSCELES

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/1045

# Resolução
Sempre lembrar de incluir as bibliotecas padrões:
```c
        #include <stdio.h>
        #include <stdlib.h>
```
O problema pede a utilização de 3 valores de ponto flutuante no caso então 3 valores do tipo float:
```c
        float A,B, C;
```
Iremos utilizar variáveis auxiliares, pois o problema pede que o lado A sempre seja o maior e para isso temos que fazer as verificações usando if ou else if para assegurar que a condição seja respeitada:
```c
        float a, b, c;
        scanf("%f %f %f", &a, &b, &c); //Iremos ler usando as variaveis auxiliares para utilizar elas nas verificacoes 

        if(a<0||b<0||c<0){  //Problema pede que os numeros sejam positivos.
        return 0;
        }
        if(a>=b&&a>=c){     //Caso em que A eh maior ou igual a B 'e'(&& operador logico para "e(AND)") A maior ou igual a C
            A=a;
            B=b;
            C=c;
        }
        else if(b>a&&b>=c){ //Caso em que B eh o maior ou igual a C
            A=b;            //Então A recebe o valor da variavel auxiliar "b"
            B=a;
            C=c;
        }
        else if(c>a&&c>b){  //Caso em que C eh o maior
            A=c;            //Entao A recebe o valor da variavel auxiliar "c"
            B=a;
            C=b;
        }

```
**OBS:**Temos que testar para igualdade também, pois existe as condições para triângulos equilateros e isosceles.

Depois de assegurar que a entrada está correta passamos para etapa dos teste para classificar cada tipo de triângulo pedido pelo problema 1045:
**OBS:**[Caso apresente dificuldade com a matemática do problema](https://escolakids.uol.com.br/matematica/classificacao-dos-triangulos.htm)
```c
        if(A >= (B+C)){
            printf("NAO FORMA TRIANGULO\n");
        }

        else if((A*A) == ((B*B) + (C*C))){
            printf("TRIANGULO RETANGULO\n");
        }

        else if((A*A) > ((B*B) + (C*C))){
            printf("TRIANGULO OBTUSANGULO\n");

                if((A==B||B==C||C==A)&&(A!=B||B!=C||C!=A)){  //Um triangulo Obtusangulo pode ser tambem um triangulo Isosceles por isso temos que fazer essa veri-
                    printf("TRIANGULO ISOSCELES\n");         //cacao
                }
                
        }

        else if((A*A) < ((B*B) + (C*C))){
            printf("TRIANGULO ACUTANGULO\n");

                if((A==B||B==C||C==A)&&(A!=B||B!=C||C!=A)){  //Mesmo vale para o Ocutangulo que pode ser isosceles ou equilatero  
                    printf("TRIANGULO ISOSCELES\n");          
                }
                if(A==B && B==C){
                    printf("TRIANGULO EQUILATERO\n");
                }

        }
```
Lembre-se de encerrar o seu código, boas práticas são sempre bem vindas:
```c
        return 0;
```

##### Para aprender mais sobre operadores em c: 
[Operados em C](https://www.tutorialspoint.com/cprogramming/c_operators.htm)


