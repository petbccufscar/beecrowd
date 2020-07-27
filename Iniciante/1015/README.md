# Problema:

Leia os quatro valores correspondentes aos eixos x e y de dois pontos quaisquer no plano, p1(x1,y1) e p2(x2,y2) e calcule a distância entre eles, mostrando 4 casas decimais após a vírgula, segundo a fórmula:


Distancia = raiz((x2 − x1)<sup>2</sup> + (y2 − y1)<sup>2</sup>)

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/1015

# Resolução:

Para resolver o problema, realiza-se a leitura dos dados e aplicá-os diretamente na fórmula dada. Além disso, iremos importar a biblioteca `math.h`, para utilizarmos a função de raiz quadrada`sqrt()` e a função de potência`pow()` .

Vale pontuar que a distância entre dois pontos é a medida do seguimento de reta que os une(`dist`). 

Primeiramente, para representar os valores em nosso programa, fazemos: 

```c
        float x1, y1, x2, y2, distX, distY, dist;
```

**Vale ressaltar que, `distX` representa a distancia entre os pontos no eixo x, `distY` representa a distancia entre os pontos no eixo y e `dist` representa a distancia entre os pontos.**

Para ler a entrada, usa-se `scanf`:

```c
        scanf("%f %f", &x1, &y1);

        scanf("%f %f", &x2, &y2);
```

É possível inserir mais de um dado dentro de um mesmo `scanf` separando os %(variavel), lembrando que a ordem da variaveis inseridas entre as aspas deve corresponder com a ordem dos endereços de memoria indicados na função. 

Após a leitura das variáveis, calcula-se a distância em cada eixo:

```c
        distX = x2-x1;

        distY = y2-y1;
```

Em seguida, calculamos a distância de acordo com a fórmula e escrevemos o resultado na tela utilizando a função `printf`:

```c
        dist = sqrt(pow(distX,2)+pow(distY,2));
   
        printf("%.4f\n", dist);
```

O `%.4f` será substituido pelo valor contido em `dist`. O '.4' indica quantas casas decimais serão mostradas na tela, que no caso são quatro.


##### Para revisar sobre a biblioteca math.h: [Biblioteca math.h](http://linguagemc.com.br/a-biblioteca-math-h/)


Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou envie um e-mail com o assunto "URI" para petbcc.ufscar@gmail.com