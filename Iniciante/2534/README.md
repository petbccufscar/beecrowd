# Problema:

Escreva um programa que dado o número de habitantes da Nlogônia e todas as notas obtidas, responda as consultas para retornar a nota do cidadão que ficou em determinada posição.

##### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/2534

# Resolução:

Nesse exercício temos que ler n notas, ordená-las em ordem decrescente e mostrar qual nota está em cada posição que for buscada.

Para esse código, nós não começamos com o `int main()`, mas com uma função criada para fazer o exercício. Essa função se chama `insertionSort` e será explicada no final.

Dentro do `int main()`, vamos criar 4 variáveis do tipo `int`:
```c
    int n, q, p, i;
```
`n` representa o número de notas que vão ser lidas, `q` indica quantas posições serão buscadas e `p` é a variável que vai guardar a posição a ser buscada e `i` é uma variável auxiliar para o `for`.

O exercício aborda um caso de leitura em que deve ser lido até o final do arquivo [EOF - End of File](https://pt.wikipedia.org/wiki/EOF). Fazemos a leitura do `n` e `q` no `scanf` dentro do `while`:
```c
    while (scanf("%d%d", &n, &q)!=EOF) {
```
Um único `scanf` pode ler mais de um valor se usarmos mais de um `%d`. Dentro do `while`, fazemos a leitura e comparamos ao EOF, portanto o `while` irá rodar até chegar no final do arquivo. Este é simbolizado pela quebra de linha (`\n`).

No começo do laço de repetição, criamos um vetor do tipo `int` com `n` posições. Esse vetor vai guardar todas as notas que serão registradas:
```c
      int v[n];
```
Para ler os valores e guardá-los dentro do vetor, usamos um laço de repetição `for` e, dentro dele, um `scanf` para ler o valor:
```c
      for (i=0; i<n; i++)
        scanf("%d", &v[i]);
```
Com os dados do vetor, vamos ordenar eles usando a função `insertionSort` mencionada anteriormente:
```c
      insertionSort(v, n);
```
Depois de ordenar o vetor usando a função `insertionSort`, vamos criar um novo laço de repetição `for` para ler `q` posições e determinar qual nota está presente dentro de cada posição:
```c
      for(i=0;i<q;i++) {
        scanf("%d", &p);
        printf("%d\n", v[p-1]);
      }
    }
```
Dentro da repetição usamos `scanf` para ler um valor `p` e, em seguida, usamos `printf` para mostrar a nota armazenada na posição `p-1` porque um vetor sempre começa na posição 0. Isso quer dizer que se `p` for 1 o exercício está querendo saber o valor na posição 0 do vetor e assim em diante. A segunda chave no final serve para fechar o `while` criado no início do programa.

Esse é o exercício, mas para fazê-lo precisamos criar a função `insertionSort`. Como a função não existe dentro da biblioteca `stdio.h`, criamos essa função antes do `int main()`.

Essa função utiliza como entrada um vetor do tipo `int` (`*vetor`) e uma variável `n` do tipo `int`. As variáveis criadas dentro dessa função não afetam as criadas dentro do `int main()`:
```c
void insertionSort(int *vetor, int n) {  
    int aux, i, j;  
    for (i=1; i<n; i++) {  
        aux = vetor[i];  
        j = i - 1;  

        while ((j>=0) && (vetor[j]<aux)) {  
            vetor[j+1] = vetor[j];  
            j = j-1;  
        }  
        vetor[j+1] = aux;  
    }  
} 
```
Essa função tem como objetivo fazer a ordenação dos valores do `vetor` em ordem decrescente usando [Insertion sort](https://medium.com/@henriquebraga_18075/algoritmos-de-ordena%C3%A7%C3%A3o-iii-insertion-sort-bfade66c6bf1). Primeiro criamos três variáveis do tipo `int`, sendo `aux` o valor auxiliar que guarda o valor que vai ser ordenado e `i` e `j` variáveis que vão ser usadas nos laços de repetição.

A ordenação é feita guardando um valor do vetor em uma variável `aux` e comparando os valores desse vetor até encontrar um valor maior que `aux`. Quando isso acontecer, paramos o laço de repetição `while` e colocamos o valor de `aux` dentro do vetor na posição que ficou vaga. Esse processo ocorre `n` vezes em que `n` é o número de valores dentro do `vetor`.

##### Para aprender mais sobre vetores: [Vetores](http://linguagemc.com.br/vetores-ou-arrays-em-linguagem-c/)
##### Para aprender um pouco mais sobre a estrutura for: [For](http://linguagemc.com.br/a-estrutura-de-repeticao-for-em-c/)
##### Para aprender um pouco mais sobre vetores como entrada de função: [Vetor para função](http://linguagemc.com.br/passando-um-vetor-para-funcao-em-c/)
##### Para aprender um pouco mais sobre a estrutura while: [While](http://linguagemc.com.br/o-comando-while-em-c/)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
