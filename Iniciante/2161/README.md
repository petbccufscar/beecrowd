# Problema:

Uma das formas de calcular a raiz quadrada de um número natural é pelo método das frações periódicas continuadas. Esse método usa como denominador uma repetição de frações. Essa repetição pode ser feita uma quantidade específica de vezes.

Por exemplo, ao repetir 2 vezes a fração continuada para calcular a raiz quadrada de 10, temos a fórmula abaixo.

![Imagem do exercício](https://resources.urionlinejudge.com.br/gallery/images/contests/933.png)

**Problema completo:** https://www.urionlinejudge.com.br/judge/pt/problems/view/2161

# Resoluçāo:

A ideia de resolver este exercício é que para cada  iteração, incrementamos o valor da raiz em 6 e a dividimos por 1 sob o valor atual da raiz, fazendo esse cálculo durante n repetições; e ao final adicionamos 3 o resultado final.

Primeiramente, declaramos as variáveis inteiras `nro`, que é o número de repetições; `i` é responsável pelo controle do laço `for`. Do mesmo modo também definimos a variável de ponto flutuante `raiz`, que guardará o valor da raiz de 10 que vai ser calculada.

```c
   int nro, i;
   float raiz = 0.0;
```

Fazemos a leitura do valor de `nro`.
```c
   scanf("%d", &nro);
```

Esse é o laço em que, é feito o cálculo das divisões periódicas da `raiz`, a cada interação `raiz` tem seu valor aumentado em 6 e depois seu valor é alterado para `1/raiz`. Estes passos é feito pela quantidade de `nro` vezes.
```c
   for (i = 0; i < nro; i++)
   {
      raiz += 6.0;
      raiz = 1.0 / raiz;
   }
```

Ao final, acrescentamos 3 a `raiz`, de acordo com a fórmula do exercício.
```c 
   raiz += 3.0;
```

Dessa forma, exibimos a raiz de 10 que foi calculada. 

```c
   printf("%.10f\n", raiz); 
```
 
##### Para aprender um pouco mais sobre laço de repetição: [Laços](http://linguagemc.com.br/estruturas-de-repeticao/)
 
Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
