# Problema:

Alguns algoritmos de processamento de imagem exigem um pré-processamento no qual é necessário transformar uma imagem colorida em uma imagem em tons de cinza. Esta conversão pode ser realizada de diversas maneiras, dependendo do resultado que se pretende obter.

Para preservar a percepção das cores básicas pelo olho humano, uma conversão apropriada seria tomar 30% da componente vermelha (R), 59% da componente verde (G) e 11% da componente azul (B). Em termos matemáticos,

```
P = 0, 30R + 0, 59G + 0, 11B
```

Outras abordagens possíveis seriam determinar o valor de P através da média aritmética das três componentes ou atribuir a P os valores da maior ou da menor entre as três componentes.

Dadas as componentes RGB de um pixel da imagem colorida, determine o valor do pixel P da imagem em tons de cinza correspondente, determinada a conversão a ser utilizada. Despreze a parte decimal do resultado, caso exista.

##### Link do problema: https://www.urionlinejudge.com.br/judge/pt/problems/view/2630
 
 
# Resolução:

O exercício nos dá 4 maneiras diferentes de converter um pixel colorido para um pixel cinza. Vamos escrever 4 funções que calculam cada abordagem e, para cada caso de teste, mostrar o resultado dessa função. Como precisamos ler o nome da abordagem e compará-lo com "eye", "mean" e etc, vamos precisar incluir a biblioteca `string.h` no início do código, para poder manipular melhor strings.

```c
#include <string.h>
```

Em seguida, escrevemos as 4 abordagens para converter o pixel. A primeira, caracterizada por manter a percepção de cores do olho humano, seguirá o cálculo estabelecido no enunciado - recebe os valores do pixel RGB e retorna o resultado do cálculo.

```c
int eye(int R, int G, int B) {
    return (0.3 * R) + (0.59 * G) + (0.11 * B);
}
```

A segunda, referida como "mean" no exemplo de entrada, é uma média aritmética simples. Vamos somar os valores de R, G e B e dividir por 3.

```c
int mean(int R, int G, int B) {
    return (R + G + B) / 3;
}
```

A função `max` retorna o maior valor entre as 3 cores. Para isso, comparamos todos os valores entre si: se `R` for maior ou igual a `G` e `B`, retornamos `R` pois é o maior valor. Fazemos o mesmo para as outras variáveis.

```c
int max(int R, int G, int B) {
    if (R >= G && R >= B) {
        return R;
    }
    else if (G >= R && G >= B) {
        return G;
    }
    else {
        return B;
    }
}
```

A função `min` é similar à `max`, mas verificando se um valor é _menor ou igual_ aos outros dois.

```c
int min(int R, int G, int B) {
    if (R <= G && R <= B) {
        return R;
    }
    else if (G <= R && G <= B) {
        return G;
    }
    else {
        return B;
    }
}
```

Tendo as 4 abordagens definidas como funções, podemos começar o método `main()` para resolver o exercício. Primeiro, declaramos todas as variáveis que vamos utilizar: `casos` para armazenar a quantidade de casos de teste, `i` para percorrer cada caso; `R`, `G`, `B` e `P` para guardar os valores de cada pixel e `abordagem[4]`, um vetor de 4 caracteres para identificar qual função deve ser utilizada.  
Note que utilizamos 4 posições pois o maior nome de abordagem é `mean`.

```c
int casos, i;
int R, G, B, P;
char abordagem[4];
```

Em seguida, fazemos a leitura do número de casos.

```c
scanf("%d", &casos);
```

Como precisamos exibir o número do caso atual, vamos começar nosso loop em `i = 1` e repetir enquanto `i <= casos`.

```c
for (i = 1; i <= casos; i++) {
```

Para cada caso, vamos ler a abordagem e os 3 valores do pixel RGB.

```c
    scanf("%s", abordagem);
    scanf("%d %d %d", &R, &G, &B);
```

Para definir qual função chamar, precisamos comparar o texto salvo em `abordagem` com a função `strcmp()`, importada pela biblioteca `string.h`. Essa função retorna o valor `0` quando duas strings são iguais. Caso o valor de `abordagem` seja igual a `"eye"`, o pixel `P` recebe o cálculo de `eye(R, G, B)`.

```c
    if (strcmp(abordagem,"eye") == 0) {
        P = eye(R, G, B);
    }
```

Repetimos a lógica para os outros casos, com as condicionais `else if`.

```c
    else if (strcmp(abordagem, "mean") == 0) {
        P = mean(R, G, B);
    }
    else if (strcmp(abordagem, "max") == 0) {
        P = max(R, G, B);
    }
    else if (strcmp(abordagem, "min") == 0) {
        P = min(R, G, B);
    }
```

Por fim, imprimimos o número do caso e o valor calculado de `P`.

```c
    printf("Caso #%d: %d\n", i, P);
}
```

##### Para revisar sobre funções: [Funções em C](http://linguagemc.com.br/funcoes-em-c/)
##### Para aprender sobre as funções da biblioteca `string.h`: [A biblioteca string.h](http://linguagemc.com.br/a-biblioteca-string-h/)


Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com