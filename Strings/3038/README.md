# Problema:   
O Senhor Claus recebe as mais diversas cartas de crianças do mundo todo. Todo ano, sem exceções, ele seleciona algumas das cartas mais legais para dar maior atenção a elas. Neste ano, uma dessas cartas chamou a atenção de Claus por um motivo bem peculiar: a carta estava criptografada! Nela, continha a carta com o pedido de natal, e um bilhete anexado que dizia o seguinte:

"Sr. Papai Noel: imagino que você deva receber muitas cartas de natal, mas deve ser quase chato ter que ler todas elas sem nenhum desafio. Espero que a minha traga um pouco de diversão ao senhor. Eu troquei todas as vogais das palavras por símbolos. Use essa tabela para traduzir meu pedido!"

Vamos ajudar o Senhor Claus a traduzir essa carta?

**Problema Completo**: https://www.urionlinejudge.com.br/judge/pt/problems/view/3038

# Resolução:

A ideia por trás da resolução deste exercício é apenas substituir os caracteres especiais por suas respectivas versões de caracteres do alfabeto. Para isso iniciamos a resolução deste exercício incluindo duas bibliotecas que serão utilizadas durante o processo `stdio.h` para usar funções de `input e output`, e a biblioteca `string.h` para utilizarmos funções que tratam strings.

```c
#include <stdio.h>
#include <string.h>
```

Iremos declarar também algumas variáveis, uma do tipo `int` para usarmos como auxiliar em nosso laço de repetição e uma do tipo vetor de caracteres, ou string, para armazenarmos as frases que serão passadas para serem descriptografadas

```c
int i;
char texto[300];
```

Iremos utilizar um laço de repetição geral que ira ficar lendo e esperando por novas frases, o parâmetro `%[^\n]%*c` faz com que seja feita a leitura até que se encontre um `\n` indicando o fim de linha, ao encontrar atribuirmos isso à nossa variável `texto`, porem, colocamos o **~** antes de nossa função `~scanf()` pois com a função `scanf` ao ler algum dado nos retorna valor "0", ao negarmos isso fazemos com que nosso loop continue enquanto esteja lendo algo ou seja ainda há frases para serem tratadas, caso falso apenas saímos de nosso loop e encerramos.

```c
while (~scanf("%[^\n]%*c", texto)){
    ...
}
```

dentro de nosso laço principal iremos percorrer o texto que foi lido, iterando por cada um de seus caracteres buscando por caracteres especiais para realizamos as devidas trocas, para isso realizamos um cadeia de `if` e `else` abordando todos os casos que devem ser tratados

```c
for (i = 0; i < strlen(texto); i++){
    if (texto[i] == '@')
        texto[i] = 'a';
    else if (texto[i] == '&')
        texto[i] = 'e';
    else if (texto[i] == '!')
        texto[i] = 'i';
    else if (texto[i] == '*')
        texto[i] = 'o';
    else if (texto[i] == '#')
        texto[i] = 'u';        
}
```

Após cada leitura de frase juntamente com suas alterações, por final nos resta apenas imprimir a frase em seu novo formato, para isso realizamos um novo loop, iterando por cada posição de nosso texto e imprimindo o caractere presente naquela posição. Ao final, quando já acabamos de imprimir todo nosso texto precisamos imprimir um `\n` para que a próxima frase fique na linha de baixo, mantendo assim a formatação solicitada pelo URI.

```c
for (i = 0; i < strlen(texto); i++){
    printf("%c", texto[i]);
}

printf("\n");
```

É valido acentuar que há varias formas de se resolver esse problema, um exemplo é para cada caractere lido já realizamos a troca para seu devido caractere do alfabeto e já o imprimimos, evitando assim a realização de vários loops para realizar leitura e impressão, porém optei por essa forma de resolução para deixar mais simples a explicação da logica por trás.


    
Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com