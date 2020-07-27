# Problema:

NLeia os quatro valores correspondentes aos eixos x e y de dois pontos quaisquer no plano, p1(x1,y1) e p2(x2,y2) e calcule a distância entre eles, mostrando 4 casas decimais após a vírgula, segundo a fórmula:

Distancia = raiz((x2 − x1)^2+ (y2 − y1)^2)

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/1015

# Resolução:

Uma forma de resolver o problema é realizar a leitura dos dados e apĺicá-los diretamente na fórmula dada. Além disso, iremos importar a biblioteca math.h, para utilizarmos a função de raiz quadrada.

##### Para aprender um pouco mais sobre a biblioteca math.h: [Bibliotecas](http://linguagemc.com.br/a-biblioteca-math-h/)

Primeiramente, para representar os valores em nosso programa, fazemos: 

```c
        float x1, y1, x2, y2, p1, p2, dist;
```

##### Para aprender um pouco mais sobre variáveis: [Variáveis](http://linguagemc.com.br/variaveis-em-linguagem-c/)

Para ler as variáveis, usa-se scanf:

```c
        scanf("%f %f", &x1, &y1);

        scanf("%f %f", &x2, &y2);
```

É possível inserir mais de um dado dentro de um mesmo scanf separando os %(variavel), lembrando que a ordem da variaveis inseridas no "" deve corresponder com a ordem dos endereços de memoria indicados na função. Durante a execução do programa, usamos . para separar o valor decimal do inteiro.

Após a leitura das variáveis, calcula-se a distância em cada eixo:

```c
        p1 = x2-x1;

        p2 = y2-y1;
```

Em seguida, calculamos a distância de acordo com a fórmula e escrevemos o resultado na tela utilizando a função printf:

```c
        dist = sqrt((p1*p1) + (p2*p2));
   
        printf("%.4f\n", dist);
```

O '%0.4f' será substituido pelo valor contido em valorTotal. O '.4' indica quantas casas decimais serão mostradas na tela, que no caso são duas.

##### Para aprender um pouco mais sobre tipos de variáveis: [Tipos de Variáveis](http://linguagemc.com.br/tipos-de-dados-em-c/)


###### Adento 1:
		
Ao invés de calcular a distância em cada eixo separadamente, pode-se substituir direto na fórmula, da seguinte forma:
```c
        dist = sqrt(pow(x2-x1,2)+pow(y2-y1,2));
```

