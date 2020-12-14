# Problema: 
Em chats, é muito comum entre jovens e adolescentes utilizar sequências de letras, que parecem muitas vezes aleatórias, para representar risadas. Alguns exemplos comuns são:

huaauhahhuahau
hehehehe
ahahahaha
jaisjjkasjksjjskjakijs
huehuehue

Cláudia é uma jovem programadora que ficou intrigada pela sonoridade das “risadas digitais”. Algumas delas ela nem mesmo consegue pronunciar! Mas ela percebeu que algumas delas parecem transmitir melhor o sentimento da risada que outras. A primeira coisa que ela percebeu é que as consoantes não interferem no quanto as risadas digitais influenciam na transmissão do sentimento. A segunda coisa que ela percebeu é que as risadas digitais mais engra¸cadas são aquelas em que as sequências de vogais são iguais quando lidas na ordem natural (da esquerda para a direita) ou na ordem inversa (da direita para a esquerda), ignorando as consoantes. Por exemplo, “hahaha” e “huaauhahhuahau” estão entre as risadas mais engraçadas, enquanto “riajkjdhhihhjak” e “huehuehue” não estão entre as mais engraçadas.

Cláudia está muito atarefada com a análise estatística das risadas digitais e pediu sua ajuda para escrever um programa que determine, para uma risada digital, se ela é das mais engraçadas ou não.

**Problema completo**: https://www.urionlinejudge.com.br/judge/pt/problems/view/2242

# Resolução:

Para resolver esse problema, a lógica é a seguinte: lê-se uma risada, depois exclui-se as consoantes presentes nela e, por fim, verifica-se se a risada, composta apenas por vogais, restante quando lida na ordem natural e inversa é a mesma.
Iniciando, declaramos as bibliotecas de funções que usaremos: `<stdio.h>`, para leitura e impressão de informações, e `<stdlib.h>`, para comparações entre strings e leitura de comprimento da risada.
``` c 
#include <stdio.h>
#include <stdlib.h>
```

Agora, declara-se as variáveis, a serem utilizadas: do tipo `char`, usa-se dois vetores: `risada[100]`, para armazenar a risada inicial e `risa_invertida[100]`, para armazenar o contrário da risada lida; do tipo `int`, `i` e `j`, para uso em loops, `comprimento`, para armazenar o comprimento da risada.
``` c
    char risada[100], risada_invertida[100];
    int i, j, comprimento;
```

Prosseguindo, lê-se a risada e depois, com o uso da função `strlen`, defini-se o comprimento dela.
``` c
    scanf("%s", &risada);
    comprimento = strlen(risada);
```

Usando o valor do comprimento, abri-se um loop `for`, onde cada caractere da risada será acessado. Assim sendo, verifica-se se o caractere acessado é diferente de todas as vogais minúsculas, configurando uma consoante. Caso seja uma consoante, abri-se outro loop `for` para que cada caractere seguinte a consoante seja colocado um índice prévio em `risada` - o loop tem como limite `comprimento` menos 1 para contar a exclusão da consoante - dessa forma, as consoantes serão sobrescritas. Por fim, na última posição do vetor de caracteres coloca-se '\0' indicando que aquela posição é o novo fim do vetor. Ademais, diminuí-se o comprimento e a variável `i`, para evitar-se acesso a valores que não existem mais e evitar-se que uma consoante seja passada sem ser analisada(isso pode acontecer caso haja duas consoantes seguidas e `i` não seja diminuído para que elas sejam testadas individualmente).
``` c
    for (i=0; i<comprimento; i++) {
        if ((risada[i] != 'a') && (risada[i] != 'e') && (risada[i] != 'i') && (risada[i] != 'o') && (risada[i] != 'u')) {
                for (j=i; j<(comprimento-1); j++) {
                    risada[j] = risada[j+1];
                }
                risada[comprimento-1] = '\0';
                comprimento--; 
                i--;
        }
    }
```

Seguindo, precisa-se configura a risada invertida para futura comparação. Assim sendo, zera-se o valor de `j`, cria-se um loop `for` com `i` inciando no último elemento de `risada` e diminuindo até o primeiro elemento. Dessa forma, usa-se `j` para acessar os primeiros itens de `risada_invertida` e `i` para acessar os últimos elementos de `risada` e armazena-los em seu correspondente invertido. Por fim, armazena-se '\0' no último elemento da risada inversa, para finalizar o vetor. 
``` c
    for(i=comprimento-1; i>=0; i--) {
        risada_invertida[j] = risada[i];
        j++;
    }
    risada_invertida[j] = '\0';
```

Por fim, basta comparar as risadas e imprimir a mensagem necessária. Para tal, usa-se a função `strcmp`, tendo como parâmetros as risadas, dentro de uma estrutura condicional `if`. Caso elas forem diferentes a função retornará um valor diferente de zero, entrando na condição verdadeira de `if` e imprimindo "N\n". Caso forem diferentes, a função retorna 0, entrando na condição falsa de `if` e imprimindo "S\n". Para encerrar o program usa-se `return 0`.
``` c 
    if (strcmp(risada, risada_invertida)) {
        printf("N\n");
    }
    else {
        printf("S\n");
    }
    return 0;
```

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
