# Problema:    
Leia um caractere maiúsculo, que indica uma operação que deve ser realizada e uma matriz M[12][12]. Em seguida, calcule e mostre a soma ou a média considerando somente aqueles elementos que estão na área inferior da matriz, conforme ilustrado abaixo (área verde).

<img src="https://resources.urionlinejudge.com.br/gallery/images/problems/UOJ_1188.png">

**Problema completo**: https://www.urionlinejudge.com.br/judge/pt/problems/view/1188


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
- Começamos em `[11][1]`, terminamos em `[11][10]`;
- Começamos em `[10][2]`, terminamos em `[10][9]`;
- Começamos em `[9][3]`, terminamos em `[9][8]`;
- (...)
###### Matrizes são escritas em [linha][coluna]
###### Optamos por percorrer a matriz debaixo para cima, mas isso não é obrigatório

Note o padrão: a cada linha, aumentamos 1 unidade no início, diminuímos 1 unidade no fim. Seguindo a mesma lógica do loop anterior para percorrer a matriz, faremos dois laços `for`. Sendo assim:
- começamos na linha 11, coluna 1, e vamos até a coluna 10;
- na próxima linha, aumentamos 1 coluna no início e diminuímos 1 coluna no fim.

O primeiro `for` percorre as 5 linhas da matriz, de 11 até 7.
Para o segundo `for`, vamos utilizar uma variável auxiliar `offset` para deslocar as colunas - esta variável será somada e subtraída de cada lado das linhas. Representamos as colunas iniciais com `(1 + offset)` e as finais por `(10 - offset)`.  
Para cada posição da matriz, incrementamos o `total` com seu valor.  
Após o fim da linha, incrementamos `offset`.

```c
for (i = 11; i >= 7; i--) {
    for (j = (1 + offset); j <= (10 - offset); j++) {
        total += M[i][j];
    }
    offset++;
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
