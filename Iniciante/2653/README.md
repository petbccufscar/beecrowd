# Problema:
No jogo O Bruxo, Sigismund Dijkstra é o líder do Serviço Secreto Redaniano, por causa disso ele é uma das pessoas mais importantes do mundo.

Além disso Dijkstra possui um grande tesouro, o qual possui diversos tipos de jóias.

Dijkstra está muito curioso para saber quantos tipos de jóias diferentes seu tesouro possui.

Sabendo que você é o melhor programador do continente Dijkstra te contratou para verificar quantos tipos de jóias distintas ele tem em seu tesouro.
 
##### Link do problema: https://www.urionlinejudge.com.br/judge/pt/problems/view/2653
 
 
# Resolução:
 
Para a resolução do problema, iremos importar a biblioteca `string.h`, para utilizarmos a função `strcmp()` e `strcpy()`, e a biblioteca `stdlib.h`, para utilizarmos a função `malloc()`. 

Além disso, iremos utilizar o conceito de árvore binária para armazenarmos cada joia. Cada nó da árvore (`no`) será composto por um vetor de caracteres de tamanho "1000000", que representa a joia, e dois ponteiros de `no`, o da esquerda, que aponta para uma joia de string menor (caso aponte para algo) e o da direita, que aponta para uma joia de string maior (caso aponte para algo). 

Para isso, iremos declarar nosso tipo `no`, de forma global, utilizando `typedef struct`.

```c
typedef struct no{
    char joia[1000000];
    struct no *esq;
    struct no *dir;

} no;
```

Também iremos declarar de forma global a variável do tipo inteiro `numJoias` e atribuí-la o valor 0. Esta variável representa o número de tipos de joias lidos.

```c
int numJoias = 0;
```

Em seguida, ainda de forma global, iremos construir a nossa função `adiciona` que irá adicionar nós na árvore. Nossa função terá como parâmetros um ponteiro para um nó e uma string, que representa a joia atual. Com isso, teremos 3 ocorrências:

Caso o nó recebido seja NULL, ou seja, o nó em questão ainda não existe e aquele tipo de joia não foi lido anteriormente, iremos inicializá-lo da seguinte forma :
- alocamos o espaço de memória necessária de um nó, utilizando `malloc()`;
- atribuímos `NULL` aos ponteiros `esq` e `dir` deste nó, já que estes não apontam para nenhum outro nó ainda;
- atribuímos a `joia` a string passada como parâmetro pela nossa função `adiciona`;
- adicionamos 1 ao nosso contador de tipos de joia (`numJoias`).

```c
if (!ramo){
    ramo = (no * ) malloc(sizeof(no));
    ramo->esq = ramo->dir = NULL;
    strcpy(ramo->joia, p);
    numJoias++;

}
```

Caso o nó recebido não seja NULL, o nó em questão já foi inicializado, então só precisamos decidir se iremos para o nó a esquerda ou para o nó a direita. Decidiremos isso com base no tamanho da string recebida.
- Se for menor que o nó em que estamos, iremos para o nó da esquerda.

```c
else if (strcmp(ramo->joia, p) > 0)
        ramo->esq = adiciona(ramo->esq, p);
```

- Se for maior que o nó em que estamos, iremos para o nó da direita.

```c
else if (strcmp(ramo->joia, p) < 0)
        ramo->dir = adiciona(ramo->dir, p);
```

Ao fim da função, retornarmos a árvore, para que possamos construí-la e armazenar a alteração realizada a cada chamada da função. Vale ressaltar que caso a `joia` do nó seja igual a `joia` recebida pela função, o retorno da função `strcmp()` será "0", então nada irá acontecer.

```c
return ramo;
```

**Com as preparações para utilizarmos a nossa estrutura de árvore feitas, mudamos nosso escopo para a função main() agora.** Iremos declarar um vetor de caracteres de tamanho 1000000 (`novaJoia`), para lermos a string fornecida e o nó raiz da nossa árvore, inicializado com NULL.

```c
char novaJoia[1000000];
no *arvore = NULL;
```

Em seguida, utilizaremos uma estrutura de repetição `while` que irá iterar enquanto houver entrada. A cada iteração do laço de repetição lemos a joia fornecida e a adicionamos na árvore. A árvore é atualizada a cada chamada de função, por isso utilizamos `arvore = adiciona(arvore, novaJoia)`

```c
while (scanf("%s", joia) != EOF)
    arvore = adiciona(arvore, novaJoia);
```

Em seguida, exibimos o número de joias diferentes pesquisadas.

```c
printf("%d\n", numJoias);
```

##### Mais sobre alocação dinâmica: [alocação dinâmica](https://www.ime.usp.br/~pf/algoritmos/aulas/aloca.html)
##### Mais sobre árvore binária: [árvore binária](https://pt.wikibooks.org/wiki/Programar_em_C/Árvores_binárias)



Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
