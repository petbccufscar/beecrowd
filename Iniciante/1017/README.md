# Problema:

Joaozinho quer calcular e mostrar a quantidade de litros de combustível gastos em uma viagem, ao utilizar um automóvel que faz 12 KM/L. Para isso, ele gostaria que você o auxiliasse através de um simples programa. Para efetuar o cálculo, deve-se fornecer o tempo gasto na viagem (em horas) e a velocidade média durante a mesma (em km/h). Assim, pode-se obter distância percorrida e, em seguida, calcular quantos litros seriam necessários. Mostre o valor com 3 casas decimais após o ponto.

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/1017

# Resolução:

Uma forma de resolver o problema é calcular a distância e depois dividí-la por 12.

Para representar isto em nosso programa, fazemos: 

```c
        int tempo, velocidade;
        float dist;
```

Para ler as variáveis, usa-se scanf:

```c
        scanf("%d", &tempo);

        scanf("%d", &velocidade);
```

Em seguida, calcula-se a distância e escrevemos o resultado na tela utilizando a função printf:

```c
        printf("%.3f \n", dist/12);
```

O '%0.3f' será substituido pelo valor contido em valorTotal. O '.3' indica quantas casas decimais serão mostradas na tela, que no caso são três.


Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou envie um e-mail com o assunto "URI" para petbcc.ufscar@gmail.com

