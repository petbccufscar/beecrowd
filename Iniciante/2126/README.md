# Problema

Dados dois números naturais N1 e N2, diz-se que N1 é subsequência contígua de N2 se todos os dígitos de N1 aparecem, na mesma ordem e de forma contígua, em N2. Crie uma aplicação que leia dois números naturais e diga se o primeiro é uma subsequência contígua do segundo.

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/2126

# Resolução

Para resolver o problema, iremos salvar N1 e N2 em vetores, depois procurar N1 em todas as posiçoes possíveis de N2, trabalhando com variáveis temporárias para armazenar as posições e quantidade de subsequencias.

Começamos incluindo a biblioteca `string.h`, que contém os tipos de vetores de caracteres e funções como a `strlen`, que usaremos para contar do tamanho dos vetores.
```c
	#include <string.h>
```

Agora, iremos declarar nossas variáveis iniciais. 
Primeiro, as variáveis inteiras. Serão elas: os contadores de laços de repetição (`i`, `j`, `l` e `k`) e os contadores de `casos` e de confirmação da subsequencia dentro da sequencia `contador`.
```c
    int i, j, casos, contador, k, l;
```

Depois, as variáveis de caracteres, do tipo `char`. Esses vetores de caracteres serão usados para que possamos manipular melhor as sequencias, assim como utilizar funções da biblioteca `string.h` para contabilizar seus tamanhos. Serão elas: o vetor de subsequência N1 `subsq` e o vetor de sequencia N2 `seq`.
```c
    char subsq[100], seq[100];
```

Como não recebemos ou contabilizamos nenhum caso ainda, inicializamos a variável `casos` como 0.
```c
    casos = 0;
```

Inicializamos nossa estrutura de repetição `while`. Como nosso critério de parada do programa é a leitura de um `End Of File (EOF)`, colocaremos a função de leitura `scanf` dentro desta área de condição do `while`. Assim, quando a leitura do `scanf` for `EOF`, nosso programa terminará.]
Como estamos lidando com o tipo `char`, nossa variável de leitura será `%s` (diferentemente do costumeiro `%d`, que utilizamos para tipos inteiros).
```c
    while(scanf("%s%s", subsq, seq)!=EOF)
```

Declararemos mais variáveis dentro da estrutura `while`, visto que elas serão temporárias e reinicializadas em cada loop da estrutura. Serão do tipo inteiro as variáveis: quantidade de subsequências presentes `total`, a última posição em que uma subsequência está presente `posicao`, a temporária `tmp` e as variáveis de tamanho dos vetores de caracteres `tam_subsq` e `tam_seq`.
```c
    int total, posicao, tmp, tam_subsq, tam_seq;
```

Agora, iremos armazenar os tamanhos dos vetores de sequencia e subsequencia lidos em `scanf` em suas respectivas variáveis. Para isso, utilizaremos a função `strlen`, presente na biblioteca `string.h`. Esta função lê um vetor de caracteres e retorna o tamanho.
```c
    tam_subsq = strlen(subsq); 
    tam_seq = strlen(seq);
```

Inicializamos a variável `total` com 0, visto que ainda não começamos a analisar as sequencias e subsequencias, e somamos 1 no contador de `casos`, pois iremos comneçar a ler o primeiro caso de sequencias e subsequencias.
```c
    total = 0;
    casos++;
```

Faremos outra estrutura de repetição, desta vez o `for`. 
A variável de controle de loops será o `i` e, forma os requisitos normais como ser inicializado em 0 e somar 1 a cada loop, terminará quando for igual a `tam_seq - tam_subsq`. Esta condição é feita para que não sejam contabilizadas leituras na sequência onde não caberia a subsequência.
Exemplo: uma situação onde a sequência tem tamanho 30 e a subsequência tenha tamanho 3. Sua substração seria `tam_seq - tam_subsq` = 27.
Em um loop onde a posição de leitura está em 28, caso não houvesse a condição, o algoritmo tentaria procurar uma subsequência de tamanho 3 onde só existiriam 2 espaços, gastando um tempo computacional desnecessário.
Desta forma, este passo é apenas para poupar tempo do algoritmo.
```c
    for(i=0; i <= tam_seq-tam_subsq; i++)
```

Caso a posição `i` do vetor de sequência seja igual à primeira posição do vetor de subsequência (isto é, caso o i-gésimo número da sequência seja igual ao primeiro número da subsequência), achamos uma possível posição de subsequência.
Com isso, colocamos 1 em `contador` (pois encontramos o primeiro número da subsequência) e `i+1` na variável temporária `tmp` (pois possivelmente encontramos a posição que inicia a subsequência).
```c
        if(seq[i] == subsq[0])
            contador = 1; 
        	tmp = i + 1;
```
Colocamos `i + 1` pois o vetor inicia-se no índice 0. 
Exemplo: caso uma subsequência esteja presente no índice 0 do vetor, ela encontra-se na 1ª posição.

Utilizaremos mais uma estrutura `for`. Esta estrutura irá verificar se as próximas posições de sequencia são compatíveis com a subsequência que procuramos.
Utilizaremos as variáveis `k` e `l` para navegar pelos vetores, e o `for` continuará rodando enquanto existirem `l` posições no vetor de subsequncia. `k` inicia-se na posição `i + 1` e `l` em 1 pois, anteriormente, verificamos que a posição `i` da sequencia contém um valor compatível com o primeiro valor da subsequencia, na posição 0. Com isso, verificaremos se esta condição se mantém nas próximas posições.
```c
        for(k = i+1, l = 1; subsq[l]; l++, k++)
```

Caso a posição `k` da sequencia seja igual à `l` da subsequencia, somamos nosso contador de verificação. Caso não seja, o loop `for` termina.
```c
            if(seq[k] == subsq[l]) 
                contador++;
            else
            	break;
```

Caso o valor em contador seja igual ao tamanho da subsequencia, encontramos uma ocorrência (somando 1 em `total`) e armazenamos a posição salva na temporária `tmp` na variavel `posicao`, que será exibida.
```c
	        if(contador == tam_subsq)
                total++;
                posicao = tmp;
```

Por fim, exibimos nossos resultados com a estrutura `printf`.
Começamos exibindo o número do caso atual, visto que podem ocorrer inúmeros casos até `EOF`.
```c
	    printf("Caso #%d:\n", casos);
```

Caso o valor em `total` seja 0, a subsequência procurada não ocorre nenhuma vez na sequência.
```c
        if(total == 0)
            printf("Nao existe subsequencia\n\n");
```

Caso contrário, exibimos a quantidade de subsequências encontradas em `total` e a última posíção onde ela aparece.
```c
        else
        {
            printf("Qtd.Subsequencias: %d\n", total);
            printf("Pos: %d\n\n", posicao);
```

##### Para aprender um pouco mais sobre caracteres: [Caracteres](http://linguagemc.com.br/string-em-c-vetor-de-caracteres/)
##### Para aprender um pouco mais sobre a biblioteca string.h: [string.h](http://linguagemc.com.br/a-biblioteca-string-h/)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
* [Facebook](https://www.facebook.com/petbcc/),
* [Instagram](https://www.instagram.com/petbcc.ufscar/)
* ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
