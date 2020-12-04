# Problema:    
Evergreen Bushy, um dos duendes ajudantes de Noel, responsável por inventar muitos dos brinquedos distribuídos por Noel e também muito conhecido por fazer pegadinhas com o bom velhinho, aprontou mais uma neste ano. 

Como sempre faz todos os anos, Bushy separou os presentes para cada criança colocando um bilhete com o nome dela. O problema que ele não se limitou a simplesmente colocar o nome correto da criança no presente: ele zoou :) cada um dos nomes misturando as letras segundo uma sequência: duas letras do nome, seguidas por duas letras do sobrenome, seguidas por duas letras do nome e por duas letras do sobrenome e assim por diante.

Bem, como Noel está bem cansado e sem tempo para brincadeiras, pediu a você que é expert em programação para fazer um programa que converta o nome misturado por Evergreen no nome correto de cada criança.

Apenas um fato curioso: a primeira linha do nome misturado sempre terá um número par de caracteres e a segunda linha, sempre terá o mesmo número de caracteres da primeira linha ou um caractere a menos do que a primeira linha

**Problema Completo**: https://www.urionlinejudge.com.br/judge/pt/problems/view/2722


# Resolução:
O exercício pede para desenvolver um programa que corrija os nomes que tiveram suas letras misturadas por Evergreen. 

Para resolver esse problema, iremos utilizar a biblioteca `<string.h>` para usarmos a função `strlen()` que retorna o tamanho de uma string. 

Como o nome está dividido em duas linhas (nome e sobrenome), a resolução se baseia em pegar dois caracteres do nome, seguidos por dois caracteres do sobrenome, seguidos por dois caracteres do nome e assim por diante até acabar os caracteres e armazenar isso em uma nova `string` que será o nome correto.

Inicialmente, declaramos as variáveis do tipo vetor de `char` `primeiraLinha[100]`, `segundaLinha[100]` e `nomeCerto[200]` onde as duas primeiras armazenarão as entradas e a última a saída. Depois declaramos as variáveis do tipo `int`:
- `n`: Usada para armazenar o número de casos de teste
- `j`: Usada para iterar sobre a string `nomeCerto[200]`
- `i`: Usada para iterar sobre a string `primeiraLinha[100]`
- `k`: Usada para iterar sobre a string `segundaLinha[100]`
- `tamPrimeiraLinha`: Usada para armazenar o tamanho da string `primeiraLinha[100]`
- `tamSegundaLinha`: Usada para armazenar o tamanho da string `segundaLinha[100]`

```c
char primeiraLinha[100], segundaLinha[100], nomeCerto[200];
int n, j, i, k, tamPrimeiraLinha, tamSegundaLinha; 
```

Para começar a resolução, lemos a quantidade de casos de teste `n` com a função `scanf` e fazemos um loop `while(n--)` para iterar sobre todos os casos de teste.

```c
scanf("%d ", &n);

    while(n--){ 
```

Dentro do `while` iniciamos nossas variáveis `i, j, k` com o valor 0. Pois todos irão iterar sobre strings e precisam iniciar na primeira posição delas.  

```c
i = 0;
j = 0;
k = 0;
```

Em seguida, lemos as strings com a função `fgets` e também armazenamos o tamanho delas utilizando o `strlen()`.
```c
fgets(primeiraLinha, sizeof(primeiraLinha), stdin);
fgets(segundaLinha, sizeof(segundaLinha), stdin);

tamPrimeiraLinha = strlen(primeiraLinha);
tamSegundaLinha = strlen(segundaLinha);
```

Agora fazemos um loop `while` para iterar sobre as strings. A condição de parada é `(j+3 < tamPrimeiraLinha + tamSegundaLinha)` pois o `j` é o iterador do `nomeCerto` que no máximo vai ser do tamanho `tamPrimeiraLinha + tamSegundaLinha`. O `j+3` se dá pelo motivo de a cada iteração iremos colocar no mínimo três caracteres no `nomeCerto` - sendo atingido pela última iteração que compõe dois caracteres da primeira linha e um da segunda. Sabemos disso pois no enunciado do problema é dito que a segunda linha pode ter a mesma quantidade de caracteres que a primeira ou um a menos. 
Dentro do `while` teremos `nomeCerto[j++] = primeiraLinha[i++]` que é a mesma coisa que fazer `nomeCerto[j] = primeiraLinha[i]` e em seguida `j++` e `i++`. Com isso, estamos pegando os primeiros dois caracteres da `primeiraLinha` e passando para `nomeCerto` e logo depois fazemos o mesmo com `segundaLinha` para o `nomeCerto` com uma ressalva: Precisamos verificar se a `segundaLinha` acabou ou não, já que ela pode ter um caractere a menos que a `primeiraLinha`. Para isso, fazemos `if(segundaLinha[k+1] != '\0')`, ou seja, verificamos se o próximo caractere da `segundaLinha` é o caracter `\0` que marca o final da string. Se não for, então é um caracter normal e colocamos ele no `nomeCerto`, se for, ignoramos e o `while` acabará nessa iteração. 

```c
while(j+3 < tamPrimeiraLinha + tamSegundaLinha){       
    nomeCerto[j++] = primeiraLinha[i++];
    nomeCerto[j++] = primeiraLinha[i++];
    nomeCerto[j++] = segundaLinha[k++];
    if(segundaLinha[k+1] != '\0')
        nomeCerto[j++] = segundaLinha[k++];
}
```

Finalmente, colocamos um `\0` na posição `j` do `nomeCerto`, ou seja, logo após o último caracter adicionado para indicar o fim dessa string e apresentamos o resultado fazendo um `printf` do `nomeCerto`.

```c
nomeCerto[j] = '\0';
printf("%s\n", nomeCerto);
```
    
#### Para aprender um pouco mais sobre fgets: [Fgets](http://www.w3big.com/pt/cprogramming/c-function-fgets.html)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com

