# Problema:
Durante sua última viagem, Dona Ricota comprou 2n presentes para seus n netos. Cada presente custou x reais (1 ≤ i ≤ 2n) e, para evitar conflitos, ela planeja formar os pares de presentes de modo a minimizar a diferença entre o valor total do par de presentes mais caro e o valor total do par mais barato.

Como você é uma pessoa gentil, Dona Ricota resolveu pedir sua ajuda para organizar os presentes.

##### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/3089

# Resolução:

Nesse exercício temos que responder qual o par de presentes mais caro e o mais barato. Os preços dos presentes serão escritos em ordem decrescente.

Precisamos de um vetor do tipo `int` de tamanho maior que 20000. Como é um vetor muito grande precisamos criar o vetor como uma variável global, ou seja, antes do `int main()`:
```c
int presente[20001];
```
`presente` vai guardar os preços dos presentes dados.

Além do vetor, vamos criar quatro variáveis locais do tipo `int`:
```c
  int n, maior, menor, i;
```
`n` é um valor que representa o número de crianças. `maior` e `menor` são variáveis que vão guardar o par mais caro e o par mais barato de presentes, respectivamente. `i` é uma variável auxiliar para o `for`.

O exercício aborda um caso de leitura em que deve ser lido até `n` ser 0. Para isso usaremos o laço de repetição `while`:
```c
  while (n != 0) {
```
Agora, descobrimos quantos presentes serão dados lendo o valor de `n` com o `scanf`:
```c
    scanf("%d", &n);
```
Como cada criança receberá dois presentes, então fazemos um `for` de 0 a `2*n` para ler o preço de cada presente:
```c
    for(i = 0; i < 2*n; i++)
      scanf("%d", &presente[i]);
```
Todos os valores ficarão guardados no vetor `presente`. Vale lembrar que nesse exercício os valores estarão em ordem decrescente. Sabendo disso, cada criança vai receber o presente mais caro e o mais barato que ainda não foram entregues:
```c
    maior = presente[0] + presente[2*n-1];
    menor = presente[0] + presente[2*n-1];
```
Começamos atribuindo o mesmo valor para `maior` e `menor` para poder comparar o preço desse par com as outras somas. Para poder comparar os outros pares de presentes será usado o `for`:
```c
    for(i = 1; i < 2*n - 1; i++) {
      if (presente[i] + presente[2*n-1-i] > maior)
        maior = presente[i] + presente[2*n-1-i];
      if (presente[i] + presente[2*n-1-i] < menor)
        menor = presente[i] + presente[2*n-1-i];
```
Na repetição comparamos a soma dos presentes mais caro e mais barato que ainda não foram somados e comparamos o valor obtido com `maior` e `menor`. Se o valor for maior que o `maior` (`presente[i] + presente[2*n-1-i] > maior`) ou menor que o `menor` (`presente[i] + presente[2*n-1-i] < menor`) atualizamos a variável.

Depois de comparar todos os pares de presentes, escrevemos o resultado na tela usando `printf`. Como `n = 0` é o caso para encerrar o programa, nenhum resultado deve ser mostrado se `n` for 0:
```c
    if (n != 0)
      printf("%d %d\n", maior, menor);
  }
```
##### Para aprender um pouco mais sobre vetores: [Vetores](http://linguagemc.com.br/vetores-ou-arrays-em-linguagem-c/)
##### Para aprender um pouco mais sobre a estrutura for: [For](http://linguagemc.com.br/a-estrutura-de-repeticao-for-em-c/)
##### Para aprender um pouco mais sobre a estrutura while: [While](http://linguagemc.com.br/o-comando-while-em-c/)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
