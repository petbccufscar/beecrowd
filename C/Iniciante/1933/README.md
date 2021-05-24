# Problema:
Tri-du é um jogo de cartas derivado do popular jogo de Truco. O jogo utiliza um baralho normal de 52 cartas, com treze cartas de cada naipe, mas os naipes são ignorados. Apenas o valor das cartas, considerados como inteiros de 1 a 13, são utilizados.

No jogo, cada jogador recebe três cartas. As regras são simples:

Um trio (três cartas de mesmo valor) ganha de uma dupla (duas cartas de mesmo valor).
Um trio formado por cartas de maior valor ganha de um trio formado por cartas de menor valor.
Uma dupla formada por cartas de maior valor ganha de uma dupla formada por cartas de menor valor.
Note que o jogo pode não ter ganhador em muitas situações; nesses casos, as cartas distribuídas são devolvidas ao baralho, que é embaralhado e uma nova partida é iniciada

Um jogador já recebeu duas das cartas que deve receber, e conhece seus valores. Sua tarefa é escrever um programa para determinar qual o valor da terceira carta que maximiza a probabilidade de esse jogador ganhar o jogo.

**Problema Completo**: https://www.urionlinejudge.com.br/judge/pt/problems/view/1933


# Resolução:
O ponto chave deste exercício consiste em analisar as regras fornecidas. A partir delas, notamos que um trio de cartas é mais vantajoso do que uma dupla; assim como, no caso de ambos jogares possuírem um trio (ou dupla), é almejado dispor dos maiores valores.

Iniciamos a resolução declarando as variáveis inteiras a serem utilizadas: `A` e `B`, que representam as duas primeiras cartas recebidas; e `terceiraCarta`, como sendo aquela que maximiza a probabilidade de vitória.  

```c
int A, B, terceiraCarta;
```  

Como próximo passo, realizamos a leitura do valor de cada uma das duas cartas recebidas, armazenando-os em `A` e `B` através da função `scanf()`.  

```c
scanf("%d %d",&A,&B);
```  

Visto que o melhor cenário possível corresponde a três cartas iguais, iremos, como primeira opção, verificar se é possível obtê-lo: utilizamos a estrutura condicional `if` para analisar se os inteiros `A` e `B` possuem mesmo valor. Em caso afirmativo, basta determinar que `terceiraCarta` equivale a um deles (no caso, atribui-se `A`, mas `B` seria igualmente correto).  

```c
if(A == B)
  terceiraCarta = A;
```  

Em caso negativo (ou seja, não são iguais), devemos, então, garantir que haja uma dupla. Portanto, é preciso averiguar qual das cartas já fornecidas é maior, para que aumentemos as chances de vencer ao apostar em uma dupla de alto valor. Dessa forma, a estrutura `else` conterá, em seu escopo, dois comandos `if`: o primeiro representa a situação em que `A` é maior e, assim, a terceira carta conterá o seu valor; já o segundo indica que `B` é o maior inteiro dentre os dois, e `terceiraCarta` será atribuída como este.  

```c
else{
  if(A>B)
    terceiraCarta = A;
  if(B>A)
    terceiraCarta = B;
}
```  

Por fim, basta que `terceiraCarta` seja exibida na tela com `printf()`.  

```c
printf("%d\n",terceiraCarta);
```


##### Para aprender um pouco mais sobre a estrutura condicional: [O teste condicional IF ELSE](https://www.cprogressivo.net/2013/01/O-testecondicional-IF-ELSE.html)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso [Facebook](https://www.facebook.com/petbcc/), [Instagram](https://www.instagram.com/petbcc.ufscar/) ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
