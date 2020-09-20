# Problema:
Papai Noel adora jogos de celular, especialmente se forem com temas natalinos. Ele acaba de instalar um novo jogo para seu celular. O jogo consiste em um personagem correndo infinitamente em um caminho composto de três pistas, tendo que trocar de pista para desviar de obstáculos (árvores de natal) que aparecem no caminho. O personagem sempre começa um jogo na pista do meio, sendo necessário que Papai Noel toque uma vez do lado esquerdo da tela do celular para o personagem se deslocar uma pista para a esquerda e um toque do lado direito da tela para se deslocar uma pista para o lado direito. Ou seja, se o personagem estiver na pista mais à esquerda, precisará de 2 toques do lado direito para chegar até a pista mais à direita.
Apesar de parecer simples, Papai Noel está tendo dificuldades em permanecer vivo por muito tempo. Uma coisa que ele notou durante o jogo é que, sempre que há obstáculos, somente uma das pistas está livre para atravessar, enquanto que as outras duas possuem árvores de natal bloqueando os caminhos. Como vocês são grandes amigos, ele pediu sua ajuda para escrever um programa que minimize o número de toques necessários na tela para que ele consiga percorrer M metros no jogo.

**Problema Completo**: https://www.urionlinejudge.com.br/judge/pt/problems/view/3042


# Resolução:
O ponto chave deste exercício é compreender todos os possíveis cenários. Há o caso em que todos os caminhos estão livres e, se isto não ocorrer, 2 pistas (necessariamente) conterão árvores, existindo apenas uma opção viável. Portanto, trabalharemos com possibilidades.  

Como sugerido pelo enunciado, declaramos a variável inteira `M`, correspondendo à distância a ser percorrida; assim como `L`, `C` e `R`, representando as pistas esquerda, central e direita, respectivamente. Também precisaremos dos inteiros `numToques`, `posicao` e `i`; responsáveis por armazenar a quantidade de toques realizados, a posição corrente do personagem e a iteração atual do loop. Vale destacar que a posição será representada da seguinte maneira: 0 indica que o personagem encontra-se no centro; enquanto 1 significa que está na pista da esquerda e 2, na da direita.  

```c
int M, L, C, R;
int numToques, posicao, i;
```  

Podemos, então, fazer a leitura de quantos metros serão percorridos. Logo em seguida, utilizamos a estrutura de repetição `while` para garantir que os procedimentos serão executados enquanto a distância lida por diferente de zero (indicador de final da entrada).  

```c
scanf("%d",&M);

while(M != 0){
  ...
}
```  

No interior do `while` realizamos toda a lógica do exercício. Primeiramente, inicializamos `posicao` e `numToques` como zero, pois o jogo começa na pista do meio e, neste momento, nenhum toque foi preciso.  

```c
  posicao = 0;
  numToques = 0;
```  

O loop `for` será importante para garantir a leitura das próximas `M` linhas de entrada, indicando a situação do jogo a cada metro percorrido. Portanto, em seu escopo, o primeiro passo consiste em realizar a leitura das informações de cada pista, armazenando-as em `L`, `C` e `R`.  

```c
  for(i=1; i<=M; i++){
    scanf("%d %d %d", &L, &C, &R);
    ...
  }
```  

Agora podemos tratar cada uma das possíveis situações, utilizando diversas vezes a condicional `if`. Começamos pelo caso em que o personagem encontra-se na esquerda, ou seja, `posicao` contém o valor 1. Se isto ocorrer, devemos analisar se o metro seguinte possui uma árvore nesta pista (a entrada fornecida contém 1 na variável `L`). Em cenário positivo e, considerando que, necessariamente, 2 dos 3 caminhos possíveis terão uma árvore, devemos nos preocupar apenas com duas possíveis situações:  
- a pista central também contém uma árvore e, assim, devemos realizar dois toques (`numToques` incrementado em 2) para migrar da pista da esquerda para a direita (`posicao` atualizada para 2);  
- a pista direita é a que também contém uma árvore e, desse modo, apenas um toque (`numToques` incrementado em 1) é suficiente para nos direcionarmos a pista central — única livre (`posicao` passa a ser igual a 0).  

```c
    if(posicao == 1){

      if(L == 1){

        if(C == 1){
          numToques = numToques + 2;
          posicao = 2;
				}

				if(R == 1){
          numToques = numToques + 1;
          posicao = 0;
				}
			}

    }
```  

O mesmo pode ser feito para o caso em que o personagem encontra-se no centro, ou seja, `posicao` contém o valor 0. Precisaremos, então, verificar se haverá uma árvore nesta posição e, caso positivo, apenas 2 cenários poderão alterar a localização do personagem:  
- a pista da esquerda também contém uma árvore e precisaremos nos deslocar para a direita (`numToques` incrementado em 1 e `posicao` atualizada para 2);
- a pista da direita é a que contém a outra árvore e, então, nos movimentamos para a esquerda.  

```c
    if(posicao == 0){

      if(C == 1){

        if(L == 1){
          numToques = numToques + 1;
          posicao = 2;
        }

        if(R == 1){
          numToques = numToques + 1;
          posicao = 1;
        }

      }
    }
```  

Se a posição atual corresponder a pista da direita (`posicao` contém o valor 2), o procedimento será muito parecido com o caso em que encontrava-se na esquerda, apenas realizando certas mudanças pontuais.  

```c
    if(posicao == 2){

      if(R == 1){

        if(L == 1){
          numToques = numToques + 1;
          posicao = 0;
        }

        if(C == 1){
          numToques = numToques + 2;
          posicao = 1;
        }

      }
    }
```  

Após a conclusão de todas as iterações do `for`, podemos exibir a saída contendo o número de toques que foram necessários para aquela rodada. Em seguida, é importante que a leitura da entrada seja feita novamente, para possibilitar a análise desta no próximo loop da estrutura `while` (se for 0, o programa encerra-se; caso contrário, todo o ciclo se inicia novamente).  

```c
  printf("%d\n",numToques);

  scanf("%d",&M);
```  


Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso [Facebook](https://www.facebook.com/petbcc/), [Instagram](https://www.instagram.com/petbcc.ufscar/) ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
