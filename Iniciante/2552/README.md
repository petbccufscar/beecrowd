# Problema

Está chegando a grande final do Campeonato Nlogonense de Surf Aquático, que este ano ocorrerá na cidade de Bonita Horeleninha (BH)! Nesta cidade, o jogo PãodeQueijoSweeper é bastante popular!

O tabuleiro do jogo consiste em uma matriz de N linhas e M colunas. Cada célula da matriz contém um pão de queijo ou o número de pães de queijo que existem nas celulas adjacentes a ela. Uma célula é adjacente a outra se estiver imediatamente à esquerda, à direita, acima ou abaixo da célula. Note que, se não contiver um pão de queijo, uma célula deve obrigatoriamente conter um número entre 0 e 4, inclusive.

Dadas as posições dos pães de queijo, determine o tabuleiro do jogo!

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/2552

# Resolução

Para resolver o problema, iremos, posição por posição, verificar se existe um pão de queijo na posição ou em suas redondezas, e exibir o valor da posição com esses critérios.

Começamos declarando as variáveis, todas do tipo inteiro. Serão elas:
- `N`, o número de linhas;
- `M`, o número de colunas;
- `a[100][100]`, a matriz do tabuleiro com 10000 posições;
- `soma`, para a quantidade de pães de queijo nas redondezas;
- `i` e `j`, para iterar pelas estruturas de repetição.
```c
    int N, M;
    int a[100][100], soma;
    int i, j;
```

Inicializamos nossa estrutura de repetição `while`. Seu critério de parada será a leitura de um EOF (End of File - Fim do arquivo) pela estrutura `scanf` nas variáveis `N` e `M`.
```c
    while(scanf("%d %d", &N, &M) != EOF)
```

Em seguida, inicializamos duas estruturas `for` para receber se há ou não pães de queijo na matriz. Utilizaremos a estrutura `scanf` para ler os valores e colocar em suas devidas posições na matriz.
```c
        for(i=0;i<N;i++)
        {
            for(j=0;j<M;j++)
                scanf("%d", &a[i][j]);
```

O primeiro caso que iremos tratar é a matriz 1x1, com apenas um elemento.
Caso ela tenha um pão de queijo, exibiremos 9 com a estrutura `printf`. Caso contrário, 0, pois não há nenhuma posição perto com um pão de queijo.
```c
        if(M==1)
        {
            if(N==1)
            {
                if(a[0][0]==1) 
                    printf("9");
                else 
                    printf("0");
            }
```

Caso tenha 1 coluna, mas mais de uma linha, faremos outro `for` para navegar pelas posições procurando um pão de queijo.
Inicializamos nossa variável `soma` com 0, visto que não foi contabilizado nenhum pão de queijo nas redondezas.
```c
            else{
                
                for(i=0;i<N;i++)
                {
                    soma=0;
```

Enquanto não estamos na última posição (N-1), verificamos se a posição atual é igual a 1, isto é, tem um pão de queijo.   
* Caso tenha, exibimos 9.   
* Caso contrário, procuramos se há na próxima posição.   
    * Caso haja, somamos 1 na variável `soma`.
```c
                    if(i!=N-1)
                    {
                        if(a[i][0]==1) 
                            printf("9");
	                    else
                        {
                            if(a[i+1][0]==1)
                                soma+=1;
                                printf("%d", soma);
                        }

```

Caso estejamos na última posição, verificamos se há um pão de queijo nela. 
	- Em caso positivo, exibimos 9.
	- Em caso negativo, procuramos na posição anterior. 
		- Caso haja, somamos na variável `soma`.

Por fim, exibimos o valor em `soma`.
```c
                    else{
                            if(a[i][0]==1) 
                                printf("9");
                            
                            else{
                                
                                if(a[i-1][0]==1)
                                soma+=1;
                        
                        printf("%d", soma);
```

Agora, trataremos os casos em que há 2 colunas. 
Caso seja apenas 1 linha, inicializamos nossa variável de soma e verificamos se a primeira posição contém um pão de queijo.  
* Em caso positivo, exibimos 9.  
* Em caso negativo, procuramos se a próxima posição à inicial contém.  
    * Caso tenha, exibimos 1 pois há um pão de queijo na redondeza.  
    * Caso contrário, exibimos 0 pois não há nenhum próximo.

```c
        else if(M==2)
        {
            if(N==1)
            {
                soma=0;

                if(a[0][0]==1)
                    printf("9");
                else
                {
                    if(a[0][1]==1)
                        printf("1");
                    else 
                        printf("0");
                }
```

Verificamos, com isso, a próxima posição. A mesma sequência de ações é feita, porém verificamos a posição anterior em vez da próxima. Por fim, pulamos uma linha.
```c
                if(a[0][1]==1)
                    printf("9");
                else
                {
                    if(a[0][0]==1)
                        printf("1");
                    else 
                        printf("0");
                }
                printf("\n");
```

Caso haja mais de uma linha, faremos duas estruturas `for` para procurar, posição por posição, se há pães de queijo nas redondezas. Inicializamos a variável soma como 0 e verificamos se a posição atual tem um pão de queijo, exibindo 9 em caso positivo.
```c
            else{
                for(i=0;i<N;i++)
                {
                    for(j=0;j<M;j++)
                    {
                        soma=0;

                        if(a[i][j]==1) 
                            printf("9");
```

Caso contrário, verificaremos em todas as posições se sua posição atual tem um pão de queijo ou algum em sua redondeza. Seguiremos sempre a sequência de verificar, em ordem:  
* A posição inicial  
* A última  
* Outras posições
Podemos, inclusive, somar o valor presente na posição da matriz, visto que é formada por 0 e 1.

Por fim, exibiremos a soma e a quebra de linha.
```c
                        else
                        {
                            if(j==0)
                            {
                                if(i==0)
                                {
                                    if(a[i][j+1]==1) soma+=1;
                                    if(a[i+1][j]==1) soma+=1;
                                }
                                else if(i==N-1)
                                {
                                    if(a[i][j+1]==1) soma+=a[i][j+1];
                                    if(a[i-1][j]==1) soma+=a[i-1][j];
                                }
                                else{
                                    if(a[i][j+1]==1) soma+=1;
                                    if(a[i+1][j]==1) soma+=1;
                                    if(a[i-1][j]==1) soma+=a[i-1][j];

                                }
                            }
                            else{
                                    if(i==0)
                                {
                                    if(a[i][j-1]==1) soma+=1;
                                    if(a[i+1][j]==1) soma+=1;
                                }
                            else if(i==N-1)
                                {
                                    if(a[i][j-1]==1) soma+=1;
                                    if(a[i-1][j]==1) soma+=1;
                                }
                                else{
                                    if(a[i][j-11]==1) soma+=1;
                                    if(a[i+1][j]==1) soma+=1;
                                    if(a[i-1][j]==1) soma+=1;

                                }
                            }
                            printf("%d", soma);

```

Caso não seja uma matriz com 1 ou 2 colunas, faremos o caso geral.
Inicializamos a váriavel `soma` novamente em 0.
Seguimos a mesma sequência de ações demonstrada anteriormente, verificando, em ordem:
	- A posição atual;
	- A posição inicial;
	- A última posição;
	- As outras posições.

Por fim, exibimos a soma final e a quebra de linha.
```c
        else{
        for(i=0;i<N;i++)
        {
            for(j=0;j<M;j++)
            {
                soma=0;
                if(a[i][j]==1)
                    printf("9");
                else{
                    if(j==0)
                    {
                        if(i==0)
                        {
                            if(a[i][j+1]==1) soma+=a[i][j+1];
                            if(a[i+1][j]==1) soma+=a[i+1][j];
                        }
                        else if(i==N-1)
                        {
                            if(a[i][j+1]==1) soma+=a[i][j+1];
                            if(a[i-1][j]==1) soma+=a[i-1][j];
                        }
                        else
                        {
                            if(a[i][j+1]==1) soma+=a[i][j+1];
                            if(a[i-1][j]==1) soma+=a[i-1][j];
                            if(a[i+1][j]==1) soma+=a[i+1][j];
                        }
                    }
                    else if(j<M-1)
                    {
                        if(i==0)
                        {
                            if(a[i][j+1]==1) soma+=a[i][j+1];
                            if(a[i+1][j]==1) soma+=a[i+1][j];
                            if(a[i][j-1]==1) soma+=a[i][j-1];
                        }
                        else if(i==N-1)
                        {
                            if(a[i][j+1]==1) soma+=a[i][j+1];
                            if(a[i-1][j]==1) soma+=a[i-1][j];
                            if(a[i][j-1]==1) soma+=a[i][j-1];
                        }
                        else
                        {
                            if(a[i][j+1]==1) soma+=a[i][j+1];
                            if(a[i+1][j]==1) soma+=a[i+1][j];
                            if(a[i][j-1]==1) soma+=a[i][j-1];
                            if(a[i-1][j]==1) soma+=a[i-1][j];
                        }
                    }
                    else{
                        if(i==0)
                        {
                            if(a[i][j-1]==1) soma+=a[i][j-1];
                            if(a[i+1][j]==1) soma+=a[i+1][j];
                        }
                        else if(i==N-1)
                        {
                            if(a[i][j-1]==1) soma+=a[i][j-1];
                            if(a[i-1][j]==1) soma+=1;
                        }
                        else
                        {
                            if(a[i][j-1]==1) soma+=1;
                            if(a[i-1][j]==1) soma+=1;
                            if(a[i+1][j]==1) soma+=1;
                        }
                    }
                    printf("%d", soma);
                }
            }
            printf("\n");
```

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
