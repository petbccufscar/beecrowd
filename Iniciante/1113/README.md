# Problema: 1113

Leia uma quantidade indeterminada de duplas de valores inteiros X e Y. Escreva para cada X e Y uma mensagem que indique se estes valores foram digitados em ordem crescente ou decrescente.

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/1113

# Resolução

O problema pede a utilização de 2 valores inteiros X e Y:
```c
        float X, Y;
```
O exercício pede vários casos de teste sendo cada um deles divididos em valores para X e Y, para fazer esse tipo de exercício é recomendado usar um `while` em conjunto à um `scanf`:

```c
        while(X!=Y){
            scanf("%d %d", &X, &Y);
        }
```
Porém adotando essa estratégia é nescessário iniciar um `scanf` antes se não o `while` não irá iniciar, sendo assim a primeira parte do exercício é reservada para fazer apenas uma verificação de cada nos `if` e `else if`, resaltando o último `else if` que é a condição de parada, ela é testada para contemplar o caso onde se inicia com o caso de parada (X igual Y):

```c
        int X, Y;
        
        scanf("%d %d", &X, &Y);
        if(X>Y){
            printf("Decrescente\n");
        }
        else if(X<Y){
            printf("Crescente\n");
        }
        else if(X==Y){
            return 0;
        }
```
Como o exercício pede para ser vários casos de teste, então iremos expandir o que foi mostrado ateriormente e junta-los:

```c

        while(X!=Y){
            scanf("%d %d", &X, &Y);
            if(X>Y){
                printf("Decrescente\n");
            }
            else if(X<Y){
                printf("Crescente\n");
            }
        }
```

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para petbcc.ufscar@gmail.com

##### Para aprender um pouco mais sobre Operadores Lógicos em C:
[Operadores Lógicos em C](http://linguagemc.com.br/operadores-logicos-em-c/#:~:text=Os%20operadores%20lógicos%20são%20utilizados,condições%20simples%20em%20expressões%20lógicas.)


