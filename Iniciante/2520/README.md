# Problema

Analógimôn Go! é um jogo bastante popular. Em sua jornada, o jogador percorre diversas cidades capturando pequenos monstrinhos virtuais, chamados analógimôns. Você acabou de chegar em uma cidade que contém o último analógimôn que falta para sua coleção!

A cidade pode ser descrita como um grid de N linhas e M colunas. Você está em uma dada posição da cidade, enquanto o último analógimôn está em outra posição da mesma cidade. A cada segundo, você pode se mover (exatamente) uma posição ao norte, ao sul, a leste ou a oeste. Considerando que o analógimôn não se move, sua tarefa é determinar o menor tempo necessário para ir até a posição do monstrinho.

A figura abaixo descreve o exemplo da entrada, e apresenta um caminho percorrido em 5 segundos. Outros caminhos percorridos no mesmo tempo são possíveis, mas não há outro caminho que pode ser percorrido em um tempo menor.

![Mapa](https://www.urionlinejudge.com.br/gallery/images/problems/UOJ_2520.png)


**Link do problema:** https://www.urionlinejudge.com.br/judge/pt/problems/view/2520

# Resolução

Para resolver esse problema, faremos um cálculo de distância entre a posição do jogador e do analogimôn, que consiste na soma das distâncias verticais e horizontais entre eles.

Nesse exercício, utilizamos a biblioteca `<stdlib.h>` para fazer uso da função `abs()` que retorna o valor absoluto (positivo) do que for passado como argumento (ex: abs(-3) = 3).

Primeiramente, declararemos as variáveis que serão utilizadas. A matriz `cidade` é nosso "campo", declarada inicialmente com tamanho 100x100, que é o tamanho máximo de `N` e `M`,o tamanho real dessa cidade é dado por `N` x `M` que representam a quantidade de linha e colunas, respectivamente. `pos_i_jogador` e `pos_j_jogador` é a posição na matriz, em linha e colunas em que o jogador está, o mesmo vale para o analogimon, com as variáveis `pos_i_analogimon`, `pos_j_analogimon` e por fim, `i` e `j` serão contadores para os loops.

```c
    int i, j;
    int N, M, cidade[100][100], dist;
    int pos_i_jogador, pos_j_jogador, pos_i_analogimon, pos_j_analogimon;
```

Começaremos validando a condição de saída do exercício, que diz que a entrada terminará com o fim do arquivo (EOF).

```c
while(scanf("%d %d",&N,&M) != EOF){
    /*
        [Lógica omitida]
    */
}
```

Já dentro do loop `while` faremos agora dois loops `for` encadeados, para percorrermos a matriz `cidade` inteira. Para cada `i` e `j` fazemos um `scanf` para receber o valor a ser preenchido na matriz, que pode ser 2 para indicar a posição do analogimon, 1 para indicar a posição do jogador e 0 para os campos vazios.
Fazemos a verificação `if(cidade[i][j] == 1)` para identificarmos a posição do jogador e à armazenamos em `pos_i_jogador` e `pos_j_jogador` e simultaneamente, a mesma verificação e atribuição para encontrar o analogimon, porém, armazenamos nas variáveis `pos_i_analogimon` e `pos_j_analogimon`.

```c
while(scanf("%d %d",&N,&M) != EOF){
    for(i = 0; i < N; i++){
        for(j = 0; j < M; j++){
            scanf("%d", &cidade[i][j]);
            if(cidade[i][j] == 1){
                pos_i_jogador = i;
                pos_j_jogador = j;
            }
            if(cidade[i][j] == 2){
                pos_i_analogimon = i;
                pos_j_analogimon = j;
            }
        }
    }   
}
```

Agora, ainda dentro do loop `while` acima, após terminar o loop `for` externo, faremos o cálculo da distância, que consiste em somar a distância vertical e horizontal do jogador ao analogimon. Para esse cálculo utilizamos a função `abs(pos_i_jogador - pos_i_analogimon)` para receber o valor absoluto (distancia) horizontal e `abs(pos_j_jogador - pos_j_analogimon)` para receber o valor absoluto (distancia) vertical.
E por fim, exibimos na tela o resultado da soma dessas duas distancias com a função `printf`

```c
 while(scanf("%d %d",&N,&M) != EOF){

    for(i = 0; i < N; i++){
        for(j = 0; j < M; j++){
            scanf("%d", &cidade[i][j]);
            if(cidade[i][j] == 1){
                pos_i_jogador = i;
                pos_j_jogador = j;
            }
            if(cidade[i][j] == 2){
                pos_i_analogimon = i;
                pos_j_analogimon = j;
            }
        }
    }

    dist = abs(pos_i_jogador - pos_i_analogimon) + abs(pos_j_analogimon - pos_j_jogador);

    printf("%d\n",dist);


}
```

#### Revise sobre estruturas de decisão aqui: [If/else](http://linguagemc.com.br/estrutura-de-decisao-if-em-linguagem-c/#:~:text=Uma%20estrutura%20de%20decis%C3%A3o%20examina,estrutura%20de%20decis%C3%A3o%20muito%20utilizada.&text=Elaborar%20um%20programa%20em%20linguagem,valor%20da%20soma%20na%20tela.)

#### Para entender melhor o fim do arquivo: [EOF](https://pt.wikipedia.org/wiki/EOF)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com




