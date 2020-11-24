# Problema:

Seu irmão mais novo aprendeu a escrever apenas um, dois e três, em Inglês. Ele escreveu muitas dessas palavras em um papel e a sua tarefa é reconhecê-las. Nota-se que o seu irmão mais novo é apenas uma criança, então ele pode fazer pequenos erros: para cada palavra, pode haver, no máximo, uma letra errada. O comprimento de palavra é sempre correto. É garantido que cada palavra que ele escreveu é em letras minúsculas, e cada palavra que ele escreveu tem uma interpretação única.

**Problema Completo**: https://www.urionlinejudge.com.br/judge/pt/problems/view/1332

# Resolução:

Para a resolução deste problema, além da biblioteca padrão `stdio.h`, é necessário incluir a biblioteca `string.h`.

```c
#include <stdio.h>
#include <string.h>
```

Após informar as bibliotecas, iniciamos o nosso algoritmo. Primeiramente, declaramos uma variável do tipo inteiro chamada `CasoTeste` e em seguida fazemos a leitura desta variável com o comando `scanf()`, esse será o nosso número de casos testes no problema em questão. Em seguida, entramos na parte lógica do nosso código, que está explicada logo abaixo.

```c
int main ()
{
    int CasoTeste; scanf("%d", &CasoTeste);

	/**
     * restante do código aqui (informado abaixo)
    **/

    return 0;
}
```

É necessário fazer uma estrutura `while()` para cada caso teste. Após, declaramos uma variável do tipo caractere chamada `a[10]` e em seguida fazemos a leitura da palavra escrita, armazenando-a nesta variável com o comando `scanf()`.

```c
while ( CasoTeste-- )
{
    char a[10]; scanf("%s", a);

	/**
     * restante do código aqui (informado abaixo)
     * parte lógica do problema
    **/

}
```

Aqui, temos uma estrutura `if` e `else` que transforma as palavras: 'one', 'two' ou 'three', em seus respectivos números: '1', '2' ou '3'.

Com o `if`, se a palavra tiver 5 letras, é mostrado o número 3 com o comando `printf()`, pois, no caso 'três' em inglês é 'three' e contém 5 letras.

Os outros casos possiveis, são 'um' ou 'dois', que em inglês são respectivamente, 'one' ou 'two', ambos com três letras, ou seja, com o `else`, caso a palavra não tenha 5 letras (não seja o número 3) uma nova estrutura de decisão é feita para decidir se é o número 1 ou o número 2.

Dentro dessa estrutura else, temos uma nova estrutura `if` e `else`, é analisado que se a variável do tipo caractere `a[10]` recebe a palavra 'one' através da variável do tipo inteiro recém definida chamada `cnt`, e em caso afirmativo, é mostrado o número 1 com o comando `printf()`. E no caso contrário, ou seja, se `a[10]` não receber a palavra 'one', com o `else` é mostrado o número 2 com o comando `printf()`.

```c
if ( strlen(a) == 5 ) printf("3\n");
else
{
    int cnt = 0;

    if ( a[0] == 'o' ) cnt++;
    if ( a[1] == 'n' ) cnt++;
    if ( a[2] == 'e' ) cnt++;

    if ( cnt >= 2 ) printf("1\n");
    else printf("2\n");
}
```

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/),
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
