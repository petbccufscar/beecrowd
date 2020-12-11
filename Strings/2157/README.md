# Problema:

Imprimir números em sequência é uma tarefa relativamente simples. Mas, e quando se trata de uma sequência espelho? Trata-se de uma sequência que possui um número de início e um número de fim, e todos os números entre estes, inclusive estes, são dispostos em uma sequência crescente, sem espaços e, em seguida, esta sequência é projetada de forma invertida, como um reflexo no espelho. Por exemplo, se a sequência for de 7 a 12, o resultado ficaria 789101112211101987.

Escreva um programa que, dados dois números inteiros, imprima a respectiva sequência espelho.

A entrada da sequência são número menores ou iguas a 12221.

**Problema completo:** https://www.urionlinejudge.com.br/judge/pt/problems/view/2157

# Resolução:

Para esse exercício a parte mais complexa é a parte de espelhar a sequência, já que a primeira parte é apenas mostrar a sequência de forma crescente. Para lidar com o espelhamento foi criado duas variáveis globais, que estão explicitas a baixo:

```c
int numSeparado[5];
int tamVet = 0;
```

A variável `numSeparado` é um vetor de cinco posições, pois é ele que receberá o número invertido, que é no máximo 12221, logo um número de até cinco dígitos, por isso de tamanho cinco o vetor. Em seguida temos `tamVet` que é quantas posições do vetor `numSeparado` estão ocupadas.

Em seguida tem a declaração e implementação da função que será responsável por inverter o número e colocar no vetor `numSeparado`, que é a funçaõ `inverteNum`.

```c
void inverteNum (int num) {
    int i = 0;
    .
    .
    .

```

Ela é uma função que não retorna nenhum valor, por isso `void` no tipo de retorno, e ela recebe um valor inteiro que é a entrada `num`, em seguida temos a declaração e atribuição da variável `i` em zero, ela será a vaiável responsável por indicar qual posição do vetor será inserido tal valor. Em seguida dessa declaração temos um `while`, que se encontra a seguir:

```c
    .
    .
    .
    while(num != 0) {  
        numSeparado[i] = num % 10;
        num /= 10;
        tamVet++;
        i++;
    }
}
```

A condição para o `while` parar é `num` ser igual a zero, em seguida temos a atribuição do vetor `numSeparado` na posição `i`, o valor a ser recebido é o resto da divisão de `num` por 10, dessa forma é colocado o último dígito de `num` na primeira posição de `numSeparado`. Para manter atualizado `num` é atribuído a ele o quociente inteiro entre ele mesmo e 10, assim fazendo com que o valor que foi anteriomante colocado em `numSeparado` não se repita. Em seguida é somado em `tamVet` e `i` mais um. 


Para mostrar o veotr `numSeparado` foi feita uma função chamada `exibirVetor` que não possui retorno e entrada, sua declaração e de sua única variável esta a baixo:

```c
void exibirVetor() {
  int i;
  .
  .
  .
```

A exibição do vetor está feita no próximo `for`:

```c
  for (i = 0; i < tamVet; i++) {
    printf("%i", numSeparado[i]);
  }
  tamVet = 0;
}
```
O laço de repetição esta iniciando em zero e indo até `tamVet` menos um, e dentro dele esta sendo mostrado posição a posição do `numSeparado`, com o fim do laço é atribuído a `tamVet`zero, pois caso não acontecesse isso, toda vez que `inverteNum` fosse chamada, `tamVet` estaria sendo incrementado de forma que ele extrapolaria o tamanha real de `numSeparado`, acarretando em erros de lógica.

Foi feita a função principal para este exercício, que é a `seqInverte` ela não possui retorno e suas entradas são dois inteiros, `ini` e `fim` que respectivamente são o início e fim da sequência a ser dada pelo usuário, sua declaração e variáveis se encontram a seguir:

```c
void seqInverte (int ini, int fim) {
    int numSeq = (fim - ini + 1) * 2;
    int i = 0;
    .
    .
    .

```

A variável `numSeq` contem quantos números a sequência terá, pois subtraindo `fim` e `ini`, e em seguida somando com mais um, temos quantos elementos tem entre o `ini` e `fim`, e multiplicando por dois resulta no tamanho total da sequência, afinal deve se espelhar a primeira parte. A variável `i` é um controlador para o laço que teremos e esta sendo inicializada em zero. Em seguida temos um `while` que esta descrito a seguir:

```c
    .
    .
    .

    while (i < numSeq) {
        if (ini <= fim) {
            printf("%i", ini);
            ini++;
        } else {
            inverteNum(fim);
            exibirVetor();
            fim--;
        }
        i++;
    }
}
```

O `while` vai até a quantidade `numSeq` menos um, dentro dele tem um `if` que compara se `ini` é menor ou igual a `fim`, se for verdade irá mostrar o valor de `ini` e em seguida somar mais um nele, caso não seja verdade o `else` esta chamando as funções `inverteNum` e `exibirVetor`, em seguida subtraimos um de `fim`, com esse condicional mostramos a parte crescente da sequência e depois a parte espelhada, e para atualizar o `i` somamos mais um a ele.

Para completar o exercício, foi feito na `main` a declaração das variáveis `quantSeq` que írá armazenar quantas sequências serão recebidas, `inicio` que é o primeiro valor da sequência, `fim` que é o último número da sequência e `i` que é um controlador para o laço que teremos, a baixo esta o código do trecho descrito:

```c
int main()
{
    int quantSeq, inicio, fim;
    int i;
    .
    .
    .

```
Em seguida foi feita a leitura de `quantSeq` e a criação de um `for` que vai rodar de `i` igual a zero até `quantSeq` menos um, dentro desse laço tem a leitura de `inicio` e `fim`, e a chamada de `seqInverte` que recebe `inicio` e `fim`, em seguida tem uma quebra de linha com um `printf`. Com isso encerramos o programa.

```c
    .
    .
    .
    scanf("%i", &quantSeq);
   
    for (i = 0; i < quantSeq; i++) {
        scanf("%i %i", &inicio, &fim);

        seqInverte(inicio, fim);
        printf( "\n");
    }

    return 0;
}
```

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com