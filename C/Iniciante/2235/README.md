# Problema:
Imagine que você tenha uma máquina do tempo que pode ser usada no máximo três vezes, e a cada uso da máquina você pode escolher voltar para o passado ou ir para o futuro. A máquina possui três créditos fixos; cada crédito representa uma certa quantidade de anos, e pode ser usado para ir essa quantidade de anos para o passado ou para o futuro. Você pode fazer uma, duas ou três viagens, e cada um desses três créditos pode ser usado uma vez apenas. Por exemplo, se os créditos forem 5, 12 e 9, você poderia decidir fazer duas viagens: ir 5 anos para o futuro e, depois, voltar 9 anos para o passado. Dessa forma, você terminaria quatro anos no passado, em 2012. Também poderia fazer três viagens, todas indo para o futuro, usando os créditos em qualquer ordem, terminando em 2042.

Neste problema, dados os valores dos três créditos da máquina, seu programa deve dizer se é ou não possível viajar no tempo e voltar para o presente, fazendo pelo menos uma viagem e, no máximo, três viagens; sempre usando cada um dos três créditos no máximo uma vez.

**Problema Completo**: https://www.urionlinejudge.com.br/judge/pt/problems/view/2235


# Resolução:
Neste problema, analisaremos os valores fornecidos para concluirmos se é possível viajar no tempo e retornar ao presente. Para que isto ocorra, é necessário que 2 dos 3 créditos sejam equivalentes; ou que a soma de 2 quaisquer resulte no terceiro crédito.  

Como primeiro passo, declaramos as variáveis inteiras `A`, `B` e `C` para armazenarem, através da leitura com `scanf()`, as quantias concedidas.  

```c
int A, B, C;
scanf("%d %d %d",&A, &B, &C);
```  

Em seguida, verificamos se o primeiro caso é atendido: aplica-se a estrutura condicional `if` para realizar a comparação, aos pares, da quantia armazenada em cada variável. Desse modo, a condição será cumprida se `A` contiver mesmo valor que a `B` ou `C`; ou se `B` equivaler a `C`. Desse modo, averiguamos se existe algum par de créditos iguais e, em caso positivo, imprime-se 'S'.  

```c
if(A == B || A == C || B == C)
  printf("S\n");
```  

Se este cenário não ocorrer, `else` analisará o outro caso possível. Em seu escopo, a estrutura `if` verifica se as somas de 2 créditos corresponde ao terceiro (utilizando o operador lógico 'ou': `||`) e, então, exibe 'S'. Em situação contrária, `else` imprime 'N'.  

```c
else {
  if( (A+B == C) || (A+C == B) || (B+C == A))
    printf("S\n");
  else
    printf("N\n");
}
```  


##### Para aprender um pouco mais sobre operadores lógicos: [Operadores Lógicos em C](http://linguagemc.com.br/operadores-logicos-em-c/)  

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso [Facebook](https://www.facebook.com/petbcc/), [Instagram](https://www.instagram.com/petbcc.ufscar/) ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
