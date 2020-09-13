# Problema:

Armandinho tem um amigo o tanto quanto chato, chamado Laércio. Quando jogam o jogo do mestre manda, um jogo onde alguém dá uma ordem e alguém a cumpre, e em vez de dar ordens legais como subir em uma árvore, pular o muro, plantar bananeira ou organizar manifestações para derrubar o governo (independente de quem estiver no poder) ele sempre pede algo maçante. Em sua última partido, Laércio exigiu que Armandinho ordenasse uma lista de números, de forma que apenas os números ímpares aparecessem e o primeiro item seja o maior, o segundo seja o menor, o terceiro o segundo maior, o quarto seja o segundo menor e assim por diante. Como fazer isso a mão é muito chato, Armandinho procurou sua ajuda.

**Problema completo:** https://www.urionlinejudge.com.br/judge/pt/problems/view/2812

# Resoluçāo:

A ideia deste exercício é a partir do vetor do caso de teste, colocar apenas os números ímpares dele em outro vetor, então ordenar o vetor de ímpares. Após o ordenação em ordem decrescente, declaramos 2 variáveis uma que está ao início deste vetor, tendo valor de zero, esta aponta para o maior elemento; a outra que está no último elemento(que tem menor valor), é designada com o tamanho deste vetor menos 1(para poder acessar o elemento). Então em um vetor resultado, colocamos na primeira posição o elemento de maior valor e na segunda posição o elemento de menor valor, aumentamos a variável que está na primeira posição em uma unidade e a variável do último elemento diminuímos em uma unidade, até completar todos os elementos.

Primeiramente, vamos declarar a biblioteca `string.h` pois usaremos a função `memset` a fim de deixar todos os elementos iguais a zero.

```c
    #include <string.h>
```

Então iremos declarar as variáveis inteiras `i`, `j`, `a` que serão usadas como auxiliares para fazer iterações em laços. O inteiro `n` guarda a quantidade de casos de testes e `tam` representa o tamanho do vetor daquele caso de teste. Por último, `indice` é uma variável que serve de índice para o vetor de ímpares e `elem` é auxiliar para ser lido e caso seja impar entrará dentro do vetor de ímpares.
```c
    int i, j, a;
    int n, tam;
    int indice = 0, elem;
```

Guardamos o valor de `n`, `tam` e declaramos o vetor de inteiros `v` que tem tamanho de `tam`. A partir disto, usamos um `for` para poder ler os valores de entrada do vetor, mas antes de inserir ele dentro de `v`, verificamos por meio de um `if` para verificar se o valor de `elem` é ímpar, caso afirmativo adicionamos o valor a `v` e acrescentamos `indice` em uma unidade.

```c
    scanf("%d", &n);

    for (a = 0; a < n; a++)
    {

        scanf("%d", &tam);
        int v[tam];

        for (i = 0; i < tam; i++)
        {
            scanf("%d", &elem);
            if (elem % 2 == 1)
            {
                v[indice] = elem;
                indice++;
            }
        }
```

Se `indice` for maior que 0, isto significa que existe ao menos um número ímpar dentro de `v`, se esta condição for verdadeira, faremos a ordenação do vetor utilizando o método bubble sort.

```c
    if (indice > 0)
    {
        int aux;
        for (i = 0; i < indice; i++)
        {
            for (j = i + 1; j < indice; j++)
            {
                if (v[i] < v[j])
                {
                    aux = v[i];
                    v[i] = v[j];
                    v[j] = aux;
                }
            }
        }
```

Declaramos as variáveis `maior`, `menor` e um vetor `resultado` com o tamanho de `indice`. Tanto `maior` quanto `menor` são utilizadas para marcar índice de `v`, sendo que `maior` marca o inicio, que possui os elementos de tamanho maior e `menor` marca o final, que possui os elementos de tamanho menor.

Designamos `i` a 0, pois ele servirá como índice do vetor `resultado`. Dentro do `while` acontecerá a organização dos elementos de `v` de maneira que terá o maior elemento seguido do menor, o segundo maior seguido do segundo menor e por diante. A organização dos elementos consiste da seguinte maneira, colocamos `v[maior]` na primeiro em `resultado` e `v[menor]` uma posição a frente de `v[maior]` no vetor `resultado`, aumentamos `i` em 2 unidades e incrementamos `maior` em 1 e decrementamos `menor` em 1.

Este laço é repetido enquanto `maior` for menor ou igual que a metade de `indice`, assim isso evita que os índices `maior` e `menor` não ultrapassem entre si.


```c
    int maior = 0, menor = indice - 1;
    int resultado[indice];
    i = 0;

    while (maior <= (indice / 2))
    {
        resultado[i] = v[maior];
        resultado[i + 1] = v[menor];
        i += 2;
        maior++;
        menor--;
    }
```

Imprimimos o vetor `resultado`, de modo que no final do último elemento tenha uma quebra de linha.

```c
for (i = 0; i < indice; i++)
{
    if (i == indice - 1)
        printf("%d\n", resultado[indice - 1]);
    else
        printf("%d ", resultado[i]);
}
```

Ao final, atribuímos `ìndice` a 0 e usamos a função `memset` para deixar todos os elementos de `v` e `resultado` com o valor de 0.

```c
indice = 0;
memset(v, 0, sizeof(v));
memset(resultado, 0, sizeof(resultado));

```
Caso `indice` for 0, apenas imprimimos uma quebra de linha, devido ao fato de não ter nenhum valor ímpar no vetor de entrada.
```c
else
    printf("\n");
```

##### Para aprender um pouco mais sobre a biblioteca string.h: [string.h](http://linguagemc.com.br/a-biblioteca-string-h/)
 
Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
