# Problema

Leia um valor inteiro N que é o tamanho da matriz que deve ser impressa conforme o modelo fornecido.
A entrada contém vários casos de teste e termina com EOF. Cada caso de teste é composto por um único inteiro N (3 ≤ N < 70), que determina o tamanho (linhas e colunas) de uma matriz que deve ser impressa

Exemplo de saída com entrada = 4:

	1332
	3123
	3213
	2331

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/1534

# Resolução

Antes de iniciar o código, é preciso entender o que o enunciado do problema pede, visto que não está escrito de forma intuitiva. 
Conforme dito e exemplificado pela saída do programa, o valor `N` representa as dimensões de uma matriz, sendo desta forma uma [matriz quadrada](https://mundoeducacao.uol.com.br/matematica/matriz-quadrada.htm) e suas definições (como a diagonal principal e secundária), isto é, uma matriz com o mesmo número de linhas e colunas. 
Em seguida, precisamos entender o que a saída do programa nos diz sobre a matriz. Visto os dois exemplos de saída, entendemos que a diagonal principal da matriz é formada por números '1' e a diagonal secundária por números '2', resultando no resto da matriz ser formada por números '3'. 
Com isso, nosso maior desafio para solucionar o problema é adequar-se a estas necessidades.

O primeiro passo é declarar as variáveis que serão utilizadas no problema. Como todos os valores, tanto a matriz e suas dimensões quanto os contadores que usaremos para as estruturas de repetição, são inteiros, declararemos todos do tipo `int`

```c
	int matriz[70][70], N, i, j;
```

Um dos grandes desafios deste problema é não exceder o tempo limite. Desta forma, usaremos uma forma não convencional da estrutura `while`, para que consigamos concluir o exercício sem exceder o tempo.
Em seguida, colocaremos nossa primeira estrutura de repetição, o `while`. Desta vez, como o critério de parada é um valor que não temos ainda e não sabemos quando virá, usaremos-o dentro da estrutura.
Este critério é a leitura de um valor com a função `scanf`. Enquanto o valor de `N` não é igual a EOF, continuaremos a executar os passos dentro do `while`.

```c
    while(scanf("%d", &N) != EOF){
```

Agora, usaremos a estrutura de repetição `for`. Os laços das estruturas são entrelaçados para, com cada loop de `i`, serão feitos `N` loops de `j`. 

```c
        for(i = 0; i < N; i++){
	        for(j = 0; j < N; j++) {
```

Seguidamente, iremos adicionar as condições anteriormente discutidas para adequar a matriz à saída, conforme pede o exercício. Para isso, utilizaremos a condicional `if`.

A primeira condicional que asseguraremos é a diagonal secundária. Ela acontece nos casos inversos à diagonal principal, sendo, por definição, formada por (valor da linha + valor da coluna) = (valor da dimensão - 1).
```c
        if((i + j) == (N - 1)) {
            matriz[i][j] = 2;
```

A segunda condicional é a diagonal principal. Também por definição, temos que é descrita por posições onde o valor da linha é igual ao da coluna.
```c
                else if (i == j){
                    matriz[i][j] = 1;
```

Por último, não atendendo nenhum dos dois critérios definidos, os outros valores da matriz serão preenchidos com 3.
```c
                else {
                    matriz[i][j] = 3;
```

Com isso, finalizamos com mais um par de estruturas `for` entrelaçadas para exibir os elementos da matriz, utilizando a função `printf`. Ao final do loop do `for` com `j`, lembrar de colocar a estrutura `printf` com o `\n` para que seja pulada uma linha, visto que o URI costuma ser rigoroso com as saídas apresentadas pelo programa. 
```c
        for(i = 0; i < N; i++){
            for(j = 0; j < N; j++) {
                printf("%d", matriz[i][j]);
            }
            printf("\n");
        }
```

##### Mais sobre matrizes: [matriz](http://linguagemc.com.br/matriz-em-c/)
##### Mais sobre a matriz quadrada: [matriz quadrada](https://mundoeducacao.uol.com.br/matematica/matriz-quadrada.htm)
##### Mais sobre a estrutura de repetição for: [for](http://linguagemc.com.br/a-estrutura-de-repeticao-for-em-c/)
##### Mais sobre a estrutura de repetição while: [while](http://linguagemc.com.br/o-comando-while-em-c/)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
* [Facebook](https://www.facebook.com/petbcc/),
* [Instagram](https://www.instagram.com/petbcc.ufscar/)
* ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com

