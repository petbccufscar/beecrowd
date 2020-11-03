# Problema:

Implemente um programa denominado combinador, que recebe duas strings e deve combiná-las, alternando as letras de cada string, começando com a primeira letra da primeira string, seguido pela primeira letra da segunda string, em seguida pela segunda letra da primeira string, e assim sucessivamente. As letras restantes da cadeia mais longa devem ser adicionadas ao fim da string resultante e retornada.

##### Link do problema: https://www.urionlinejudge.com.br/judge/pt/problems/view/1238
 
# Resolução:

O exercício consiste em ler o número de casos de teste, para cada caso de teste teremos 2 `strings` que iremos imprimir intercalando seus caracteres.

Primeiro instanciamos as variáveis necessárias, sendo elas: 6 `int` (`i` e `j` para os `loopings`; `t1` e `t2` para o tamanho das `strings`; `m` para o guardar o tamanho da maior `string`; `N` para o número de casos de teste) e 2 vetores de `char` (`n1` e `n2` para armazenar as `strings`).
Começamos lendo o número de casos de teste.

```c
    int i, j, t1, t2, m, n;
    char n1[55], n2[55];
    scanf("%d", &n);
```

Utilizaremos um `for()` para passar por todos os casos de teste.

```c
    for (i = 0; i < n; i++)
    {
        \\código para cada caso individual
    }
```

Dentro dele iremos ler as duas `strings`, utilizando o `strlen()` iremos armazenar o tamanho de ambas e em sequencia utilizaremos um `if (t1 < t2)` para encontrar qual tem o maior tamanho e armazená-lo em `m`. O `strlen()` retorna o número de caracteres da `string` passada para ele.
```c
    scanf("%s %s", &n1, &n2);
    t1 = strlen(n1);
    t2 = strlen(n2);
    if (t1 < t2)
        m = t2;
    else
        m = t1;
```

Por fim, para terminar o caso de teste individual vamos imprimir caractere por caractere de forma intercalada usando um `for()` com limite do tamanho da maior `string` (`m`), dentro dele iremos utilizar 2 `if` para saber se a determinada `string` foi completamente usada (ou seja, se `j` for menor que o tamanho dela iremos imprimir um caractere, caso contrario nao sera impresso nada). Ao finalizar esse `for()` imprimimos a quebra de linha (`printf("\n")`).

```c
    for (j = 0; j < m; j++)
        {
            if (j < t1)
                printf("%c", n1[j]);
            if (j < t2)
                printf("%c", n2[j]);
        }
        printf("\n");
```

##### Para aprender um pouco mais sobre a estrutura for: [For](http://linguagemc.com.br/a-estrutura-de-repeticao-for-em-c/)

##### Para aprender um pouco mais sobre vetores: [Vetores](http://linguagemc.com.br/vetores-ou-arrays-em-linguagem-c/)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com