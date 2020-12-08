# Problema:

Em muitos idiomas uma regra deve ser seguida ao escrever qualquer texto digital : não use espaço em branco antes de uma vírgula ou um ponto .

Escreva um programa que, dado um texto de entrada, remove todo espaço que é imediatamente sucedido por uma vírgula ou por um ponto. Se houver mais do que um espaço que satisfaz esta condição, remova apenas um deles.

##### Link do problema: https://www.urionlinejudge.com.br/judge/pt/problems/view/3088
 
# Resolução:

O exercício consiste em ler casos de teste até acabar o arquivo e, para cada caso de teste, teremos que retirar os espaços à esquerda do ',' e '.'.

Primeiro instanciamos as variáveis necessárias, sendo elas: um vetor do tipo `char` (onde armazenaremos a string lida) e um tipo `int` (que será nosso índice para imprimir cada `char`).

```c
    char string[1000];
```

Utilizaremos um `while()` para passar por todos os casos de teste. Dentro dele utilizaremos um `~scanf("%[^\n]%*c", string)`, que por questões de tempo essa leitura será mais rápida devido ao operador `~` (Bitwise complement) que trabalha diretamente com o valores binários, assim operando com mais desempenho.

```c
    char string[1000];
    while (~scanf("%[^\n]%*c", string))
    {
        \\código para cada caso individual
    }
```

Dentro dele iremos zerar o índice (`i`, pois a cada leitura iremos recomeçar as comparações) e em seguida utilizaremos outro `while(string[i])` para identificar o fim da frase, ou seja, quando não existir nada no `string[i]`, sairemos do `while`.

```c
    while (string[i])
        {
            \\código para comparar caractere por caractere
        }
```

Agora iremos passar caractere por caractere para identificar se existe espaço (`' '`), se o encontrar-mos verificamos se o caractere seguinte é `,` *ou* `.`, se for imprimimos o caractere seguinte ao espaco e depois incrementamos o `i`, caso nao seja `,` *ou* `.` imprimimos o espaço e seguimos; caso nao seja espaço imprimimos o caractere em analise e seguimos; ao final do `while` interno sempre incrementamos o `i`. 

```c
    if (string[i] == ' ')
        if (string[i + 1] == ',' || string[i + 1] == '.')
            putchar_unlocked(string[i + 1]), ++i;
        else
            putchar_unlocked(string[i]);
    else
        putchar_unlocked(string[i]);

    ++i;
```

Para questao de desempenho tambem, utilizaremos o `putchar_unlocked`, pois ele é não bloqueante e nao utiliza buffs, logo, agilizando a impressao.

Por fim, ao final do `while` externo devemos imprimir um `\n`.

```c
    while (~scanf("%[^\n]%*c", string))
    {
        i = 0;
        while (string[i])
        {
        \\código para comparar caractere por caractere
        }
        putchar_unlocked('\n');
    }
```


##### Para aprender um pouco mais sobre a estrutura while: [While](http://linguagemc.com.br/o-comando-while-em-c/)
##### Para aprender um pouco mais sobre operadores bitwise: [Bitwise](https://imasters.com.br/desenvolvimento/conheca-os-operadores-bitwise-bit-bit)
##### Para aprender um pouco mais sobre o putchar_unlocked: [putchar_unlocked](https://docs.oracle.com/cd/E36784_01/html/E36874/putchar-unlocked-3c.html)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
