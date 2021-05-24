# Problema:

Leia 3 valores inteiros e ordene-os em ordem crescente. No final, mostre os valores em ordem crescente, uma linha em branco e em seguida, os valores na sequência como foram lidos.

**Problema completo:** https://www.urionlinejudge.com.br/judge/pt/problems/view/1042

# Resolução:

O primeiro passo para resolver o exercício é definir como os números serão ordenados. Utilizaremos um algoritmo de ordenação chamado BubbleSort, que consiste em percorrer um vetor verificando se o elemento seguinte está fora de ordem com o elemento atual. Ou seja, se o elemento n é maior que o elemento n+1, estes não estão em ordem crescente e devem ser trocados de posição. Essa verificação é feita n-1 vezes para garantir que o vetor está em ordem, mas pode ser otimizada em exercícios futuros.

Como sabemos que o exercício fornecerá apenas 3 números, a função `bubbleSort(int *vetor)` precisa apenas receber o vetor que deve ser ordenado, através de um ponteiro. Não é necessário passar o número de elementos do vetor.

Agora, devemos ler o vetor e ordená-lo com a função pronta. O exercício pede que os números sejam exibidos ordenados e, depois, na ordem que foram lidos. Para isso, utilizaremos dois vetores: o original e uma cópia do original, que será ordenado.  
Durante a leitura do vetor original, aproveitaremos para copiar cada posição para o vetor que será ordenado:

```c
for(i = 0; i < 3; i++) {
    scanf("%d", &vetorOriginal[i]);
    vetorOrdenado[i] = vetorOriginal[i];
}
```
Ordenamos o vetor com a função `bubbleSort`:

```c
bubbleSort(vetorOrdenado);
```

Exibimos o vetor ordenado, pulamos uma linha e exibimos o vetor original:

```c
for(i = 0; i < 3; i++)
    printf("%d\n", vetorOrdenado[i]);

printf("\n");

for(i = 0; i < 3; i++)
    printf("%d\n", vetorOriginal[i]);
```

###### Nota: ao usar uma diretiva (for, while, if) que só tem uma linha dentro, não precisamos colocar chaves {}

##### Para aprender mais sobre [Bubble Sort](http://devfuria.com.br/logica-de-programacao/exemplos-na-linguagem-c-do-algoritmo-bubble-sort/)

##### Para aprender mais sobre [ponteiros em C](http://linguagemc.com.br/ponteiros-em-c/)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso [Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com