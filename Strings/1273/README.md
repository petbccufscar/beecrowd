# Problema

Nós temos algumas palavras e queremos justificá-las à direita, ou seja, alinhar todas elas à direita. Crie um programa que, após ler várias palavras, reimprima estas palavras com suas linhas justificadas à direita.


###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/1273

# Resolução

Para resolver esse problema, precisamos primeiro receber quantas palavras justificaremos e todas as palavras. Assim, conseguimos descobrir a maior palavra e quanto para a direita precisaremos afastar a palavra para justificá-la em relação a maior.

Como faremos algumas comparações ente dois inteiros para definir o maior entre eles, criamos a função `int max(int a, int b)` que com um `if` nos retorna o maior entre os dois números a serem comparados, aqui definidos como `a` e `b`.

```c
int max(int a,int b){
    if(a>b)
        return a;
    else
        return b;
}
```

Usaremos a biblioteca `string.h` para utilizar a função `strlen(char* string)` que nos retorna o tamanho de uma dada string.

```c
#include <string.h>

```

Começaremos declarando as variáveis que iremos utilizar. `N` será quantas palavras receberemos (0 para parar a execução), `i`, `j` e `t` são auxiliares, `maior_palavra` é o tamanho da maior palavra recebida. A matriz `palavras[50][50]` é uma lista de palavras, que recebe até 50 palavras de tamanho 50.

```c
    int N, i,maior_palavra = 0, j,t;
    char palavras[50][50];
```

Assim, recebemos o valor do primeiro `N` e iniciamos o loop para os próximos valores, ao fim do loop recebemos o próximo `N` para novamente passar pela verificação do `while`.

```c
    scanf("%d",&N);
    while(N != 0){

        scanf("%d",&N);
    }
```

Dentro do loop, começamos zerando a variável `maior_palavra`, que será diferente para cada conjunto de palavras recebida. Logo em seguida, criamos um loop para receber todas as `N` palavras e a cada palavra recebida, substituímos o conteúdo da variável `maior_palavra` pelo retorno da função `max()` que retorna o maior entre o tamanho da palavra atual e da `maior_palavra`.


```c
while(N != 0){
    
    maior_palavra = 0;

    for(i = 0; i < N; i++){
        scanf("%s",palavras[i]);
        maior_palavra = max(maior_palavra,strlen(palavras[i]));   
    }

    /* Continuação omitida */

}
```

Agora, tendo o tamanho da maior palavra armazenado em `maior_palavra` percorreremos todas as palavras em um outro loop `for` e em cada iteração determinaremos o `t` que será a quantidade de espaços necessários para que a palavra se alinhe com a maior (a direita). Assim, com um loop de 0 a t, printando espaços na tela e logo em seguida a palavra, temos o resultado desejado.

```c
while(N != 0){
        
    /* Continuação omitida */

    for(i = 0; i < N; i++){
        t = maior_palavra - strlen(palavras[i]);
        for(j=0;j<t;j++){
            printf(" ");
        }
        printf("%s\n",palavras[i]);
    } 
    scanf("%d",&N);
    if(N != 0)
    printf("\n");
    
}
```

Ao término dos prints, faremos o `scanf` do próximo `N` para receber as próximas palavras e caso não seja um 0 (que é o comando para finalizar a execução) exibimos uma quebra de linha, assim como sugerido nas especificações do exercício.



##### Para aprender um pouco mais sobre a biblioteca string: [strings](http://linguagemc.com.br/a-biblioteca-string-h/)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou envie um e-mail com o assunto "URI" para petbcc.ufscar@gmail.com
