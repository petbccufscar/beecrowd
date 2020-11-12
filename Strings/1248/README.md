# Problema:

O doutor deu a você a sua dieta, na qual cada caractere corresponde a algum alimento que você deveria comer. Você também sabe o que você tem comido no café da manha e no almoço, nos quais cada caractere corresponde a um tipo de alimento que você deveria ter comido aquele dia. Você decidiu que irá comer todo o restante de sua dieta durante o jantar, e você quer imprimi-la como uma String (ordenada em ordem alfabética). Se você trapaceou de algum modo (ou por comer muito de tipo de alimento, ou por comer algum alimento que não está no plano de dieta), você deveria imprimir a cadeia "CHEATER" (significa trapaceiro), sem as aspas.

**Problema Completo**: https://www.urionlinejudge.com.br/judge/pt/problems/view/1248

# Resolução:

Para a resolução deste problema, além da biblioteca padrão `stdio.h`, é necessário incluir as bibliotecas `stdlib.h` e `string.h`.

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
```

Após informar as bibliotecas, temos uma função que servirá para fazer uma ordenação. Dentro do código, em determinado momento é necessário chamar uma função para fazer uma ordenação de caracteres, e o método utilizado foi o 'Insertion Sort' ou 'ordenação por inserção'. Segue abaixo o algoritmo para essa ordenação, e logo após iniciamos o nosso código principal.

```c
void insertionSort(char *array, int length) {
    int i, j;
    char tmp;

    for (i = 1; i < length; ++i) {
        tmp = array[i];
        j = i - 1;
        while (tmp < array[j]) {
            array[j + 1] = array[j];
            --j;
        }
        array[j + 1] = tmp;
    }
}
```

Iniciamos o nosso código principal com a declaração das variáveis que serão utilizadas para a resolução do problema. A entrada contém vários casos de teste, cada caso de teste é composto por três linhas, cada uma delas com uma string com até 26 caracteres de 'A'-'Z' ou vazia, representando respectivamente os alimentos da dieta, do café da manhã e do almoço.

Sendo assim, declaramos as variáveis do tipo inteiro: `N`, `dietLength`, `alreadyEatenLength`, `dinnerLength`, `i`, `j`, `k`, `cheater`, `isInDiet[26]`, `shouldEat[26]`; E as variáveis do tipo caractere: `diet[28]`, `alreadyEaten[54]`, `dinner[28]`. Em seguida, é feita a leitura da variável `N` através do comando scanf(), e com o comando getchar() a leitura dos caracteres informados (nas variáveis `diet[28]` e `alreadyEaten[54]`). Sendo que `N` é o número de casos testes a serem realizados, `diet[28]` são os alimentos da dieta, e `alreadyEaten[54]` são os alimentos comidos no café da manhã e no almoço.

```c
int main()
{
    int N;
    char diet[28], alreadyEaten[54], dinner[28];
    int dietLength, alreadyEatenLength, dinnerLength;
    int i, j, k, cheater;
    int isInDiet[26], shouldEat[26];

    scanf("%d", &N);
    getchar();

	/**
     * restante do código aqui (informado abaixo)
    **/

    return 0;
}
```

Após informado o número de casos testes, os alimentos da dieta e os alimentos comidos nas variáveis `N`, `diet[28]` e `alreadyEaten[54]`, temos que descobrir se a dieta foi trapaceada, e devemos escrever "CHEATER" caso a dieta tenha sido trapaceada, e caso a dieta não tenha sido trapaceada devemos informar quais são os alimentos que devem ser comidos no jantar, através da variável `dinner[28]`, e essa análise é feita como demonstrado no trecho do algoritmo abaixo.

```c
    for (i = 0; i < N; ++i) {
        memset(shouldEat, 1, sizeof(shouldEat));
        memset(isInDiet, 0, sizeof(isInDiet));

        fgets(diet, 28, stdin);
        dietLength = strlen(diet) - 1;

        fgets(alreadyEaten, 28, stdin);
        alreadyEatenLength = strlen(alreadyEaten) - 1;

        fgets(alreadyEaten + alreadyEatenLength, 28, stdin);
        alreadyEatenLength = strlen(alreadyEaten) - 1;

        for (j = 0; j < dietLength; ++j)
            isInDiet[diet[j] - 'A'] = 1;

        cheater = 0;
        for (j = 0; j < alreadyEatenLength && !cheater; ++j) {
            k = alreadyEaten[j] - 'A';

            if (!(isInDiet[k] && shouldEat[k]))
                cheater = 1;
            else
                shouldEat[k] = 0;
        }

        if (cheater)
            puts("CHEATER");
        else {
            insertionSort(diet, dietLength);

            dinnerLength = 0;
            for (j = 0; j < dietLength; ++j) {
                if (shouldEat[diet[j] - 'A'])
                    dinner[dinnerLength++] = diet[j];
            }
            dinner[dinnerLength] = '\0';

            puts(dinner);
        }
    }
```

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/),
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
