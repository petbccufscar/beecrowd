# Problema

Rafael encontrou um novo hobbie: fazer desenhos usando caracteres do teclado. Por mais simples ou limitada que essa nova forma de arte possa parecer, basta criatividade para se fazer os mais diferentes tipos de desenhos.

Após fazer alguns desenhos, Rafael imaginou como seriam se eles fossem redimensionados, porém ter que refazer todo o desenho pareceu meio cansativo. Para isso, Rafael pediu sua ajuda.

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/2174

# Resolução

Para resolver o problema, iremos receber o desenho feito por Rafael, calcular a proporção do novo tamanho e exibir cada linha do novo desenho com uma variável temporária.

Começamos declarando nossas variáveis, que serão do tipo `char` e do tipo `int`. Serão elas:
* `desenho[51][51]`, para representar o desenho de Rafael como uma matriz de caracteres de até 50 posições;
* `temp[51]`, para representar a variável temporária de cada linha do desenho com novas proporções;
`i`, `j`, `k`, `print`, as variáveis de iteração para receber o desenho original e exibir o novo desenho;
* `N`, `M`, representando a altura e largura do desenho, respectivamente;
* `nova_altura`, `nova_largura`, para representar os novos valores de altura e largura do desenho a ser exibido;
* `proporcao_altura, proporcao_largura`, para calcular a proporção entre os novos tamanhos e os originais, visto que são múltiplos.
```c
    char desenho[51][51], temp[51];
    int i, j, k, print;
    int N, M;
    int nova_altura, nova_largura;
    int proporcao_altura, proporcao_largura;
```

Em seguida, iremos iniciar nossa estrutura de repetição `while`, que executará o programa enquanto a leitura de altura e largura `N` e `M` for válida e enquanto a variável de altura `N` for diferente de zero.
Esta adição é necessária por conta do enunciado especificar que a entrada `N = M = 0` não deve ser executada e, visto que `N = M = 0`, podemos usar apenas `N` ou `M` para verificar, para que o código fique mais limpo.
```c
    while(scanf("%d %d", &N, &M), N)
```

Enquanto a entrada não for inválida, o desenho continuará sendo lido pela estrutura `scanf` e salvo em cada posição de `desenho`, iterado pela estrutura de repetição `for` até a altura `N`. Utilizamos o formato `%s`, originalmente de `strings`, pois queremos ler a linha inteira da matriz, em vez dé só um caracter, representado por `%c`.
```c
    for(i=0;i<N;i++){
       scanf("%s", desenho[i]);
```

Depois, lemos a nova altura e largura que o desenho terá e calculamos as proporções entre os valores novos e antigos.
```c
	scanf("%d %d", &nova_altura, &nova_largura);

    proporcao_altura = (nova_altura/N);
    proporcao_largura = (nova_largura/M);
```

Agora, iremos fazer o processo de receber cada linha do desenho original, salvar na variável temporária e exibir o novo desenho.
Primeiro, iremos iniciar uma estrutura `for` que iterará `N`-vezes. Começamos copiando a linha `i` do desenho na variável `temp` com a estrutura `strcpy`, da biblioteca `string.h`.
```c
    for(i=0;i<N;i++)
    {
        strcpy(temp, desenho[i]);
```

Em seguida, iremos utilizar outro `for`, dessa vez pela `proporcao_largura`, para exibir cada linha por proporção. Utilizamos outro `for` para exibir cada caracter da linha lida, que é o tamanho da variável `temp`. Calculamos o tamanho com a estrutura `strlen`, também da biblioteca `string.h`.
```c
    for(j=0;j<proporcao_altura;j++)
        {
            for(k=0;k<strlen(temp);k++)
```

Por fim, instanciamos nosso último `for`, para exibir o caracter selecionado por `k` para ser repetido na quantidade de vezes de `proporcao_largura`. Exibimos cada caracter com `%c` na estrutura `printf`.
```c
        for(print=1;print<=proporcao_largura;print++)
            printf("%c", temp[k]);
```

Finalizamos exibindo as quebras de linha com dois `printf("\n")`, conforme requisitado pelo exercício.
```c
            printf("\n");

    printf("\n");
```

##### Para aprender um pouco mais sobre a biblioteca string: [strings](http://linguagemc.com.br/a-biblioteca-string-h/)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
 * [Facebook](https://www.facebook.com/petbcc/),
 * [Instagram](https://www.instagram.com/petbcc.ufscar/)
 * ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
