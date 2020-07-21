# Problema:

Faça um programa que calcule e mostre o volume de uma esfera sendo fornecido o valor de seu raio (R). A fórmula para calcular o volume é: (4/3) * pi * R<sup>3</sup>. Considere (atribua) para pi o valor 3.14159.

Dica: Ao utilizar a fórmula, procure usar (4/3.0) ou (4.0/3), pois algumas linguagens (dentre elas o C++), assumem que o resultado da divisão entre dois inteiros é outro inteiro.

**Problema completo**: https://www.urionlinejudge.com.br/judge/pt/problems/view/1011

# Resolução:

Devemos receber do usuário o valor do raio de uma esfera, calcular o volume e exibir o resultado na tela. Felizmente, o enunciado nos dá a fórmula para isso.

Como a fórmula requer uma potência R<sup>3</sup>, utilizaremos uma função chamada `pow()` que realiza potenciações. Para utilizá-la, devemos importar no início do nosso código uma biblioteca que contém essa função, chamada `math.h`.

```c
    #include <math.h>
```

Dentro da função main(), criaremos uma variável para armazenar o valor do raio e faremos sua leitura. Na instrução de entrada, é apontado que o raio possui valor de **ponto flutuante de dupla precisão**, por isso, utilizaremos o tipo de variável `double` e o argumento `%lf` para ler/escrever.

```c
        double raio;
        scanf("%lf", &raio);
```

Aplicaremos a fórmula para cálculo de volume utilizando o valor 3.14159 para PI, conforme especificado no enunciado. A função pow utiliza a estrutura `pow(base, expoente)`, ou seja, para calcular R<sup>3</sup>, faremos a chamada `pow(raio, 3)`. O exercício também sugere utilizar a expressão (4.0/3) para evitar problemas entre valores inteiros e decimais em alguns compiladores.

```c
    double volume = (4.0/3) * 3.14159 * pow(raio, 3);
```

Por último, basta exibir o resultado conforme os exemplos de saída do exercício. Para limitar a exibição a apenas 3 casas decimais, utilizamos `%.3lf` ao invés de `%lf`, sendo `.3` o número de casas após a vírgula. Como todo bom exercício, não podemos esquecer de quebrar a linha ao final, utilizando `\n` - a omissão causaria um erro de apresentação.

```c
    printf("VOLUME = %.3lf\n", volume);
```

##### Para aprender mais sobre formatação de saída: [A printf format reference page](https://alvinalexander.com/programming/printf-format-cheat-sheet/)

##### Para aprender mais sobre variáveis de ponto flutuante: [Os tipos float e double](https://www.cprogressivo.net/2012/12/Os-tipos-float-e-double-numeros-decimais-reais-em-C.html)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com