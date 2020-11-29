#include <stdio.h>
#include <stdlib.h> 
#include <string.h>

struct item { 
    char nome[100]; 
    struct item *prox; 
}; 

int temItem(struct item *cabeca, char nomeItem[])
{
    while (cabeca != NULL )
    { 
        if(strcmp(cabeca->nome, nomeItem) == 0)
            return 1;
        cabeca = cabeca->prox; 
    }
    return 0;
}

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


void imprime(struct item *cabeca)
{
    cabeca = cabeca->prox;
    while (cabeca != NULL )
    { 
        printf("%s\n", cabeca->nome); 
        cabeca = cabeca->prox; 
    } 
}

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

int main(int argc, char **argv)
{
    struct item* cabeca ;
    cabeca = (struct item*)malloc(sizeof(struct item)); 
    strcpy(cabeca->nome, "inicio");
    
    int numeroCasosTeste;
    int numeroUtilizacoes;
    char itemLido[100], acao[10]; 

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

    return 0;

}
