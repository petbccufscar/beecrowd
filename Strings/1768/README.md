# Problema

O exercicío 1768 pede a elaboração de um algoritmo que construa árvores de natal utilizando asteriscos (*), o modo que elas serão construidas, é de cima para baixo, começando com um asterisco e aumentando em dois a proxima linha até que a última linha tenha n asteriscos, ao fim das folhas tem que desenhar o tronco da árvore que possui um asterisco e três na sequencia. A entrada do problema é n, que poderá ter várias entradas até que se encontre o valor `EOF`. Um exemplo de como deve ser a árvore, em que n é igual a nove:

```c
    *
   ***
  *****
 *******
*********
    *
   ***
```

# Resolução

Para começar o código, foi implementada a primira função que é a `repetirCar`, ela não possui retorno assim como as demais funções deste código, então é do tipo `void`, suas entradas são um inteiro (`int`) `n` e um caracter (`char`) `c`, seu objetivo é repetir `c`, `n` vezes e como pode ser observado na seguinte declação da mesma, é utilizado um `for` que vai de zero até `n` menos um.

```c
void repetirCar(int n, char c) {
  int i;
  for(i = 0; i < n; i++) {
    printf("%c", c);
  }
}
```

A próxima função foi a `baseArvore` que faz a exibição na tela da base da árvore, ela possui uma entrada inteira `n`, que dessa forma, somos capazes de chamar a função `repetirCar` passando `n` e `' '` (espaço em branco) para alinhar o primeiro asterisco, logo o mostrando, e refazendo isso, mas no lugar de passar `n` na entrada de `repetirCar` passamos `n - 1` para o desenhar o final da base, pois ele contem três asteriscos, dessa forma o alinhamos com o restante da árvore. A seguir a função citada:

```c
void baseArvore(int n) {
  repetirCar(n, ' ');
  printf("*\n");
  repetirCar(n - 1, ' ');
  printf("***\n\n");
}
```

Em seguida temos a função que vai desenhar a árvore de natal, que é a `desenArvore` ela tem uma entrada inteira `n`, e possui duas variáveis `i` e `quantEsp`, respectivamente uma é o contador do laço que teremos e a outra é a quantidade de espaços em branco que tem que ter antes de mostrar os asteriscos, isso que faz a árvore ficar alinhada, em seguida atribuímos a `quantEsp` o valor de `n`, fazemos isso para atualizar `n` sem que percamos o valor original.

Temos então a inicialização do `for` que começará em um e irá até `n` menos um, o `i` terá seu valor acrescido de dois em dois. Dentro do laço temos `repetirCar` sendo chamado primeiramente para colocar os espaços em brancos, ou seja esta recebendo `quantEsp` divido por dois e `' '` (espaço em branco), em seguida chamamos novamente a mesma função para agora exibir os asteriscos, assim passamos `i`, pois como o desenho da árvore começa do topo com um asterisco e vai descendo e aumentando esse número de dois em dois `i` contém a característica que necessitamos, e passamos astericos como segundo parâmetro, temos um `printf` que faz uma quebra de linha usando um `\n` e subtraímos em dois `quantEsp`, depois do laço chamamos `baseArvore` que esta recebendo `n` dividio por dois, porque é o valor que se encontra o meio da árvore. A baixo temos a função descrita:

```c
void desenArvore(int n) {
    int i, quantEsp;

    quantEsp = n;

    for(i = 1; i <= n; i += 2) {
      repetirCar(quantEsp/2, ' ');
      repetirCar(i, '*');
      printf("\n");

      quantEsp -= 2;
    }

    baseArvore(n/2);
}
```

Finalizando o problema, temos a `main`, que possui uma variável que é a `entrada`, ela indica a entrada do usuário, e o laço que irá parar se a entrada for `EOF`. `EOF` é End of File, geralemnte é uma informação bem utilizada quando se trabalha com arquivos indicando o final dele, uma forma de identificá-lo é por meio de um `scanf`, que é a condição que se encontra no laço de repetição, dentro dele tem a chamada de `desenArvore` que recebe a `entrada`, com isso fanalizamos o problema.

```c
int main(){
    int entrada;

    while(scanf("%d", &entrada) != EOF) {
      desenArvore(entrada);
    }

    return 0;
}
```

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso [Facebook](https://www.facebook.com/petbcc/), [Instagram](https://www.instagram.com/petbcc.ufscar/) ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com