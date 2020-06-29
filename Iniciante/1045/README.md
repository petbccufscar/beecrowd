<<<<<<< HEAD
# Problema: 1045

=======
# Problema:
>>>>>>> 753b16d... Alterado os README - 1005, 1044, 1045, 1046
Leia 3 valores de ponto flutuante A, B e C e ordene-os em ordem decrescente, de modo que o lado A representa o maior dos 3 lados. A seguir, determine o tipo de triângulo que estes três lados formam, com base nos seguintes casos, sempre escrevendo uma mensagem adequada:
    - se A ≥ B+C, apresente a mensagem: NAO FORMA TRIANGULO
    - se A2 = B2 + C2, apresente a mensagem: TRIANGULO RETANGULO
    - se A2 > B2 + C2, apresente a mensagem: TRIANGULO OBTUSANGULO
    - se A2 < B2 + C2, apresente a mensagem: TRIANGULO ACUTANGULO
    - se os três lados forem iguais, apresente a mensagem: TRIANGULO EQUILATERO
    - se apenas dois dos lados forem iguais, apresente a mensagem: TRIANGULO ISOSCELES

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/1045

# Resolução

O problema pede a utilização de 3 valores de ponto flutuante no caso então 3 valores do tipo float:
```c
        float A,B, C;
```
Iremos utilizar variáveis auxiliares que serão **a, b e c minúsculas**, pois o problema pede que o lado A sempre seja o maior e para isso temos que fazer as verificações usando if ou else if para assegurar que a condição seja respeitada:

```c
        float a, b, c;
        scanf("%f %f %f", &a, &b, &c);

        if(a<0||b<0||c<0){  
        return 0;
        }
        if(a>=b&&a>=c){   
            A=a;
            B=b;
            C=c;
        }
        else if(b>a&&b>=c){ 
            A=b;            
            B=a;
            C=c;
        }
        else if(c>a&&c>b){  
            A=c;            
            B=a;
            C=b;
        }
```
No primeiro if irá se testar se as variáveis são positivas, condição exigida pelo uri.
No segundo if se verifica o caso em que "A" é maior ou igual a "B" 'e'(&& operador logico para "e(AND)") "A" maior.
No [else if](http://linguagemc.com.br/estruturas-de-decisao-encadeadas-if-else-if-else/) será testado o caso em que B é maior ou igual a C, Então A recebe o valor da variável auxiliar "b".
No segundo else if o caso testado é em que "c" é o maior, então "A" irá receber o valor da variável auxiliar "c".

**OBS:**Temos que testar para igualdade também, pois existe as condições para triângulos equilateros e isosceles.

Depois de assegurar que a entrada está correta passamos para etapa dos teste para classificar cada tipo de triângulo pedido pelo problema 1045:
**OBS:**[Caso apresente dificuldade com a matemática do problema - trigonometria](https://escolakids.uol.com.br/matematica/classificacao-dos-triangulos.htm)

```c
        if(A >= (B+C)){
            printf("NAO FORMA TRIANGULO\n");
        }

        else if((A*A) == ((B*B) + (C*C))){
            printf("TRIANGULO RETANGULO\n");
        }

        else if((A*A) > ((B*B) + (C*C))){
            printf("TRIANGULO OBTUSANGULO\n");

                if((A==B||B==C||C==A)&&(A!=B||B!=C||C!=A)){  
                    printf("TRIANGULO ISOSCELES\n");      
                }
                
        }

        else if((A*A) < ((B*B) + (C*C))){
            printf("TRIANGULO ACUTANGULO\n");

                if((A==B||B==C||C==A)&&(A!=B||B!=C||C!=A)){
                    printf("TRIANGULO ISOSCELES\n");          
                }
                if(A==B && B==C){
                    printf("TRIANGULO EQUILATERO\n");
                }

        }
```
Quando fazemos o teste para confimar se o triângulo é obtusângulo temos que lembrar que um triângulo Obtusângulo pode ser também um triângulo Isósceles por isso temos que fazer essa verificação.
O mesmo irá valer para o Acutângulo que poder ser Isósceles ou equilátero.

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
<<<<<<< HEAD
ou nos mande um e-mail com o assunto "URI" para petbcc.ufscar@gmail.com
=======
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
>>>>>>> 753b16d... Alterado os README - 1005, 1044, 1045, 1046

##### Para aprender um pouco mais sobre Operadores Lógicos em C:
[Operadores Lógicos em C](http://linguagemc.com.br/operadores-logicos-em-c/#:~:text=Os%20operadores%20lógicos%20são%20utilizados,condições%20simples%20em%20expressões%20lógicas.)


