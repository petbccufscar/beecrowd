# Problema:

Joaozinho quer calcular e mostrar a quantidade de litros de combustível gastos em uma viagem, ao utilizar um automóvel que faz 12 KM/L. Para isso, ele gostaria que você o auxiliasse através de um simples programa. Para efetuar o cálculo, deve-se fornecer o tempo gasto na viagem (em horas) e a velocidade média durante a mesma (em km/h). Assim, pode-se obter distância percorrida e, em seguida, calcular quantos litros seriam necessários. Mostre o valor com 3 casas decimais após o ponto.

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/1017

# Resolução:

Uma forma de resolver o problema é calcular a distância, multiplicando a velocidade média pelo tempo, e depois dividí-la por 12, pois o automóvel faz 12 KM/L, para obter-se quantos litros são necessários.

Para representar estes valores em nosso programa, declaramos tempo e velocidade como inteiros, conforme a entrada, e a distância como float, para o resultado do cálculo da quantidade de litros (dist/12) imprimir as casas decimais. 

```c
        int tempo, velocidade;
        float dist;
```

Para ler a entrada, usa-se `scanf`:

```c
        scanf("%d", &tempo);

        scanf("%d", &velocidade);
```

Em seguida, calcula-se a distância e, já que o automóvel faz 12 KM/L, divide-a por 12 e escreve-se este resultado na tela utilizando a função `printf`:

```c
		dist = tempo*velocidade;

        printf("%.3f \n", dist/12);
```

O `%.3f` será substituido pelo resultado da divisão de `dist` por 12. O '.3' indica quantas casas decimais serão mostradas na tela, que no caso são três.


Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou envie um e-mail com o assunto "URI" para petbcc.ufscar@gmail.com

