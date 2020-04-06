# Problema:

A fórmula para calcular a área de uma circunferência é: area = π . raio2. Considerando para este problema que π = 3.14159.
Efetue o cálculo da área, elevando o valor de raio ao quadrado e multiplicando por π.

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/1002

# Resolução:

Para ler o valor de dupla precisão antes precisamos declará-los como variáveis, para isso fazemos:
```c
        int var_name;
```
No nosso caso, "var_name" é substituido por raio.
Já iremos declarar todas as outras variáveis necessárias, pi e raio.

##### Para aprender um pouco mais sobre variáveis: [Variáveis](http://linguagemc.com.br/variaveis-em-linguagem-c/)

Para leitura, usamos a função scanf:
```c
        scanf("%lf",&var_name);
```
Utilizamos %lf porque estamos recebendo um valor double do usuário. 

##### Aprenda sobre as variações possíveis em: [Entrada e Saida](http://linguagemc.com.br/operacoes-de-entrada-e-saida-de-dados-em-linguagem-c/)

Agora fazemos uma atribuição a variável "area".
```c
        area = raio*raio * pi;
```
E por fim, escrevemos o resultado na tela utilizando a função printf:
```c
        printf("A= %.4lf\n",area);
```

Utilizamos .4 para a saída ficar com 4 casas de precisão.

%lf será substituido pelo valor contido em area.


###### Todas as funções utlizadas estão contidas na biblioteca stdio.h, incluída na primeira linha do nosso programa.
