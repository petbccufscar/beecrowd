# Problema

Você terá como uma entrada várias linhas, cada uma com uma string. O valor de cada caracter é computado como segue

Valor = (Posição no alfabeto) + (Elemento de entrada) + (Posição do elemento)

Todas posições são baseadas em zero. 'A' tem posição 0 no alfabeto, 'B' tem posição 1 no alfabeto, ... O cálculo de hash retornado é a soma de todos os caracteres da entrada. Por exemplo, se a entrada for 
CBA 
DDD

então cada caractere deverá ser computado como segue

2 = 2 + 0 + 0  'C' no elemento 0 posição 0 
2 = 1 + 0 + 1  'B' no elemento 0 posição 1 
2 = 0 + 0 + 2  'A' no elemento 0 posição 2 
4 = 3 + 1 + 0  'D' no elemento 1 posição 0 
5 = 3 + 1 + 1  'D' no elemento 1 posição 1 
6 = 3 + 1 + 2  'D' no elemento 1 posição 2

O cálculo final de hash será 2+2+2+4+5+6 = 21.

Problema Completo
[httpswww.urionlinejudge.com.brjudgeptproblemsview1257](httpswww.urionlinejudge.com.brjudgeptproblemsview1257)

# Resolução

O exercício pede que para cada string de entrada, deve-se calcular o valor de cada caractere dessa string, de acordo com sua posição no alfabeto, o elemento de entrada a qual ele pertence e sua posição na string.

Começaremos declarando as variáveis que iremos utilizar. A variável `linha[51]` irá guardar uma string com até 50 letras maiúsculas (51 porque é o número de caracteres máximo que o exercício aceita, incluindo o `\0` indicando o fim da string). `n`, `l`, `i`, `j` e `k` são variáveis auxiliares. `total` é a variável responsável por guardar o cálculo final de hash e retornar o resultado no fim do código.

```c
char linha[51];
int n, l, i, j, k, total;
```

A entrada do exercício contém vários casos de teste. Dessa forma, inicialmente realiza-se a leitura de um inteiro `n`, que representa a quantidade de casos de teste. Para cada caso de teste, pode-se ler `l` strings. Para realizarmos a leitura de `l` para cada caso de teste, fazemos isso dentro de um `for`, que irá de 0 até a quantidade de casos de teste de entrada (valor salvo na variável `n`). Dessa forma, realiza-se a leitura de um inteiro `l`, que representa a quantidade de linhas que vem a seguir. Neste caso, utilizamos `%d%c` ao invés de apenas `%d` porque ele é responsável por ler algum caractere que entrou no buffer (neste caso o `n` ao dar ENTER) e, posteriormente, limpar a sujeira do buffer. Realizamos também a atribuição do valor 0 a variável `total`, já que toda vez que o código entrar nesse loop, irá retornar um novo valor `total` para as novas strings de entrada.

```c
scanf(%d, &n);
for(i=0;in;i++){
   scanf(%d%c, &l);
   total = 0;
   /* Continuação omitida */
}
```

Cada uma dessas linhas contém uma string com até 50 letras maiúsculas. Para realizarmos a leitura de todas as strings, fazemos isso dentro de um `for`, que irá de 0 até a quantidade de strings de entrada (valor salvo na variável `l`).

```c
scanf(%d, &n);
for(i=0;in;i++){
   scanf(%d%c, &l);
   total = 0;
   for(j=0;jl;j++){
      scanf(%s%c, linha);
      /* Continuação omitida */
   }
   /* Continuação omitida */
}
```

Para cada linha, vamos retornar um resultado `total`, que é a soma dos valores calculados para cada caractere. Para percorrer todas as letras da string, usamos um `for` que é iniciado na letra de posição 0 e percorre até a letra da string ser igual a `\0`, que indica o fim dessa string. Realizamos a soma com o valor de cada caractere e atribuímos à variável `total`. Esse valor, como comentado no enunciado, depende da posição da letra no alfabeto, o elemento de entrada a qual ela pertence e sua posição na string.

Para calcularmos a posição da letra no alfabeto, usamos como base a tabela [ASCII](httpsweb.fe.up.pt~ee96100projectoTabela%20ascii.htm), que é um conjunto de códigos binários que codificam 128 sinais, entre eles as letras do alfabeto latino. A letra A tem código decimal 65, a letra B tem código decimal 66, e assim por diante. Ao realizar `linha[k] - 65`, estamos pegando o código decimal da letra na posição `k` da string `linha` e subtraindo 65 (que é a quantidade de símbolos anteriores ao alfabeto), resultando na posição da letra no alfabeto. Pegamos como exemplo a letra A, seu código decimal é 65, ao realizar a subtração 65 - 65, obtemos o resultado 0, que é sua posição no alfabeto.

O elemento de entrada a qual ela pertence está sendo representado pela variável `j`, que guarda o elemento atual que está sendo lido, e sua posição na string está sendo representada pela variável `k`, que guarda a posição do elemento.

Ao término do `for`, finalmente o programa retorna o resultado da variável `total`.

```c
scanf(%d, &n);
for(i=0;in;i++){
   scanf(%d%c, &l);
   total = 0;
   for(j=0;jl;j++){
      scanf(%s%c, linha);
      for(k=0;k<linha[k] != '\0';k++){
          total += linha[k] - 65 + j + k;
      }  
  }
  printf("%d\n", total);
}
```

Para aprender um pouco mais sobre a estrutura de repetição for [For](httplinguagemc.com.bra-estrutura-de-repeticao-for-em-c)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](httpswww.facebook.competbcc),
[Instagram](httpswww.instagram.competbcc.ufscar)
ou nos mande um e-mail com o assunto URI para petbcc.ufscar@gmail.com.
