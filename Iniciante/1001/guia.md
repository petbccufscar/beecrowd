# Problema:

Leia 2 valores inteiros e armazene-os nas variáveis A e B. Efetue a soma de A e B atribuindo o seu resultado na variável X. Imprima X conforme exemplo apresentado abaixo. Não apresente mensagem alguma além daquilo que está sendo especificado e não esqueça de imprimir o fim de linha após o resultado, caso contrário, você receberá "Presentation Error".

# Resolução:

Para ler os 2 valores inteiros antes precisamos declará-los como variáveis, para isso fazemos:
```c
        int var_name;
```
No nosso caso, "var_name" é substituido por A, B e X.

##### Para aprender um pouco mais sobre variáveis: [Variáveis](http://linguagemc.com.br/variaveis-em-linguagem-c/)

Para leitura, usamos a função scanf:
```c
        scanf("%d",&var_name);
```
Utilizamos %d porque estamos recebendo um valor inteiro do usuário. 

##### Aprenda sobre as variações possíveis em: [Entrada e Saida](http://linguagemc.com.br/operacoes-de-entrada-e-saida-de-dados-em-linguagem-c/)

Agora fazemos uma atribuição a variável "X" somandos A e B
```c
        X = A + B
```
E por fim, escrevemos o resultado na tela utilizando a função printf:
```c
        printf("X = %d",X);
```
%d será substituido pelo valor contido em X.


##### Todas as funções utlizadas estão contidas na biblioteca stdio.h, incluída na primeira linha do nosso programa.
