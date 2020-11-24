# Problema:
Rafael recentemente recebeu uma bolsa de estudos e está fazendo intercâmbio fora do Brasil, onde conheceu várias pessoas de várias nacionalidades diferentes. O idioma nativo desse país é o Inglês, e todas as pessoas que Rafael conheceu falam inglês como primeira ou segunda língua.

Como aprender um segundo idioma é uma tarefa difícil e cansativa, as pessoas preferem falar seu idioma nativo sempre que possível. Uma exceção à essa regra é quando há duas pessoas no grupo que não tem o mesmo idioma nativo. Nesse tipo de situação, o idioma utilizado é o inglês.

Por exemplo, se em um grupo há só brasileiros, o idioma falado será o português, mas caso haja um espanhol entre os brasileiros, o idioma falado será o inglês.

Rafael as vezes fica confuso sobre qual idioma deveria ser falado em cada grupo de pessoas, e para isso pediu sua ajuda.

##### Problema completo: [https://www.urionlinejudge.com.br/judge/pt/problems/view/1581]

# Resolução:
De início, incluímos as bibliotecas que serão necessárias para a resolução do problema. Dessa forma, precisaremos manipular strings, receber do usuário e imprimir informações, para tal usaremos as bibliotecas `string.h` e `stdio.h`.
``` c
#include <stdio.h>
#include <string.h>
```

Com as bibliotecas inclusas, iniciamos nossa função `main` com a declaração das variáveis: do tipo `int` usamos, `casos_testes` que receberá o quantidade de testes a serem realizados; `pessoas_grupo` que receberá o número de pessoas presente no grupo em teste; `idioma_igual` que será a variável de controle para receber a compareção dos idiomas, nela usamos o conceito de 1 para verdadeiro/igual e 0 para falso/diferente; `i` e `j` que serão usadas para loops. Além dessas, do tipo `char` usaremos dois vetores de 20 elementos, `idioma_atual` que receberá o idioma da pessoa em teste; `idioma_anterior` que armazenará o idioma passado em teste.
``` c
int main () {
    int casos_testes, pessoas_grupo, idioma_igual, i, j;
    char idioma_atual[20], idioma_anterior[20];
```

Dando prosseguimento, começamos por ler a quantidade de casos e, com o valor lido, abrimos um loop `for` com limite sendo a quantidade de casos. Já no loop, iniciamos lendo a quantidade de pessoas naquele grupo, o primeiro idioma falado pela primeira pessoa e configuramos a variável `idioma_igual` para 1(verdadeiro).
``` c 
    scanf("%d", &casos_testes);
    for (i=0; i<casos_testes; i++) {
        scanf("%d", &pessoas_grupo);
        scanf("%s", &idioma_anterior);
        idioma_igual = 1;
```

Com os dados lidos, abrimos outro loop `for` com limite o número de pessoas, daquele grupo em questão, menos 1, pois o idioma da primeira pessoa já foi lido. Nesse segundo loop, lemos o próximo idioma(referente a próxima pessoa). Com os dois idiomas lidos, dentro de uma estrutura condicional comparamos eles, por meio da função `strcmp`. Caso os idiomas sejam diferentes, `strcmp` retorna um valor diferente de 0, e configuramos a variavel de controle para 0(falso). Caso sejam iguais, a função retornará 0, assim copiamos o atual idioma para a variavel anterior com `strcpy` e damos continuidade ao loop `for`.
``` c
        for (j=0; j<(pessoas_grupo-1); j++) {
            scanf("%s", &idioma_atual);
            if (strcmp(idioma_anterior, idioma_atual)) {
                idioma_igual = 0;
            }
            else {
                strcpy(idioma_anterior, idioma_atual);
            }
        }
```

Finalizadas as comparações, faremos a avaliação da igualdade entre os idiomas. Sendo assim, abrimos uma estrutura condicional `if` com o uso da variável `idioma_igual` já com seu valor configurado previamente. Se os idiomas forem iguais imprimimos na tela o valor da váriavel `idioma_atual` que terá o valor do idioma unanimante predominante no grupo de pessoas. Caso forem diferentes, imprimimos a mensagem `"ingles\n"`. Assim encerramos o primeiro loop `for` e, para finalizar o programa, inserimos `return 0;`.
``` c
        if (idioma_igual) {
            printf("%s\n", idioma_atual);
        }
        else {
            printf("ingles\n");
        }
    }

    return 0;
}
```

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso [Facebook](https://www.facebook.com/petbcc/), [Instagram](https://www.instagram.com/petbcc.ufscar/) ou nos mande um e-mail com o assunto "URI" para petbcc.ufscar@gmail.com
