# Problema:
Neste programa seu trabalho é ler um valor inteiro que será o tamanho da matriz quadrada (largura e altura) que será preenchida da seguinte forma: a parte externa é preenchida com 0, a parte interna é preenchida com 1, a diagonal principal é preenchida com 2, a diagonal secundária é preenchida com 3 e o ponto central contém o valor 4, conforme os exemplos abaixo.

**Obs**: o quadrado com '1' sempre começa na posição tamanho/3, tanto na largura quanto quanto na altura. A linha e a coluna começam em zero (0).

**Problema Completo**: https://www.urionlinejudge.com.br/judge/pt/problems/view/1827


# Resolução:
É importante armazenarmos a primeira entrada para que então declaremos uma matriz com tamanho equivalente ao número fornecido. O ponto chave deste exercício é identificar o padrão que representa cada uma das categorias estabelecidas (partes externa e interna, diagonais principal e secundária e ponto central) para que seja possível realizar o preenchimento correto.  

Em um primeiro momento, declaramos apenas a variável inteira `N` para receber o valor ímpar fornecido.

```c
int N;
```

Conforme exemplificado no exercício, serão aplicados diversos casos de teste, continuamente lidos até que atinja-se o fim do arquivo (representado por `EOF`). Portanto, utilizamos a estrutura de repetição `while` para garantir que seja feita a leitura das entradas enquanto o arquivo não chegar ao fim.

```c
while(scanf("%d",&N) != EOF){
	...
}
```  

No interior desta estrutura, declaramos a matriz de tamanho NxN, assim como diversas variáveis inteiras. Neste momento, precisamos recorrer aos padrões identificadores. Ao observar as saídas desejadas pelo exercício, é possível notar que o ponto central encontra-se na posição (N/2) – prezando apenas pela parte inteira deste valor. Com o intuito de facilitar o desenvolvimento do código, declaramos então a variável `centro`, que armazena o resultado deste cálculo.
Como já fornecido pelo enunciado, a parte interna ["sempre começa na posição tamanho/3"]. Poranto, iremos guardar tal informação na variável `internoMin`. Todavia, também é importante identificarmos a posição em que esta termina e, por isso, declaramos `internoMax` para armazenar o cálculo '(N-1) - internoMin' (o tamanho deve ser subtraído de 1 em virtude das linhas e colunas iniciarem em 0 e terminarem em N-1).
Já `linha` e `coluna` servirão como auxiliares ao percorrermos a matriz.  

```c
int matriz[N][N];

int centro = N/2;
int internoMin = N/3;
int internoMax = (N-1) - internoMin;

int linha, coluna;
```  

Como primeiro passo, incluiremos o valor 1 em seu respectivo lugar. Portanto, necessitamos de duas estruturas de repetição `for` aninhadas: a externa percorre as linhas, enquanto a interna, as colunas. Isto deve ser feito iniciando-se na posição equivalente a `internoMin` e encerrando em `internoMax`, uma vez que estas variáveis armazenam os delimitadores da parte interna da matriz.  

```c
for(linha=internoMin; linha<=internoMax; linha++){
	for(coluna=internoMin; coluna<=internoMax; coluna++){
		matriz[linha][coluna] = 1;
	}
}
```  

Agora precisaremos caminhar por toda a matriz para preenchê-la com os demais valores. Dessa forma, utilizamos, novamente, os comandos `for` de modo aninhado; mas, desta vez, o caminho será de 0 até `N`.  

```c
for(linha=0; linha<N; linha++){
	for(coluna=0; coluna<N; coluna++){
		...
	}
}
```  

Uma vez que já temos os demarcadores internos determinados, podemos utilizá-los para percorrer a região externa a eles. Ainda neste raciocínio, trataremos, primeiro, de verificar se a linha atual encontra-se na região desejada. Para isto, recorremos à estrutura `if`, que selecionará os casos em que `linha` possui valor menor do que o delimitante inferior (`internoMin`) ou maior do que o superior (`internoMax`).
Em cenário positivo, averiguamos se a posição corresponde a diagonal principal (linha e coluna possuem mesmo valor, exemplo: [0][0], [1][1], etc) ou secundária (linha e coluna somadas equivalem ao tamanho da matriz – subtraído em 1 neste caso devido aos padrões da linguagem C já explicados em momento anterior), para a preenchermos com 2 ou 3, respectivamente. Neste mesmo contexto, se nenhuma destas duas situações forem aceitas, inserimos então o valor 0. Vale destacar que é imprescindível utilizar `if else` em cada uma das condições, visto que, caso uma seja cumprida, as demais não devem ser verificadas; ou seja, casa situação deve adequar-se a apenas uma condição.  

```c
if(linha<internoMin || linha>internoMax){
	if(linha == coluna){
		matriz[linha][coluna] = 2;

	}else if(linha+coluna == N-1){
		matriz[linha][coluna] = 3;

	}else{
		matriz[linha][coluna] = 0;
	}
}
```  

A estrutura `else` sucedente engloba o contexto em que a linha corrente não encontra-se fora da região interna. Neste caso, o `if` em seu interior verifica se então o valor da **coluna** equivale a uma posição na parte externa da matriz e, em caso afirmativo, este ponto conterá o número 0.  

```c
else{
	if(coluna<internoMin || coluna>internoMax){
		matriz[linha][coluna] = 0;
	}
}
```  

Em seguida, setamos a posição central (tanto `linha` como `coluna` são iguais a `centro`) como 4. Esta já foi acessada anteriormente ao preenchermos a região interna, mas será sobrescrita nesse momento.  

```c
matriz[centro][centro] = 4;
```  

Por fim, basta circularmos por toda a matriz novamente (através de dois `for` aninhados) para que a função `printf()` mostre na tela todos os seus valores e, com o intuito de exibi-los no formato adequado, inserimos um `\n` a cada final do `for` interno (representando a quebra para a próxima linha). Outro `\n` também deve ser adicionado ao final do comando externo, como solicitado na especificação da saída ["Após cada caso de teste, imprima uma linha em branco."].


##### Para aprender um pouco mais sobre fim de arquivos: [EOF](https://pt.wikipedia.org/wiki/EOF)

##### Para aprender um pouco mais sobre matrizes: [Matriz em C](http://linguagemc.com.br/matriz-em-c/)  

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso [Facebook](https://www.facebook.com/petbcc/), [Instagram](https://www.instagram.com/petbcc.ufscar/) ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
