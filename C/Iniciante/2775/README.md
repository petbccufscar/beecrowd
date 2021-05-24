# Problema:
Uma montadora de carros, permite que os usuários criem seus próprios projetos de veículos da maneira que desejar e ainda compartilhar tais informações com outros usuários com o intuito de criar uma rede de utilizadores bem diversificada. O processo se inicia com o cliente desenvolvendo seu próprio modelo através de um software, logo após a conclusão, os dados do projeto são armazenados e de acordo com a disponibilidade da montadora vão sendo realizados.

Porém uma falha na entrega das peças para a montadora está atrasando os pedidos. Acontece que as peças são entregues em pacotes, etiquetados com um número, que deveriam estar ordenados de forma crescente para que a produção inicie. A falha é que os pacotes estão sendo entregues de uma forma aleatória. Você deve criar um programa em que dados a ordem de entrega dos pacotes e o tempo que cada um deles leva para ser trocado de posição, calcule o tempo total para organizar os pacotes. Sabe-se que para efeito de organização dentro da empresa, os pacotes devem ser trocados de posição somente dois a dois e se estiverem um do lado do outro.
##### Link do problema: https://www.urionlinejudge.com.br/judge/pt/problems/view/2775
 
 
# Resolução:
 

Para a resolução do problema, iremos importar a biblioteca `stdlib.h`, para utilizarmos a função `malloc()`. Também iremos utilizar o algoritmo de ordenação bubble sort.

Além disso, iremos declarar nosso tipo `pacote`, de forma global, utilizando `typedef struct`, para armazenarmos o valor e o tempo necessário para troca juntos,.

```c
typedef struct pacote{
    int valor;
    int tempo;

} pacote;
```

Iremos declarar as variáveis inteiras `N` e `i`. A variávei `N` representa quantos pacotes o caso de teste terá.

```c
int N, i;
```

Em seguida, utilizaremos uma estrutura de repetição `while` que irá iterar enquanto houver entrada, para ler o valor de `N`. Cada iteração do laço de repetição será um caso teste.

```c
while ((scanf("%d", &N)) != EOF){
```

Em seguida, já com o valor de `N`, declaramos nosso vetor de pacotes de forma dinâmica.

```c
pacote *vetor;
vetor = malloc (N * sizeof (pacote));
```

Agora, realizamos a leitura dos dados. Primeiro, leremos todos os valores dos pacotes e depois, todos os tempos de troca necessários, conforme o padrão da entrada.

```c
for( i = 0; i < N; i++)
    scanf("%d", &vetor[i].valor);
      
for( i = 0; i < N; i++)
    scanf("%d", &vetor[i].tempo);
```


Em seguida, vamos iniciar nosso algoritmo de ordenação [bubble sort](https://www.embarcados.com.br/algoritmos-de-ordenacao-bubble-sort/).

Iremos declarar 3 variáveis que utilizaremos durante a ordenação dos pacotes. A variável `pacote aux` será um auxiliar utilizado durante a troca de pacotes, `soma` indica a soma dos tempos necessários de troca, é o resultado de nosso programa. Já `alterado` será um auxiliar utilizado para verificação se houve troca durante uma iteração do laço. O algoritmo de ordenação irá parar após percorrer o vetor inteiro e não realizar nenhuma troca, o que significa que está ordenado. 

```c
pacote aux;
int alterado = 1;
int soma = 0;
```

Inicializamos `alterado` com `1` para a condição do laço `while` ser verdadeira e iniciarmos a ordenação:
- Atribuímos `0` a `alterado`.
- **A cada iteração do laço `for`, iremos percorrer o vetor do início até `N - 1`**, pois realizamos comparações entre o elemento `i` e o elemento subsequente. Caso `i` for `N` em alguma hipótese, a comparação será realizada entre `N` e `N + 1` e iremos acessar memória além do nosso vetor, pois nosso vetor termina em `N`. 
- Dentro do laço `for` verificamos se o valor de `i` é menor que o de `i + 1` (elemento subsequente). Se sim, somamos os tempos de troca de cada um dos elementos à `soma`, realizamos a troca dos elementos e atribuímos `1` a alterado, indicando que houve troca.

Quando `alterado` não receber o valor `1`, significa que o vetor está ordenado, pois foi percorrido inteiro e não houve nenhuma troca. Com isso, imprimimos o a soma dos tempos de troca, utilizando a função `printf()`.

```c
printf("%d\n", soma);
```

##### Mais sobre alocação dinâmica: [alocação dinâmica](https://www.ime.usp.br/~pf/algoritmos/aulas/aloca.html)
##### Mais sobre bubble sort : [bubble sort](https://www.embarcados.com.br/algoritmos-de-ordenacao-bubble-sort/)



Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com