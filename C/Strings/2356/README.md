# Problema

Dr. Henrique realmente adora suas pesquisas com bactérias. Na tentativa de criar bactérias mais resistentes a antibióticos, avaliou o DNA de algumas delas e percebeu uma semelhança nas bactérias que eram mais resistentes do que as demais. Todas elas possuiam uma parte do código genético igual (composto pelas proteínas A, C, G, T). Logo constatou que aquele trecho de código genético é o que define se uma bactéria é resistente ou não. Assim, Dr. Henrique pediu para que você fizesse um programa que avalie se uma bactéria é resistente dado seu DNA e o código genético que leva a resistência.

**Problema Completo:**
[https://www.urionlinejudge.com.br/judge/pt/problems/view/2356](https://www.urionlinejudge.com.br/judge/pt/problems/view/2356)

# Resolução

Para verificar se a bactéria é resistente, temos que verificar se o código genético que leva a resistência está contido no DNA da mesma.

Nesse exercício iremos utilizar a biblioteca `string.h`, pois ela contém uma série de funções para manipular strings.

Começaremos declarando as variáveis que iremos utilizar. A variável a[101] irá guardar uma string que representa o DNA da bactéria e b[101] irá guardar uma string que representa o código genético que leva a resistência. Ambas possuem até 100 letras (declaramos 101 porque é o número de caracteres máximo que o exercício aceita, incluindo o `\0` indicando o fim da string).

```c
char a[101], b[101];
```

A entrada do exercício contém vários casos de teste. Dessa forma, inicialmente fazemos um laço de repetição `while` que realiza a leitura da string `a` e compara com `EOF`. Caso essa comparação for verdadeira o algoritmo termina, já que `EOF` representa erro na leitura.

Caso a comparação for falsa, fazemos a leitura da string `b`. Logo em seguida chamamos a função `resistente` passando as strings `a` e `b` como parâmetro. Essa função é responsável por verificar se `b` está contido em `a`, ou seja, se o código genético que leva a resistência está contido no DNA da mesma. Retorna `true` se estiver contida e `false` se não estiver contida. Caso retornar `true`, printamos como resultado que a bactéria é Resistente e, caso contrário, retornamos como resultado Nao resistente.

```c
while(scanf("%s", a) != EOF){
   scanf("%s", b);
   if(resistente(a, b))
      printf("Resistente\n");
   else
      printf("Nao resistente\n");
}
```

A função `resistente`, como comentado acima, recebe as strings `a` e `b` como parâmetros. Inicialmente declaramos a variável `contem` que armazenará a resposta da função `strstr()` e usada para verificar se `b` está contido em `a`. Declaramos `contem` como ponteiro (`*contem`) pois a resposta da função `strstr()` é um ponteiro.

Usamos a função `strstr(a, b)` (contida na biblioteca `string.h`) que verifica se `b` está contido em `a`. Caso exista coincidência entre as strings, retorna um ponteiro para a primeira ocorrência da string apontada por `b` na string apontada por `a`, caso contrário retorna um ponteiro nulo.

Finalmente verificamos se `contem` está declarado, ou seja, não é `null`. Caso for, indica que `b` está contido em `a` e retornamos 1, caso não, retornamos 0.

```c
char resistente(char *a, char *b){
   char *contem;
   
   contem = strstr(a, b);

   if(contem)
      return 1;
   
   return 0;
}
```

**Para aprender um pouco mais sobre a função strstr:** [strstr](http://www.br-c.org/doku.php?id=strstr)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou envie um e-mail com o assunto "URI" para petbcc.ufscar@gmail.com