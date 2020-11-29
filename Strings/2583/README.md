# Problema:
O Grande herói Chapolout vai ajudar um inventor, e lá encontra com o genro dele, que tinha más intenções. Para tentá-lo fazer mudar de ideia, Chapolout conta a estória de Tausfo e Mefistótriste. Tausfo era um senhor com idade bem avançada, e era apaixonado por uma mulher bem mais jovem que ele. Um dia, ele recebe a visita de Mefistótriste, um demônio que lhe oferece uma ferramenta, chamada Chirrin Chirrion, que trazia ou afastava coisas conforme era dito. Para trazer algo, precisava dizer o que queria, seguido da palavra Chirrin, e para afastar algo, precisava dizer o que não queria, seguido da palavra Chirrion. Qualquer outra palavra dita, não iria fazer efeito. Depois de tanto usar, Mefistótriste volta e diz que irá levar a sua alma consigo, a menos que devolvesse tudo o que havia pedido. Ajude Tausfo!

Escreva um programa que, - dadas as utilizações da ferramenta -, reúna tudo o que Tausfo adquiriu com o Chirrin Chirrion.

Entrada
O primeiro valor a ser lido é um inteiro C, indicando o número de casos de teste. Cada caso de teste inicia com um inteiro N, informando quantas utilizações foram feitas. Considere que antes ele não possuía nada, que um Chirrion só terá efeito se ele possuir tal coisa dita, e que um Chirrin só terá efeito se ele ainda não possuir tal coisa, ou seja, não tem como ele possuir dois exemplares de uma mesma coisa.

Saída
Para cada caso de teste, imprima a palavra TOTAL, seguida da relação de coisas que Tausfo tem, em ordem alfabética.
 
##### Link do problema: https://www.urionlinejudge.com.br/judge/pt/problems/view/2583
 
 
# Resolução:

O problema consiste em exibir as coisas que Tausfo tem, em ordem alfabética, ao fim de todas as suas ordens. Para isso, vamos utilizar uma lista encadeada com nó cabeça.

Uma lista encadeada com nó cabeça é uma estrutura de dados em que cada elemento, além dos dados que armazena, também possui um ponteiro de nó, onde se armazena o endereço do próximo nó, além de ter um nó struct inicial (`cabeça`). Note que o ponteiro do próximo nó, do último elemento da lista, aponta para `NULL`, justamente para indicar o término da lista. Utilizando estes ponteiros, é possivel manipular a lista.

Para a resolução do problema, iremos importar a biblioteca `string.h`, para utilizarmos a função `strcmp()` e `strcpy()`, e a biblioteca `stdlib.h`, para utilizarmos a função `malloc()`. Logo após isso, declaramos o struct item, que irá compor nossa lista.

```c
struct item { 
    char nome[100]; 
    struct item *prox; 
}; 
```

Em seguida, como tanto para adicionar um novo item a lista, caso a ordem de Tausfo seja chirrin, quanto para remover um item, se a ordem de Tausfo seja chirrion, precisamos de uma função para nos informar se há o item ou não na lista. Isto por quê, caso seja chirrin, se ele já tiver o item, nada será feito, pois ele só guarda um por vez. De maneira análoga, caso seja chirrion, não é possivel remover um item que ele não tem, então nada será feito.

Para isso, utilizaremos a função `temItem()`, que recebe como parâmetros o início de nossa lista, `struct item cabeca,` e o item a ser buscado, `nomeItem`:
- Utilizamos um laço de repetição `while(cabeca != NULL)` para percorrer a lista inteira;
- A cada elemento lido, verificamos com `strcmp()` se o item do elemento da lista atual (`cabeca->nome`) é igual ao que estamos procurando
    - caso seja, retorna-se 1;
    - caso contrário, avança-se para o próximo elemento da lista, utilizando `cabeca = cabeca->prox;` ;
- Se a lista inteira for percorrida e o item não foi achado, retorna-se 0.

```c
int temItem(struct item *cabeca, char nomeItem[])
{
    while (cabeca != NULL)
    { 
        if(strcmp(cabeca->nome, nomeItem) == 0)
            return 1;
        cabeca = cabeca->prox; 
    }
    return 0;
}
```

Para adicionar um item a nossa lista, utilizamos a função `adiciona()`, que recebe como parâmetros um ponteiro para o início de nossa lista, `struct item cabeca`, já que iremos modificá-la, e o item a ser adicionado, `nomeItem`. Como não precisamos adicionar um item em um local específico da lista, iremos adicioná-lo no final, como um apendice:
- Alocamos a memória necessária do item a ser adicionado, utilizando `malloc()`;
- Copiamos os dados do item a ser adicionado, para o elemento da lista (em nosso caso é o nome do item somente), utilizando `strcpy()`, pois é uma string; 
- Atribuimos `NULL` ao ponteiro que indica o endereço do próximo elemento da lista, para indicar o final desta, pois o elemento será adicionado no final;
- Criamos um elemento auxiliar (`struct item *aux`), que recebe o início da lista (`*cabeca`);
- Percorremos a lista até o fim, utilizando um laço de repetição `while(aux->prox != NULL)` que a cada iteração avança um elemento, por meio de 
`aux = aux->prox)`
- Atribuímos ao endereço do elemento posterior ao antigo último elemento, que antes era `NULL`, nosso novo item, por meio de `aux->prox = novoItem`.

```c
void adiciona(struct item** cabeca, char nomeItem[])
{
    struct item *novoItem = (struct item*)malloc(sizeof(struct item));
 
    strcpy(novoItem->nome, nomeItem);
    novoItem->prox = NULL;
  
    struct item *aux = *cabeca;
    while (aux->prox != NULL)
        aux = aux->prox;
    
    aux->prox = novoItem;

}
```

Agora, para remover um item X da nossa lista, precisamos fazer o elemento que apontava para X, apontar para o elemento posterior a X. O exemplo a seguir ilustra isto:
- Antes da remoção do elemento 2:
    `cabeca -> 1 -> 2 -> 3 -> NULL`
- Após a remoção :
    `cabeca -> 1 -> 3 -> NULL`

Para isso, utilizamos a função `remover()`, que também recebe como parâmetros um ponteiro para o início de nossa lista, `struct item cabeca`, já que iremos modificá-la, e o item a ser removido, `nomeItem`:
- Declaramos dois elementos, `*aux = *cabeca`, que será excluído, e  `*anterior = NULL`, que será o elemento anterior a `aux`;
- Percorremos a lista até o elemento cujo `nome` seja igual a `nomeItem`, no caso, o item a ser excluído, por meio de uma estrutura de repetição `while()` em que a cada iteração, `anterior = aux` e `aux = aux->prox`;
- Atribuímos ao ponteiro `prox` do elemento predecessor ao elemento que irá ser excluído, o endereço do elemento posterior ao que será excluído, por meio de `anterior->prox = aux->prox`;
- Desalocamos o espaço de memória do elemento excluído, utilizando `free(aux)`.

Note que nossa função de remoção não verifica se chega ao fim da lista sem encontrar o elemento desejado, pois, por conta da verificação com `temItem()` que iremos fazer antes de usá-la, o elemento necessariamente está presente na lista.

```c
void remover(struct item** cabeca, char nomeItem[])
{
    struct item *aux = *cabeca;
    struct item *anterior = NULL;

    while (!(strcmp(aux->nome, nomeItem) == 0) )
    {
        anterior = aux;
        aux = aux->prox;
    }
    anterior->prox = aux->prox;
    free(aux);

}
```

Em seguida, criamos nossa função de exibição `imprime()`, que lê todos os elementos da lista, com exceção do cabeça, exibindo o nome de cada item.

```c
void imprime(struct item *cabeca)
{
    cabeca = cabeca->prox;// pulando o no inicial
    while (cabeca != NULL )
    { 
        printf("%s\n", cabeca->nome); 
        cabeca = cabeca->prox; 
    } 
}
```

Para terminar nossas funções auxiliares, iremos implementar um bubblesort, responsável pela ordenação de nossa lista. Vale ressaltar que nosso algoritmo não troca os elementos de lugar, mas sim o conteúdo (nome) dos itens, por meio da função `troca()`, e que ele ignora o primeiro item da lista, pois é nosso nó cabeça, realizando `cabeca = cabeca->prox`.
Fora estas duas especifidades, nosso algoritmo é igual aos dos livros: percorre a lista do início ao fim, verificando elementos dois a dois e trocando-os, caso necessário, dessa forma, "flutuando" o maior elemento ao fim da lista. O algoritmo para até que nenhuma troca tenha sido realizada na passagem anterior, indicando que a lista está ordenada.

```c
void troca(struct item *a, struct item *b)
{ 
    char aux[100]; 
    strcpy(aux, a->nome);
    strcpy(a->nome, b->nome);
    strcpy(b->nome, aux);
} 

void bubbleSort(struct item *cabeca) 
{ 
    cabeca = cabeca->prox; 
    int trocou, i; 
    struct item *aux1; 
    struct item *aux2 = NULL; 
  
    do
    { 
        trocou = 0; 
        aux1 = cabeca; 
        while (aux1->prox != aux2)
        {
            if ( strcmp(aux1->nome, aux1->prox->nome) > 0)
            {
                troca(aux1, aux1->prox); 
                trocou = 1; 
            } 
            aux1 = aux1->prox; 
        } 
        aux2 = aux1; 
    } 
    while (trocou); 

} 
```


**Com as preparações para utilizarmos a nossa estrutura de lista feitas, mudamos nosso escopo para a função main() agora.** Iremos declarar o nó cabeça de nossa lista, `struct item* cabeca`, e alocar a memória necessária para este, utilizando `malloc()`. Em seguida, de forma ilustrativa, para indicar que é o início de nossa lista, atribuímos "inicio" ao atributo `nome` de nosso item `cabeca`. Além disso, declaramos dois inteiros `numeroCasosTeste`, `numeroUtilizacoes` e dois vetores de caracteres `itemLido[100]`, que indica o item cuja ação irá agir, e `acao[10]`, que indica a ação sobreo item ( chirrin ou chirrion).

```c
struct item* cabeca ;
cabeca = (struct item*)malloc(sizeof(struct item)); 
strcpy(cabeca->nome, "inicio");
    
int numeroCasosTeste;
int numeroUtilizacoes;
char itemLido[100], acao[10]; 
```

Depois, lemos a quantidade de casos de teste `numeroCasosTeste` e utilizaremos uma estrutura de repetição `while` que irá iterar `numeroCasosTeste` vezes.
A cada iteração do laço de repetição:
- Iniciamos nossa lista somente com o nó cabeça `cabeca->prox = NULL`;
- lemos o número de utilizações de tausfo `numeroUtilizacoes`;
- utilizaremos uma estrutura de repetição `while` que irá iterar `numeroUtilizacoes` vezes, em que a cada iteração:
    - lemos o item e a ação em questão `scanf("%s %s", itemLido, acao)`;
    - se a ação for chirrin:
        - verificamos se há o item na lista com a função `temItem()` e, se não tiver, adicionamos-o por meio da função `adiciona()`;
    - se a ação for chirrion:
        - verificamos se há o item na lista com a função `temItem()` e, se tiver, removemos-o por meio da função `remover()`;
- ordenamos nossa lista, com exceção do elemento cabeça, utilizando `bubbleSort()`;
- exibimos "TOTAL", por meio da função `printf("TOTAL\n")`;
- exibimos nossa lista, por meio da função `imprime(cabeca)`.


```c
scanf("%d", &numeroCasosTeste);
    while (numeroCasosTeste--)
    {
        cabeca->prox = NULL;
        scanf("%d", &numeroUtilizacoes);
        while (numeroUtilizacoes--)
        {
            scanf("%s %s", itemLido, acao);
            
            if (strcmp(acao, "chirrin") == 0)
            {
                if (!temItem( cabeca, itemLido))
                    adiciona( &cabeca, itemLido);
            }
            else if (strcmp(acao, "chirrion") == 0)
            {
                if (temItem( cabeca, itemLido))
                    remover( &cabeca, itemLido);
            }
            
        }
        bubbleSort(cabeca);
        printf("TOTAL\n");
        imprime(cabeca);
    }
```


##### Mais sobre alocação dinâmica: [alocação dinâmica](https://www.ime.usp.br/~pf/algoritmos/aulas/aloca.html)
##### Mais sobre lista encadeada: [lista encadeada](https://www.ime.usp.br/~pf/algoritmos/aulas/lista.html)



Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
