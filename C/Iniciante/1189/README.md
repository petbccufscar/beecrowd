# Problema:    
Leia um caractere maiúsculo, que indica uma operação que deve ser realizada e uma matriz M[12][12]. Em seguida, calcule e mostre a soma ou a média considerando somente aqueles elementos que estão na área esquerda da matriz, conforme ilustrado abaixo (área verde).

<img src="https://resources.urionlinejudge.com.br/gallery/images/problems/UOJ_1189.png">

**Problema completo**: https://www.urionlinejudge.com.br/judge/pt/problems/view/1189


# Resolução:
O exercício resume-se em ler uma matriz 12x12 e exibir a soma/média da parte superior, conforme exemplificado na imagem. Sendo assim, faremos a leitura e somamos todos os valores em uma variável `total` e, caso a operação seja média, dividimos o total por 30 - que é a quantidade de valores somados.  

Começamos declarando as variáveis necessárias para o problema. Declaramos `total` e `M` como variáveis `double` já que o exercício especifica a entrada como _valores de ponto flutuante_. A variável `O` será o caractere (`char`) que indica soma ou média e as variáveis `i`, `j` e `offset` para percorrer a matriz.  
Além disso, inicializamos `total` e `offset` com 0 para poder incrementar as variáveis depois.

```c
double total, M[12][12];
char O;
int i, j, offset;

total = 0;
offset = 0;
```

Para identificar a operação a ser realizada, utilizamos a função `scanf()` com `%c` - a operação é representada por um caractere `'S'` ou `'M'`.

```c
scanf("%c", &O);
```

Agora, devemos preencher nossa matriz `M`. Como sabemos que será uma matriz 12x12, usaremos duas instruções `for` - uma para percorrer cada linha da matriz, outra para cada coluna dentro da linha. Assim, faremos a leitura de cada valor com a função `scanf()`, utilizando cada posição da matriz como destino.  
*Utilizamos `%lf` para ler valores do tipo `double`.

```c
for (i = 0; i < 12; i++) {
    for (j = 0; j < 12; j++) {
        scanf("%lf", &M[i][j]);
    }
}
```

Com a matriz preenchida, devemos percorrer as posições indicadas para realizar a soma, independente da operação definida no início do programa. Para isso, faremos as seguintes observações sobre as posições marcadas:
- Começamos em `[1][0]`, terminamos em `[1][0]`;
- Começamos em `[2][0]`, terminamos em `[2][1]`;
- Começamos em `[3][0]`, terminamos em `[3][2]`;
- (...)
- Da linha 5 para 6, não mudamos as colunas finais;
- A partir da linha 6, diminuímos as colunas;
###### Matrizes são escritas em [linha][coluna]

Seguindo a mesma lógica do loop anterior para percorrer a matriz, faremos dois laços `for` - o primeiro para as linhas, o segundo para as colunas. Sendo assim:
- Começamos na linha 1, coluna 0, e vamos até a linha 10;
- A cada linha, incrementamos a coluna final em 1 unidade;
- Na linha 5, não mudamos o deslocamento;
- A partir da linha 6, decrementamos o final em 1 unidade.

Para o segundo `for`, vamos utilizar a variável `offset` para deslocar as colunas finais - esta variável será somada e subtraída de acordo com a execução. Para cada posição da matriz, incrementamos o `total` com seu valor.  
Após a última coluna, verificamos se a linha é menor que 5 - se sim, incrementamos `offset`; se não, verificamos se é maior ou igual a 6 e decrementamos `offset` para a próxima repetição.

```c
for (i = 1; i <= 10; i++) {
    for (j = 0; j <= offset; j++) {
        total += M[i][j];
    }

    if(i < 5) {
        offset++;
    } else if (i >= 6) {
        offset--;
    }
    
}
```

Tendo somando todos os valores das posições marcadas, vamos verificar qual a operação inserida no início do programa. Caso seja soma, devemos apenas exibir o resultado na tela. Caso seja média, vamos dividir o total por 30 antes de exibi-lo.  
Utilizamos `%.1lf`, sendo o `.1` para indicar uma casa decimal após a vírgula e `lf` para variáveis `double`.

```c
if (O == 'S') {
    printf("%.1lf\n", total);
}

else if (O == 'M') {
    total = total / 30.0;
    printf("%.1lf\n", total);
}
```

##### Para aprender mais sobre matrizes: [Matrizes em C](http://linguagemc.com.br/matriz-em-c/)
##### Para revisar variáveis de ponto flutuante: [Os tipos float e double](https://www.cprogressivo.net/2012/12/Os-tipos-float-e-double-numeros-decimais-reais-em-C.html)
    
Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
