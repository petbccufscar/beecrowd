# Problema:

Uma faixa de letras é um conjunto de letras minúsculas alfabeticamente consecutivas tomadas de 'a' até 'z'. A menor e maior letras da faixa, separadas por dois pontos (o caractere ':'), são usadas para representar a faixa de letras. Por exemplo, a faixa "a:c" representa as letras consecutivas 'a', 'b' e 'c'. (as aspas não fazem parte da faixa). A faixa "w:z" representa as letras 'w', 'x', 'y' e 'z'. A faixa "m:m" representa apenas a letra 'm'.

**Problema completo:** https://www.urionlinejudge.com.br/judge/pt/problems/view/1276


# Resolução: 
Inicialmente, na função `main` declaramos duas varíaveis `i` e `j` que serão usadas como contadores e as varíaveis `letras_espaco` e `letras`, ambas sendo do tipo char e vetores de tamanho *50*, como requerido no enunciado.
``` c
    int i, j;
	char letras_espaco[50], letras[50];
```

Logo após as declarações, temos um loop que será executado enquanto houver letras sendo lidas.
``` c
    while ( gets(letras_espaco) )
```
Dentro desse `while` temos um `for` que é executado enquanto não alcançar o número limite do vetor e a frase não estiver chegado ao final. Esse `for` tem o objetivo de retirar os espaços entre as letras.
``` c
    for (i = 0, j = 0; i < 50 && letras_espaco[i] != '\0'; i++)
```
Para os espaços serem retirados, utilizamos uma condição `if` para que, se a letra estiver entre **a** e **z**, passamos ela do vetor `letras_espaco` para o vetor `letras`.

``` c
    if (letras_espaco[i] >= 'a' && letras_espaco[i] <= 'z')
                letras[j++] = letras_espaco[i];
```
Em seguida, chamamos a função `ordena_letras` que recebe os parâmetros `letras[50]` que é o vetor de letras e `n` que é o seu tamanho e tem o intuito de ordenar as letras em ordem alfabética.
```c
void ordena_letras(char letras[50], int n)
{
    int i, j;
    char aux;

    for (j = 1; j < n; j++){
        aux = letras[j];
        for (i = j - 1; i >= 0 && aux < letras[i]; i--)
            letras[i + 1] = letras[i];
        letras[i + 1] = aux;
    }
}
```
Por fim, chamamos a função `encontra_faixa` que recebe os parâmetros `letras[50]` e `tam_vetor`. Além disso, há também os índices `inicio`, o qual servirá para demarcar o ínicio da faixa de letras, `meio` e `fim`, que irão percorrer o vetor. O laço `for` irá durar até o índice `inicio` chegar ao fim da frase e a cada iteração os valores de `meio` e `fim` irão percorrer dois a dois os elementos do vetor, até que atinjam o fim do vetor ou até que a letra apontada por `fim` não seja a seguinte na ordem alfabética daquela apontada por `meio`. Quando o laço `while` for quebrado, `inicio` continuará apontando para o começo da faixa e `meio` (ou `[fim-1]`) apontam para o último valor da faixa. Então, imprimimos esses valores e alteramos o valor de `inicio` para onde a faixa foi quebrada, ou seja, `fim`.
```c
void encontra_faixa(char letras[50], int tam_vetor)
{
    int inicio, meio, fim;

    inicio = 0;
    for (inicio = 0; inicio < tam_vetor;){
        meio = inicio;
        fim = inicio + 1;
        while (fim < tam_vetor && letras[fim] <= letras[meio]+1){
            meio++;
            fim++;
        }

        printf("%c:%c", letras[inicio], letras[fim-1]);
        inicio = fim;

        if (fim < tam_vetor)
            printf(", ");
    }
    printf("\n");
}
```

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
