# Problema:

Uma sentença é chamada de dançante se sua primeira letra for maiúscula e cada letra subsequente for o oposto da letra anterior. Espaços devem ser ignorados ao determinar o case (minúsculo/maiúsculo) de uma letra. Por exemplo, "A b Cd" é uma sentença dançante porque a primeira letra ('A') é maiúscula, a próxima letra ('b') é minúscula, a próxima letra ('C') é maiúscula, e a próxima letra ('d') é minúscula.

**Problema completo:** https://www.urionlinejudge.com.br/judge/pt/problems/view/1234

# Resoluçāo:

Neste exercício temos como entrada uma sentença, e devemos transforma-la em uma sentença dançante, isto é, uma sentença em que há uma alternação entre letras maiúsculas e minúsculas, sendo que a primeira letra desta frase deve ser maiúscula. Desta forma, para ter essa alternancia, as posições ímpares terão letras maiúsculas e as pares letras minúsculas.

Primeiramente, vamos declarar a biblioteca `string.h` pois usaremos as funções `gets` e `strlen` .

``` c
    #include <string.h>
```

Então iremos declarar a cadeia de caracteres `sentenca` que irá armezar a frase que iremos fazer as modificações, ela tem tamanho 50 pois este é o tamanho máximo que uma sentença deste exercício pode ter. A seguinte declaramos os inteiros `i` e `count` , ambas variáveis contadoras, sendo que `i` é uma variável auxiliar dentro do `for` e `count` é usado para verificar o número da posição das letras da frase, se a posição que estar é par ou ímpar. Por último temos `tam` que guardará o tamanho da sentença.

``` c
    char sentenca[50];
    int i, count;
    int tam;
```

Como não sabemos a quantidade de sentenças que serão transformadas, usamos um `while` para poder fazer as iterações e a cada uma delas usamos a função `gets` para poder armazenar a frase em `sentenca` .  Iremos exercutar o que está dentro do laço até lermos um valor nulo.

``` c
    while (gets(sentenca) != NULL)
    {
        //CÓDIGO
    }
```

Utilizando a função `strlen` para retornamos o tamanho da sentença e atribuímos a variável `tam` , já `count` recebe 1 pois definimos as posições ímpares sendo letras maiúsculas.

``` c
    tam = strlen(sentenca);
    count = 1;
```

Usamos um `for` para poder iterar caractere por caractere da sentença.

``` c
    for (i = 0; i < tam; i++)
        {
            //BLOCO
        }
```

Dentro do laço faremos as transformações da sentença. Verificamos primeiro se o caractere atual é o espaço, se for, não é preciso fazer nenhuma transformação, nem incremento em `count` pois só alteramos as letras. No segundo e terceiro condicionais fazemos as transformações de fato. 

Na segunda condição vericamos se `count` é ímpar e se o caractere é minísculo, caso ambas as opções sejam verdadeiras subtraímos 32 unidades do código [ASCII](https://www.treinaweb.com.br/blog/uma-introducao-a-ascii-e-unicode/) da string, por exemplo, o número ASCII da letra a é 97, ao subtrair 32 obtemos a letra A que tem número 65. Ao final incrementamos 1 em `count`.

A terceira condicional vericamos se `count` é par e se o caractere é maiúsculo, caso ambas as opções sejam verdadeiras somamos 32 unidades do código [ASCII](https://www.treinaweb.com.br/blog/uma-introducao-a-ascii-e-unicode/) da string. Ao final incrementamos 1 em `count`.

Por fim, se o caractere for minúsculo em posição par ou maiúsculo em posição ímpar, não modificamos a letra e adicionamos 1 em `count`.

``` c
    if (sentenca[i] == ' ')
    {
        sentenca[i] = sentenca[i];
    }
    else if (count % 2 != 0 && (sentenca[i] >= 'a' && sentenca[i] <= 'z'))
    {
        sentenca[i] -= 32;
        count++;
    }
    else if (count % 2 == 0 && (sentenca[i] >= 'A' && sentenca[i] <= 'Z')) //maiuscula em posição par
    {
        sentenca[i] += 32;
        count++;
    }
    else
    {
        sentenca[i] = sentenca[i];
        count++;
    }
```

Ao final, imprimimos a sentença dançante.

``` c
printf("%s\n", sentenca);

```

##### Para aprender um pouco mais sobre o código ASCII: [ASCII](https://www.treinaweb.com.br/blog/uma-introducao-a-ascii-e-unicode/)

 
Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/), 
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
