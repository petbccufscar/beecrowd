# Problema

Certo dia, os irmãos Little Chitão e Xor Or Oh, exímios digitadores, fizeram um desafio, para ver quem era o melhor na digitação. Para isto, conseguiram um computador que não processa teclas pressionadas, ou seja, se for para digitar a mesma letra duas vezes seguidas, precisa pressionar a tecla duas vezes, visto que, pressionar a tecla por mais tempo, não adianta. Também mediram o tempo de uma tecla pressionada, que foi de, exatamente, um centésimo de segundo. O desafio seria quem digitasse a palavra “galopeira”, formada por mais letras e, mas ambos eram muito bons, e chegava num ponto que não era possível contar quantas letras haviam sido digitadas. Então, pediram a sua ajuda para escrever um programa que verifique a palavra digitada e veja quanto tempo foi gasto para a digitação.

Escreva um programa que, dada uma palavra digitada, informe quanto tempo foi gasto para ser digitada.

# Resolução

Para resolver o problema, iremos receber a quantidade de vezes que a palavra será inserida e, enquanto a palavra é recebida, iremos calcular o tamanho da palavra e transformá-la em tempo.

Começamos incluindo a biblioteca `string.h`, que contém os tipos de vetores de caracteres e funções como a `strlen`, que usaremos para contar do tamanho dos vetores.
```c
	#include <string.h>
```

Agora, iremos declarar as variáveis que serão utilizadas em nossa resolução. 
Primeiro, as variáveis inteiras de quantidade de casos, `casos`, e para armazenar o tamanho da palavra, `tam`.
```c
    int casos, tam;
```

Depois, a variável que armazenará a palavra, que será do tipo `char` por ser formada por caracteres. Terá o tamanho máximo da palavra explicitado no enunciado, de 10000.
```c
    char galopeira[10000];
```

Em seguida, utilizaremos a função `scanf` para ler a quantidade de casos que serão recebidos.
```c
    scanf("%d", &casos);
```

Inicializamos a estrutura de repetição `while`. Seu critério de parada será quando `casos` for igual a 0. 
Abaixo, utilizando a estrutura `scanf`, iremos ler a palavra.
```c
    while(casos>0)
        scanf("%s", galopeira);
```

Verificamos o tamanho da palavra lida com a função `strlen` e salvamos na variável de tamanho `tam`.
```c
        tam = strlen(galopeira);
```

Com isso, exibimos o tempo utilizado em cada palavra com a estrutura `printf`.
```c
        printf("%.2lf\n", tam*.01);
```

Como acabamos de ler um caso, subtraímos o número de casos que ainda faltam.
```c
        casos--;
```

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com