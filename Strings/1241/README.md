# Problema:
Paulinho tem em suas mãos um novo problema. Agora a sua professora lhe pediu que construísse um programa para verificar, à partir de dois valores muito grandes A e B, se B corresponde aos últimos dígitos de A.

**Problema Completo**: https://www.urionlinejudge.com.br/judge/pt/problems/view/1241


# Resolução:
De início, como manipularemos strings, devemos incluir as bibliotecas de funções necessárias. Nesse caso, `<stdio.h>` para receber os dados do usuário e impressão de mensagens, e `<string.h>` para manipulação de string. 
``` c
#include <stdio.h>
#include <string.h>
```

Na sequência, declaramos as variáveis que usaremos para nosso programa, primeiramente as do tipo integral:`casos_testes` para armazenar a quantidade de testes que serão realizados por vez; `a_tamanho` que receberá o comprimento do nosso vetor A; `b_tamanho` que receberá o comprimento do nosso vetor B; `encaixa` que receberá a quantidade de números finais que são iguais nos vetores A e B; `i` e `j` para serem contadores. Do tipo caractere temos: `a_valor` que será nosso vetor para receber, em cada elemento seu, os algarismos que compõem o valor A; `b_valor` que será nosso vetor para receber, em cada elemento seu, os algarismos que compõem o valor B. 
``` c
    int casos_testes, a_tamanho, b_tamanho, encaixa, j, i;
    char a_valor[1000], b_valor[1000];
```

Começando a leitura dos dados, recebemos, através de uma função `scanf`, o valor de quantos testes serão realizados e o armazenaremos em `casos_testes`. Com tal valor armazenado, criamos um loop `for`, usando `i`, que se repetirá a quantidade de vezes conforme o valor de `casos_testes`.
``` c
    scanf("%d", &casos_testes);
    for (i=0; i<casos_testes; i++) {
```

Dentro do loop, faremos a leitura dos valores A e B, armazenando-os nos vetores `a_valor` e `b_valor`, respectivamente. Atenção nesta parte, pois a leitura dos valores deve ser feita com especificador de formato de string `%s`, dessa forma cada algarismo dos valores serão interpretados como um caractere único, sendo armazenados unicamente em cada elemento do vetor formando uma string de números.
Sendo assim, como cada algarismo foi armazenado em cada elemento do vetor como uma string, usamos a função `strlen`(que retorna o comprimento de uma determinada string) para determinar o comprimento de cada vetor (consequentemente dos valores de A e B) e armazenamos tais valores em `a_tamanho` e `b_tamanho`, respectivamente. Fazemos tal passo para futuramente termos acesso a determinados algarismos dos valores A e B.
``` c
        scanf("%s", &a_valor);
        scanf("%s", &b_valor);

        a_tamanho = strlen(a_valor);
        b_tamanho = strlen(b_valor);
```

Agora, atribuimos o valor de 0 para a variável `encaixa`, para dar inicio ao ciclo de comparações. Em seguida, abrimos um loop `for`, com auxílio de `j`, que se repetirá a quantidade de vezes conforme o comprimento do valor B (tal comprimento foi armazenado em `b_tamanho`). 
Dentro do loop, através de uma estrutura `if`, acessaremos de trás para frente cada algarismo dos valores A e B, com o uso da variável `j`, que aumentará conforme o loop e com isso irá acessando cada algarismo dos valores. Se ambos os algarismos forem iguais, a variável `encaixa` tem seu valor aumentado em 1.
``` c
        encaixa = 0;
        for (j=1; j<=b_tamanho; j++) {
            if (a_valor[(a_tamanho-j)] == b_valor[(b_tamanho-j)]) {
                encaixa++;
            }
        }
```

Para encerrar nosso primeiro loop `for`, usamos uma estrutura `if` que comparará `encaixa` com `b_tamanho`, e se forem iguais impriremos, através do uso de `printf` "encaixa", caso contrário imprimimos "nao encaixa". A lógica dessa estrutura condicional é: como `encaixa` aumenta em 1 a cada algarismo final igual entre os valores A e B, se o valor de `encaixa` for igual ao tamanho do vetor B(`b_tamanho`), significa que todos os numeros do valor B estavam presentes no final do valor A. Por fim, finalizamos o programa com `return 0`.
``` c
        if (encaixa == b_tamanho) {
            printf("encaixa\n");
        }
        else {
            printf("nao encaixa\n");
        }
        
    }

    return 0;
}
```

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com