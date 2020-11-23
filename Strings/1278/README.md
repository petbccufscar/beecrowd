 # Problema

 Nós temos alguns textos e queremos formatá-los e justificá-los à direita, ou seja, alinhar suas linhas à margem direita de cada um. Crie um programa que, após ler um texto, reimprima esse texto com apenas um espaço entre as palavras e suas linhas justificadas à direita em todo o texto.

Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/1278

 # Resolução

 Devemos então, dadas frases na entrada do problema, justificá-las para a direita, retirando também os espaços extras do meio da frase.

Usamos as bibliotecas `string.h` para podermos mexer com strings, que são cadeias de texto.
Já a biblioteca `ctype.h` foi usada para podermos usarmos a função "isspace" que decide se o argumento representa um espaço em branco, ou seja, um de ` \  \t \n \v \f \r`.

Declaração de variáveis:

 Usamos no programa principal 5 váriaveis do tipo `int` e 1 do tipo `char`:

`N` - indica o número de linhas com frases que o usuário irá inserir;

`i, j, t` - são variáveis auxiliares para os loops que faremos durante o código;

`maior_frase` - o número de caracteres da maior frase;

`frase` - (do tipo char) a variável que vai carregar a frase que o usuário irá digitar.

Explicação da resolução:

 O código começa lendo o valor de `N` com a função `scanf`, que lê o valor da variável.
No trecho do código a seguir, o programa faz um loop de 0 até `N`(utilizando `i` como a variável auxiliar) para que seja possível ler todas as frases que o usuário digita, além disso ele utiliza uma função criada fora da função principal chamada `tratastring` que retira os espaços inválidos da frase. (explicação da função `tratastring` logo após o trecho do código mencionado acima).

``` c
while (N!=0) {
    for (i=0; i<N; i++) {
      scanf(" %[^\n]", frase[i]); 
      tratastring(frase[i]); ```
       

Função `tratastring`:

 O usuário pode digitar frases com vários espaços entre as palavras, por exemplo "read (vários espaços) me",  o objetivo da função tratastring é retirar esses espaços não válidos (um espaço válido é aquele   que está entre duas letras). Então declaramos a variável ponteiro do tipo char chamada frase, que será passada por parâmetro na função main (essa variável é aquela que já foi lida na main). Saiba mais sobre passagem por parâmetro em http://linguagemc.com.br/funcao-com-passagem-por-   referencia/ . Além disso, declaramos também as variáveis inteiras `i` e `j`, que serão utilizadas como auxiliares no loop e a variáel `aux[50]`, que irá receber os caracteres válidos da frase. 

 Depois disso, fizemos um `for` que vai percorrer cada caracter da frase digitada. A função `strlen`,  da biblioteca `string.h` nos retorna o número de caracteres da frase, então nosso for começa em i = 1 e termina quando o `i` é igual ao número de caracteres da frase, somando 1 no i a cada loop.

 O `for` percorre cada caracter e em cada um dele, ele verifica se é uma letra ou um espaço válido,  e, quando é um dos dois, ele copia e cola o caracter na posição `j` na váriavel `aux`. O `if` nesse  `for`, então, verifica se cada caracter é ou uma letra ou um espaço que está entre duas letras, ou seja, um espaço válido.
Vamos entender a condição do if:

``` c
if(!isspace(frase[i]) || (frase[i] == '\n') || (isspace(frase[i]) && !isspace(frase[i-1]))) {
        aux[j] = frase[i];
        j++; } ```

 Lembrando que `||` significa "ou" e `&&` significa "e". Antes do primeiro || está sendo verificado se o caracter não é um espaço usando a função `isspace`, já explicada anteriormente. Em seguida, verifica se a frase tem algum `\n`, algo que sempre tem no final de todas as frases. Em seguida, verifica se o caracter é um espaço e se for, verifica se há uma letra antes dele. Dessa forma ele está verificando se o caracter é uma letra ou um espaço válido.
       
 Entretanto, após colar os caracteres em `aux` nas posições em `j`, ainda pode o acontecer o seguinte caso: "read me ", ou seja, um último espaço logo após o fim da frase. Dessa forma, já com a frase ~quase~ válida colada em `aux`, fazemos outro if para verificarmos se há esse último espaço na frase, caso ele exista nós o retiramos. Assim, a parte do código abixo verfica se o penúltimo caracter da frase é um espaço, já que o último caracter vai ser sempre o `\n`. 

```c
if(aux[strlen(aux)-1] == ' '){
      aux[strlen(aux)-1] = aux[strlen(aux)]; ```

Para finalizar a função `tratastring`, nós colcamos tudo de `aux` na variável `frase` com a função strcpy da biblioteca `string.h`, que copia tudo da variável do segundo argumento para o primeiro.

 `strcpy(frase, aux); `

Agora voltamos para nossa função `main`.

Após usarmos a função `tratastring` na váriavel frase, zeramos a variável `maior_frase` que nos dá o número de caracteres da frase com mais caracteres (válidos!!! nossa frase já foi tratada e não tem nenhum espaço inválido mais).
Assim, fazemos um `for` de `i=0` até `i<N`, somando 1 no i a cada loop. Depois usamos uma outra função criada antes da main chamada max que retorna o maior valor de dois números.
Assim, `maior_frase` recebe o número de caracteres da maior frase (tudo isso acontece dentro do `for`).

```c
maior_frase = 0;
    for(i = 0; i < N; i++){
      maior_frase = max(maior_frase, strlen(frase[i]));  ```

Após esse `for`, fazemos outro `for`, de `j` até `t` para justificarmos a frase para direita. Um espaço é printado antes das menores frases, até que essas fiquem do mesmo tamanho (somando espaços printados + caracteres válidos) da maior frase.

 ```c
 for(i = 0; i < N; i++){
            t = maior_frase - strlen(frase[i]);
           for(j=0;j<t;j++){
                printf(" ");```

No final, quando `N` for diferente de zero a frase é printada para o monitor.

``` c
if(N!=0){
      printf("\n"); ```


if(N!=0){
      printf("\n"); ```







 