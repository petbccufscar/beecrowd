# Problema:
Depois de capturar muitos Pomekons, Dabriel e Guarte resolveram batalhar. A forma de duelo é simples, cada treinador coloca um Pomekon na batalha e vence quem tem o Pomekon com maior valor de golpe, que é definido da seguinte maneira:
<img src="https://resources.urionlinejudge.com.br/gallery/images/problems/UOJ_2221.png"/>
O Bônus será dado ao Pomekon do treinador que estiver em um level de valor par.

Neste problema será dado a você o valor do bônus aplicado, os valores de ataque e defesa do Pomekon de Dabriel e Guarte e seus respectivos níveis, cabe a você informar o ganhador da batalha.

**Problema Completo**: https://www.urionlinejudge.com.br/judge/pt/problems/view/2221


# Resolução:
O exercício consiste, basicamente, em utilizar a fórmula disponibilizada para comparar quais dos dois jogadores obteve maior resultado.  

Iniciamos declarando todos os inteiros necessários: variáveis `T` e `B`, representando a quantidade de instâncias e o valor do bônus, respectivamente; vetores `A`, `D`, `L` e `Golpe`, de tamanho 2, para que armazenem ataque/defesa/nível/golpe resultante do Pomekon de Dabriel, na primeira posição do array, e de Guarte, na segunda. `i` servirá como auxílio para a estrutura de repetição a ser utilizada.  
Após tais declarações, podemos realizar a leitura do número de instâncias a serem concedidas, armazenando tal quantia em `T` através da função `scanf()`

```c
int T, B;
int A[2], D[2], L[2], Golpe[2];
int i;

scanf("%d",&T);
```  

Usufruímos, então, do comando `for`, para tratar os inputs de cada instância. A iteração será feita de acordo com o número contido em `T` e, em cada laço, realizará, primeiramente, a leitura dos dados, armazenando-os corretamente de acordo com a ordem definida pelo enunciado. Portanto, as 3 funções `scanf()` tratarão separadamente as linhas da entrada, em que a primeira corresponde ao valor do bônus; a segunda aos dados do Pomekon de Dabriel; e a terceira, aos de Guarte.  

```c
for(i = 1; i <= T; i++) {
  scanf("%d",&B);
  scanf("%d %d %d",&A[0], &D[0], &L[0]);
  scanf("%d %d %d",&A[1], &D[1], &L[1]);
  ...
}
```  

Tendo todos os valores em mãos, podemos iniciar o cálculo do golpe de cada um dos Pomekons da jogada. Assim, a posição 0 do vetor `Golpe` conterá o resultado obtido por Dabriel; enquanto a posição 1, o obtido por Duarte.  

```c
  Golpe[0] = (A[0] + D[0]) / 2;
  Golpe[1] = (A[1] + D[1]) / 2;
```  

Em seguida, é importante verificarmos se algum dos jogadores possuem o requisito necessário para receber a bonificação. Deste modo, a estrutura condicional `if` verifica se o level em questão é par (ou seja, o resto da divisão de `L` por 2 equivale a 0) e, em caso positivo, soma-se `B` ao valor já contido em `Golpe` do jogador correspondente.  

```c
if(L[0]%2 == 0)
  Golpe[0] = Golpe[0] + B;

if(L[1]%2 == 0)
  Golpe[1] = Golpe[1] + B;
```  

Agora, podemos aplicar a função `printf()` para imprimir o desfecho da jogada. Para isto, usufruímos, novamente, do comando `if` para verificar se os golpes resultantes de Dabriel e Guarte possuem mesmo valor. Neste caso, imprimimos 'Empate!'.  

```c
if(Golpe[0] == Golpe[1])
  printf("Empate\n");
```  

Se não forem iguais, `else` direciona à outra estrutura condicional, com o intuito de analisar qual posição do vetor `Golpe` armazena o maior valor. Se for a posição 0 (correspondente ao Pomekon de Dabriel), exibimos 'Dabriel' na tela. Se não, exibe-se 'Guarte'.  

```c
else {

  if(Golpe[0] > Golpe[1])
    printf("Dabriel\n");
  else
    printf("Guarte\n");

		}
```  


##### Para aprender um pouco mais sobre vetores: [Arrays em linguagem C](http://linguagemc.com.br/vetores-ou-arrays-em-linguagem-c/)  

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso [Facebook](https://www.facebook.com/petbcc/), [Instagram](https://www.instagram.com/petbcc.ufscar/) ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
