# Problema:

Antes da colonização hispânica e depois inglesa, a região de San Antonio era dominada pelos índios ahmoc-axhozupeck, ancestrais dos sioux e dos apaches. A etnia foi completamente destruída pelos colonizadores, no século XVIII, tornando impossível a tarefa de decifrar seus grandes painéis.

O Departamento de Arqueologia da Universidade Baylor dedica boa parte de sua pesquisa aos painéis dos índios Ahmoc. Surpreendentemente os índios já conheciam os algarismos hindus, mas não o usavam para cálculos (afinal não existia comércio naquela civilização). Os arqueólogos de Baylor suspeitam que os painéis repletos de números fossem apenas decorativos. Também suspeitam que alguns padrões que se repetiam eram assinaturas dos artistas, a fim de garantir a autenticidade do painel.

Sua tarefa neste problema será verificar se os painéis são verdadeiros, ou seja, se, de fato, contêm a assinatura do artista que o arqueólogo suspeita ser o autor.

##### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/2049

# Resolução:

O objetivo desse exercício é criar um programa que leia dois inteiros `a` e `b`, o primeiro representando a assinatura do artista e o segundo o painel, e verificar se o primeiro pertence ao segundo, ou seja, se a assinatura do artista pertence ao painel, tonando-o legítimo. Caso o painel for legítimo, temos que printar a instância em que estamos no momento e a frase `verdadeira` e, caso contrário, ainda printamos a instância em que estamos, mas com a frase `falsa`. O programa só termina quando `a` for igual a `0`.

Para este exercício vamos usar a biblioteca `stdbool.h` que permite manipular variáveis lógicas, como verdadeiro e falso. Também iremos utilizar a biblioteca `string.h`, que permite manipular strings.

Inicialmente vamos declarar as variáveis que serão utilizadas no código. O inteiro `instancia` vai guardar a quantidade de assinaturas e painéis que estamos lendo. O booleano `i` vai guardar se o código deve continuar ou não, ele é inicialmete atribuído como `true` porque a mudança de valor depende da leitura da variável `a`. As variáveis `a` e `b` vão guardar os valores da assinatura do autor e o painel, respectivamente. Declaramos ambas como `char` para facilitar a verificação se uma string inclui outra.

```c
int instancia=1;
bool i=true;
char a[10], b[300001];
```

O código inicia com o `while` que continuará em loop enquanto `i=true`. Dentro desse loop iremos realizar todas as verificações necessárias, começando com a leitura do valor `a`. O restante do código depende desse valor lido e por isso, logo em seguida, vamos utilizar um `if` e `else`. A função `strcmp` é usada para comparar se o valor `a` lido é igual a `0` e retorna `0` caso as strings forem iguais. Finalmente comparamos a resposta da função `strcmp`, caso essa resposta for diferente de `0` indica que o programa continua normalmente, caso contrário indica que o programa deve ser finalizado. Se esse último caso for verdadeiro, atribuímos `false` para a variável `i`, fazendo com que na próxima iteração do `while` o loop termine e o pograma seja finalizado.

```c
while(i){		
    scanf("%s", a);

    if(strcmp(a, "0") != 0){
        /* Continuação omitida */
    } else{
        i=false;
    }
}
return 0;
```

O exercício diz que uma linha em branco deve separar a saída de cada instância. Neste caso, se o valor de `a` for diferente de `0`, inicialmente temos que printar uma linha em branco. Essa linha vai aparecer somente quando não for a instância 1 e, por isso, utilizamos um `if` para fazer essa verificação. Posteriormente realizamos a leitura do painel, ou seja, da variável `b`. Nesse momento começamos a printar os resultados, como em ambas as possibilidades precisamos printar a instância em que estamos, fazemos isso nesse momento, utilizando a variável `instancia`e já atualizamos ela com `instancia + 1` para a próxima iteração. Com as variáveis `a` e `b` lidas, usamos a função `contem_assinatura` para verificar se `b` contém a assinatura `a`. Se sim iremos printar `verdadeira` e, caso não, printamos `falsa`.

```c
while(i){		
    scanf("%s", a);

    if(strcmp(a, "0") != 0){
        if(instancia != 1)
			printf("\n");

        scanf("%s", b);
        printf("Instancia %d\n", instancia++);
        if(contem_assinatura(a, b)){
            printf("verdadeira\n");
        }
        else
            printf("falsa\n");
    } else{
        i=false;
    }
}
return 0;
```

Como comentado acima, utilizamos a função `contem_assinatura` para verificar se o painel contém a assinatura do artista, ou seja, se `b` contém `a`. Nessa função, recebemos como parâmetros duas strings `a` e `b` e usamos a função `strstr`para verificar se `b` contém `a`. Se sim, retornamos `1` e, caso contrário, retornamos `0`.

```c
int contem_assinatura(char *a, char *b){
    if(strstr(b, a))
        return 1;
    return 0;
}
```

##### Para aprender um pouco mais sobre a biblioteca string.h: [<String.h>](http://linguagemc.com.br/a-biblioteca-string-h/)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
