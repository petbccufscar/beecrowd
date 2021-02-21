# Problema:

Uma sequência de letras é escrita em um anel milagroso. Quando a sequência é lida em voz alta a partir de qualquer letra, a mágica acontece. Para obter a maior magia, você precisa da palavra mais poderosa: você quer encontrar um lugar para começar a ler, de modo que a palavra que você recebe seja a maior palavra possível na ordem alfabética.

**Problema Completo**: https://www.urionlinejudge.com.br/judge/pt/problems/view/2975

# Resolução:

Para a resolução deste problema, além da biblioteca padrão `stdio.h` (biblioteca para o scanf), é necessário incluir a biblioteca `string.h` (biblioteca para o strlen). Definimos uma constante para o máximo número de caracteres, e fazemos uma definição de macro para achar o mínimo entre dois elementos.

```c
#include <stdio.h>
#include <string.h>

#define MAX 100010

#define min(a, b) (a < b ? a : b)
```

Abaixo, o temos algoritmo LPS (longest palindromic subsequence) para retornar o comprimento da subsequência palíndrômica mais longa em sequência.

Com len = 0 temos o comprimento atual, e o vetor lps na posição zero é zero por definição.

Em seguida, temos um loop para calcular o lps:

Se pat[i] == pat[len] incremento o comprimento e seto o lps[i];

Se for diferente de zero, então volto para o lps anterior;

Se o comprimento for zero, não há o que fazer e o lps atual é nulo.

```c
void computeLPSArray(char* pat, int M, int* lps) { 
    
    int len = 0; 
  
    lps[0] = 0;
  
    int i = 1; 
    while (i < M) { 
        if (pat[i] == pat[len]) { 
            len++; 
            lps[i] = len; 
            i++; 
        } 
        else {  
            if (len != 0) {
                len = lps[len - 1]; 
            } 
            else {
             
                lps[i] = 0; 
                i++; 
            } 
        } 
    } 
} 
```

Abaixo, temos o algoritmo KMP pra encontrar todas ocorrências de uma string em outra em tempo linear.

O algoritmo de Knuth–Morris–Pratt procura a ocorrência de uma "palavra" W dentro de um "texto" S empregando a simples técnica de que quando aparece uma diferença, a palavra tem em si a informação necessária para determinar onde começar a próxima comparação.

Segue a explicação do algoritmo, no qual inicialmente definimos os seguintes valores do tipo inteiro:

int ret = 0; quantidade de ocorrências / int M = strlen(pat); tamanho da string a ser pesquisada / int N = strlen(txt); tamanho da string local de pesquisa / int lps[M]; vetor lps da string padrão / int i = 0; E int j = 0; são contadores

E em seguida, após as definições tipo inteiro, temos o loop do KMP, que está explicado abaixo.

Temos o while (i < N-1) onde usamos -1 pois a string está duplicada devido ao ciclo.

Se for igual incremento os dois índices.

Se j for o tamanho da string padrão, ocorrência encontrada.

Com o j = lps[j - 1] vai para o índice maior prefixo que também é um sufixo, pois é invariante a pesquisa.

Caso tenha dado errado, temos o else if, no qual:

Usamos o if (j != 0) para e o índice j for diferente de 0, tento o lps[j-1].

Do contrário (caso else) apenas soma-se o texto, pois nesse índice já é impossível.

E com return ret temos o retorno do valor.

Sendo assim, o algoritmo do KPM como um todo fica da seguinte forma:

```c
int KMPSearch(char* pat, char* txt) { 
    int ret = 0;
    int M = strlen(pat);
    int N = strlen(txt);
  

    int lps[M];
    computeLPSArray(pat, M, lps); 
  
    int i = 0;
    int j = 0;


    while (i < N-1) {
        if (pat[j] == txt[i]) {
            j++; 
            i++; 
        } 
  
        if (j == M) {
            ret++; 
            j = lps[j - 1];
        } 
  
        else if (i < N && pat[j] != txt[i]) { 
            if (j != 0)
                j = lps[j - 1]; 
            else
                i = i + 1;
        } 
    } 
    return ret;
} 
```

Por fim, temos o main, com o algoritmo principal, explicado em detalhes abaixo.

Temos, inicialmente, as seguintes definições:

char str[2*MAX] para a definição da string.

scanf("%s", str) para a leitura da string.

int i, j, k, len = strlen(str) que são os contadores e o comprimento da string.

Para a máxima rotação lexicográfica da string, definimos os contadores como: i = 0, j = 1, k = 0.

E definimos uma estrutura while da seguinte maneira: while (k < len && i < len && j < len), enquanto os índices forem menores que o tamanho.

E os inteiros: int idx1 = (i+k)%len, idx2 = (j+k)%len; que é o modulo, pois é o anel e portanto a string é cíclica.

E em seguida, temos uma estrutura if e else:

Na estrutura if, se: if (str[idx1] == str[idx2]) for igual, aumenta o k (offset de comparação).

Na estrutura else, se: if (str[idx1] < str[idx2]) for menor, pulo o índice i.

Ainda na estrutura else, do contrário pulo o índice.

E com um novo if verifica-se: if (i == j) caso ambos índices forem iguais, então aumento i.

E com o k = 0 reseto o offset.

Após, temos o int maxIdx = min(i, j) para o mínimo entre os índices comparadores.

Com char pat[MAX] temos a construção da string padrão para o KMP.

Com o for fazemos a duplicação da string texto, pois pode haver match em situações cíclicas.

E utilizamos o printf("%d %d\n", KMPSearch(pat, str), maxIdx+1) para escrever a resposta.

Sendo assim, temos o algoritmo final da seguinte forma:

```c
int main(int argc, char **argv) {
    char str[2*MAX];
    scanf("%s", str);
    int i, j, k, len = strlen(str);

    i = 0, j = 1, k = 0;
    while (k < len && i < len && j < len) {
            int idx1 = (i+k)%len, idx2 = (j+k)%len;
            if (str[idx1] == str[idx2]) {
                k++;
            } else {
                if (str[idx1] < str[idx2]) {
                    i = i + k + 1;
                } else {
                    j = j + k + 1;
                }
                if (i == j) {
                    i++;
                }
                k = 0;
            } 
        }
    int maxIdx = min(i, j);
    
    char pat[MAX];
    int sz = 0;
    for(k = maxIdx; k < len+maxIdx; ++k) pat[sz++] = str[k%len];
    pat[sz] = '\0';
    for(i = 0; i < len; ++i) str[i + len] = str[i];
    str[2*len] = '\0';


    printf("%d %d\n", KMPSearch(pat, str), maxIdx+1);

    return 0;
}
```

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/),
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
