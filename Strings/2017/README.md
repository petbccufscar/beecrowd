# Problema

O problema é simples. Dada uma string x e 5 outras strings, encontre a string com o menor valor de distância de edição com relação a x. Se o valor da distância de edição for maior do que k, imprima -1.

**Problema Completo:**
https://www.urionlinejudge.com.br/judge/pt/problems/view/2017

# Resolução

O exercício pede para que leia-se uma string `x` inicial, um inteiro `k` e, posteriormente, as próximas 5 linhas contendo uma string `y`. Além disso, precisamos calcular dentre as linhas da string `y`, qual possui menor valor de distância de edição com relação a `x`, ou seja, menor número de caracteres diferentes.

Começaremos declarando as variáveis que iremos utilizar. A variável `x[100001]` irá guardar uma string com até 100000 caracteres (100001 porque é o número de caracteres máximo que o exercício aceita, incluindo o `\0` indicando o fim da string). `y[5][100001]` irá armazenar as 5 strings que precisam ser comparadas com `x`, cada uma delas pode ter até 100000 caracteres. `k` irá armazenar o inteiro de entrada. `distancia[5]` irá armazenar o resultado da distância de edição de cada uma das 5 strings, cada uma em seu respectivo índice. `menor` irá armazenar o índice da menor distância de edição e, finalmente, `i` é a variável auxiliar.

```c
int k, i, distancia[5], menor;
char x[100001], y[5][100001];
```

Após declarar as variáveis, iremos realizar a leitura das entradas. Iniciamos lendo a string `x` e o inteiro `k`. Para realizar a leitura das próximas 5 linhas contendo a string `y`, vamos utilizar o `for` que irá de `i=0` a `i<5`, atribuindo a string lida ao índice `i` atual da variável `y`.

```c
scanf("%s", x);
scanf("%d", &k);

for(i=0;i<5;i++){
    scanf("%s", y[i]);
}
```

Para cada uma das strings `y` lidas, precisamos calcular a distância de edição em relação a string `x`. Para isso vamos utilizar novamente o `for` que irá de `i=0` a `i<5`, chamando a função `distancia_edicao`, que irá receber como argumento a string `x` e a string `y[i]`. Essa função irá retornar o cálculo da distância de edição que será atribuída a variável `distancia[i]`.

```c
for(i=0;i<5;i++){
    distancia[i] = distancia_edicao(x, y[i]);
}
```

Com todos os cálculos feitos, precisamos compará-los e verificar qual string tem a menor distância de edição. Para isso vamos chamar a função `calcula_menor` passando como parâmetro o vetor `distancia`. O retorno da função é o index da string com menor distância de edição. Iremos atribuir o resultado a nossa variável `menor`.

```c
menor = calcula_menor(distancia);
```

Finalmente verificamos se a menor distância de edição é maior que o inteiro `k` lido. Caso for, o resultado mostrado será o inteiro -1, se não, printamos o índice da string com menor distância (índice começando em 1) e, logo em seguida, a menor distância de edição.

```c
if(distancia[menor]>k){
    printf("-1\n");
} else{
    printf("%d\n", menor+1);
    printf("%d\n", distancia[menor]);
}
```

A função `distância_edição` recebe duas strings como parâmetros e verifica quantas letras a string `y` tem de diferente da string `x`. Para isso usamos um auxiliar `i` e um `contador` com valor inicial `0`. Percorremos a string `x` utilizando um `while` e verificamos se a letra atual é diferente de `\0` (que indica o fim da string). Dentro do loop, verificamos se a letra atual de `x` é diferente da letra atual de `y`. Caso for, somamos mais um no `contador`. Ao percorrer toda a string, retornamos o valor do contador.

```c
int distancia_edicao(char *x, char *y){
    int i = 0, contador = 0;
    while(x[i]!='\0')
    {
        if (x[i] != y[i])
            contador++;
        i++;
    }
    return contador;
}
```

A função `calcula_menor` recebe como parâmetro um vetor de inteiros. Esse vetor tem em cada índice o cálculo da distância de edição de cada string. Com isso, a função é responsável por verificar qual o menor valor desse vetor. Para isso declaramos a variável `menor` que vai guardar o menor valor do vetor, ela é iniciada com o primeiro valor desse vetor. Usamos também a variável `index` que irá guardar o index do vetor que possui o menor valor. Vamos percorrer o vetor utilizando um `for` de `i=1` até `i<5` (já estamos considerando o primeiro valor do vetor como o menor). Dentro do loop, verificamos se o valor do index atual de `distancia` é menor que o valor guardado na variável `menor`. Se sim, atribuímos esse valor como o nosso novo menor e atualizamos o index para o atual. Após percorrer todo o vetor, retornamos a nossa variavel `index`.

```c
int calcula_menor(int *distancia){
    int menor=distancia[0], index=0, i;

    for(i=1;i<5;i++){
        if(distancia[i] < menor){
            menor = distancia[i];
            index = i;
        }
    }

    return index;
}
```

**Para aprender um pouco mais sobre a estrutura de repetição for:** [For](http://linguagemc.com.br/a-estrutura-de-repeticao-for-em-c/)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou envie um e-mail com o assunto "URI" para petbcc.ufscar@gmail.com
