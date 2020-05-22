# Problema:

Dois carros (X e Y) partem em uma mesma direção. O carro X sai com velocidade constante de 60 Km/h e o carro Y sai com velocidade constante de 90 Km/h.

Em uma hora (60 minutos) o carro Y consegue se distanciar 30 quilômetros do carro X, ou seja, consegue se afastar um quilômetro a cada 2 minutos.

Leia a distância (em Km) e calcule quanto tempo leva (em minutos) para o carro Y tomar essa distância do outro carro.

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/1016

# Resolução:

Como o carro leva 2 minutos para se afastar 1 km do outro, por conta da velocidade de distanciação(30km/h = 30km/60min = 1km/2min), lemos a distância e a multiplicamos por 2, para calcular o tempo necessário.   

Para representar isto em nosso programa, fazemos: 

```c
        int dist;
```

##### Para aprender um pouco mais sobre variáveis: [Variáveis](http://linguagemc.com.br/variaveis-em-linguagem-c/)

Para ler a variável, usa-se scanf:

```c
        scanf("%d", &dist);
```

Em seguida, escrevemos o resultado na tela utilizando a função printf:

```c
        printf("%d minutos\n", dist*2);
```

##### Para aprender um pouco mais sobre tipos de variáveis: [Tipos de Variáveis](http://linguagemc.com.br/tipos-de-dados-em-c/)

###### Todas as funções utlizadas estão contidas na biblioteca stdio.h, incluída na primeira linha do nosso programa.


