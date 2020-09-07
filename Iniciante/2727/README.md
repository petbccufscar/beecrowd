# Problema:

Joana gosta de brincar de fingir ser uma agente secreta com suas amigas Bruna, Jaqueline e Laura. Joana e Bruna criaram um código secreto para se comunicar sem que suas inimigas descubram seus planos.
O código secreto funciona da seguinte forma:

    -A letra 'a' é representada por um único ponto '.'
    -A letra 'b' é representada por dois pontos '..'
    -A letra 'c' é representada por três pontos '...'
    -As demais letras seguem a lógica anterior, porém cada conjunto de pontos está separado por um espaço e sempre com um conjunto a mais de pontos, como no exemplo abaixo:


**Problema completo:** https://www.urionlinejudge.com.br/judge/pt/problems/view/2727

# Resoluçāo:

Neste exercício declaramos 3 vetores que organizam as letras de acordo com a ordem do número de espaços, ou seja, o código do primeiro elemento não tem espaço, e cada elemento seguinte tem um espaço a mais que o anterior. Também cada vetor representa um padrão de pontos. Isto é, o primeiro vetor representa letras em que o código tem apenas 1 ponto entre os espaços, o segundo vetor representa letras em que o código tem 2 pontos entre os espaços e o terceiro vetor representa letras em que o código tem 3 pontos entre espaços.  

De modo geral, a ideia deste problema é acharmos a quantidade de espaços e o padrão de pontos que a letra tem. A partir destes dados, a letra traduzida será encontrada no vetor com o padrão de pontos dela e na posição que corresponde a quantidade de espaço da mesma.

Primeiramente, como iremos trabalhar com string e alocação dinâmica, é necessário declarar estas duas bibliotecas abaixo:

```c
    #include <stdlib.h>
    #include <string.h>
```

A seguinte, declaramos as variáveis inteiras `n`(número de letras), `i` e `j` são auxiliares para iteração dentro de loops. Usamos `qtd` como um contador de pontos que o padrão do código tem e `espaco` é utilizada para contar a quantidade de espaços que o código possui.

O vetor de caracteres `*letra` é usado para guardar a o código da letra que queremos traduzir.

```c
    int n, i, j, qtd, espaco;
    char *letra;
```

Abaixo declaramos 3 vetores de caracteres, cada um deles possui letras conforme o padrão de pontos do código, por exemplo `um[10]` só tem letras que tem um ponto entre espaços. Cada vetor guarda conjunto de letras de acordo com o modelo de pontos, sendo assim `dois[10]` tem o padrão de letras com 2 pontos e `tres[10]` tem o de 3 pontos.

```c
    char um[10] = {'a', 'd', 'g', 'j', 'm', 'p', 's', 'v', 'y', '\0'};
    char dois[10] = {'b', 'e', 'h', 'k', 'n', 'q', 't', 'w', 'z', '\0'};
    char tres[10] = {'c', 'f', 'i', 'l', 'o', 'r', 'u', 'x', '\0'};
```

O laço do `while` é repetido enquanto o fim do arquivo não for lido , usamos a constante `EOF` para fazer esta comparação. Por seguinte, usamos a função `fflush` passando o `stdin` como parâmetro para poder limpar o buffer, a fim de evitar que caracteres não desejados sejam lidos.

```c
    while ((scanf("%d", &n)) != EOF)
    {
        fflush(stdin);
```

Dentro do `for` mais externo iniciamos as variáveis `qtd` e `espaco` com o valor de 0, para evitar que acumule os valores relacionados a outros códigos. 

Por seguinte, usamos a função `malloc` para alocar dinâmicamente um espaço na memória para a variável `letra`, e após isto, guardamos o valor da mesma dentro de um `scanf`. Note que alocamos o tamanho de `char` multiplicado por 100, pois é o máximo que `*letra` pode ter.

```c
    for (i = 0; i < n; i++)
        {
            qtd = 0;
            espaco = 0;
            letra = (char *)malloc(100 * sizeof(char));

            scanf("%[^\n]%*c", letra);
```

Neste laço, percorremos cada caractere de `letra` a fim de contar a quantidade de espaços e descobrir qual é o padrão de pontos do código correspondente. 

Na primeira estrutura condicional `if` é verificado se o caractere atual é um espaço, caso seja, `espaco` é acrescida de uma unidade. Dentro do `else` a quantidade de pontos apenas é aumentada se ainda não achou nenhum caractere de espaço.

```c
            for (j = 0; j < strlen(letra); j++)
            {
                if (letra[j] == ' ')
                {
                    espaco++;
                }
                else
                {
                    if (espaco == 0)
                    {
                        qtd++;
                    }
                }
            }
```

Em seguida, com o padrão do código já descoberto, imprimimos a letra correspondente, de acordo com os valores `qtd` e `espaco` .  

```c
    if (qtd == 1)
        printf("%c\n", um[espaco]);
    else if (qtd == 2)
        printf("%c\n", dois[espaco]);
    else if (qtd == 3)
        printf("%c\n", tres[espaco]);

```

##### Para aprender um pouco mais sobre vetores de caracteres: [Vetores de caracteres](http://linguagemc.com.br/string-em-c-vetor-de-caracteres/)
 
Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
