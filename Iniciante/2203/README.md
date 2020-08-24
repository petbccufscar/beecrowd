# Problema:

Fiddlesticks é um campeão do jogo League of Legends e tem como sua habilidade ultimate a "Tempestade de Corvos", ela funciona da seguinte maneira:

Primeiro Fiddlesticks escolhe um local estratégico e prontamente ele se prepara para ressurgir em uma direção até uma certa distância, então ele se enraiza e canaliza a ultimate por exatamente 1.5 segundos, após esse tempo ele ressurge imediatamente no local alvo com uma revoada de corvos voando ao seu redor e causando muito dano.

Fiddlesticks quer sua ajuda para saber se de uma certa posição é possível atingir um invasor com sua habilidade ultimate.

Obs: Considere que Fiddlesticks sempre luta exatamente na direção do invasor e o invasor sempre tenta fugir na direção contrária a Fiddlesticks, em velocidade constante.

<img src="https://resources.urionlinejudge.com.br/gallery/images/problems/UOJ_2203.png" />


##### Link do problema: https://www.urionlinejudge.com.br/judge/pt/problems/view/2203
 
 
# Resolução:

O exercício possui alguns elementos de física e plano cartersiano e, apesar de apresentar muitas variáveis, não é tão complexo de se resolver. Primeiramente, vamos analisar o que é dado:
- Posição (X,Y) do campeão Fiddlesticks;
- Posição (X,Y) do inimigo;
- Velocidade do inimigo fugindo;
- Raio de alcance que o campeão pode realizar o ataque;
- Raio do ataque em si;
- O ataque leva 1.5 segundos para ser realizado (por isso a velocidade).

Para resolver o problema, precisamos:
- Calcular a distância atual entre os campeões;
- Somar a distância que o inimigo se afasta em 1.5 segundos;
- Verificar se essa distância está dentro dos raios de ataque.

Como o exercício vai utilizar funções de potenciação e raiz, começamos importando a biblioteca `math.h`, que contém essas e outras operações matemáticas mais complexas.

```c
#include <math.h>
```

Em seguida, declaramos as variáveis necessárias para o algoritmo ─ as entradas que o exercício fornece, do tipo inteiro, e as distâncias que vamos calcular, do tipo `double`.  
Note que (Xf,Yf) são coordenadas de Fiddlesticks e (Xi,Yi) são coordenadas do inimigo.
```c
int Xf, Yf, Xi, Yi, V, R1, R2;
double distancia, distX, distY;
```

O enunciado não deixa claro, mas devemos ler as entradas do exercício até que haja o fim de arquivo, ou seja, até o `EOF`. Para isso, colocamos a função `scanf()` dentro de uma estrutura `while()` e repetimos enquanto a entrada for diferente de `EOF`.

```c
while (scanf("%d %d %d %d %d %d %d", &Xf, &Yf, &Xi, &Yi, &V, &R1, &R2) != EOF) {

    /* calculos de distancia e exibicao na tela */

}
```
###### Sim, essa linha assusta, mas estamos apenas lendo dados (:

Para calcular a [distância](https://brasilescola.uol.com.br/matematica/distancia-entre-dois-pontos.htm) entre os dois campeões, vamos utilizar funções de potência e raiz ─ `pow()` e `sqrt()` ─  presentes na biblioteca `math.h`. Primeiro, calculamos as distâncias nos eixos X e Y, realizando a subtração de cada coordenada e elevando o resultado ao quadrado, ou seja, (Xi - Xf)² e (Yi - Yf)².

```c
distX = pow((Xi - Xf), 2);
distY = pow((Yi - Yf), 2);
```

Em seguida, tiramos a raiz entre a soma das duas distâncias obtidas no passo anterior.

```c
distancia = sqrt(distX + distY);
```

Sabemos qual a distância entre os campeões, mas precisamos adicionar o espaço que o inimigo vai andar em 1.5 segundos. Para isso, vamos aplicar uma fórmula de [movimento uniforme](https://www.sofisica.com.br/conteudos/Mecanica/Cinematica/mu.php):
```
ΔS = V * Δt
```
Sendo que:  
`V` = (valor dado pelo exercício)  
`Δt` = 1.5  

```c
distancia += V * 1.5;
```

Dessa forma, podemos descobrir se a _Tempestade de Corvos_ vai atingir o inimigo ou não. Pensando que o campeão pode marcar o ataque no limite de seu alcance e que o ataque também possui seu próprio raio, concluímos que se a `distancia` está dentro da soma dos raios (ou seja, é menor ou igual à soma), é possível atingir o inimigo. Nesse caso, exibimos `Y` na tela. Caso não seja possível, exibimos `N`.

```c
if (distancia <= (R1 + R2)) {
    printf("Y\n");
} else {
    printf("N\n");
}
```

Lembre-se que este código é repetido inúmeras vezes dentro do `while()`, até que o arquivo de entrada do URI chegue ao fim com `EOF`.


##### Para aprender um pouco mais sobre fim de arquivos: [EOF](https://pt.wikipedia.org/wiki/EOF)
##### Para revisar as funções da biblioteca math.h: [Biblioteca math.h](http://linguagemc.com.br/a-biblioteca-math-h/)
##### Para revisar o conceito de distância em planos cartesianos: [Distância entre dois pontos](https://brasilescola.uol.com.br/matematica/distancia-entre-dois-pontos.htm)


Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com