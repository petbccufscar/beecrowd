# Problema:

E aí, preparado? Mais uma vez precisamos da sua ajuda! Depois de algumas trocas de aparelhos, e manutenções no prédio da informática, os teclados do IF (IFSULDEMINAS) sofreram uma brincadeira de mau gosto na formatação do teclado, suas teclas estão trocadas. Como os computadores do IF são preparados para receber qualquer software, desenvolva o mais rápido possível um programa que converta as frase da forma correta.

Observação: o teclado trocará todas as teclas do teclado, por isso todos os caracteres são aceitos.

##### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/2692

# Resolução:

Nesse exercício vamos criar um programa que leia `m` frases e substitua os caracteres de acordo com a teclas que foram trocadas.

Vamos criar iniciamente sete variáveis, sendo seis do tipo `int` e uma do tipo `char`:
```c
  int n, m, achou, i, j, k;
  char frase[1000];
```
`n` representa o número de teclas trocadas. `m` indica o número de frases que serão modificadas. `achou` é uma variável que vai ser usada na busca dos caracteres trocados na frase. `i` e `j` são variáveis auxiliar para a estrutura `for`. `k` é uma variável auxiliar para a estrutura `while`. `frase` é uma string que representa a frase que será enviada.

Para começar o exercício, precisamos saber os valores de `n` e `m`. Vamos usar um `scanf`:
```c
  scanf("%d %d", &n, &m);
```
Sabendo que `n` letras foram trocadas, criamos um vetor de caracteres `troca`, de tamanho `2n`. Esse vetor vai guardar a tecla trocada e sua substituta, respectivamente: 
```c
  char troca[2*n];
```
Feito isso, vamos usar um laço de repetição `for` e, a cada iteração usamos um `scanf` para ler as letras que foram trocadas e quais são suas substitutas:
```c
  for(i = 0; i < 2*n; i+= 2)
    scanf(" %c %c", &troca[i], &troca[i+1]);
```
Usamos `i+=2` porque em uma única iteração lemos dois valores do vetor. Agora que sabemos quais letras foram trocadas, vamos fazer um `for` que vai ler e arrumar `m` frases:
```c
  for(i = 0; i < m; i++) {
    scanf(" %1000[^\n]", frase);
```
`%1000[^\n]` significa que a leitura da variável será feita até a presença de um `\n` ou até chegar a 1000 caracteres. Com a `frase` lida, começamos um novo `for` para verificar todos os caracteres de `frase`:
```c
    for(j = 0; j < strlen(frase); j++) {
      achou = 0;
      k = 0;
```
Aqui usamos a função `strlen` para determinar o tamanho da string `frase`. Para garantir que vamos encontrar o caractere trocado na frase, igualamos `achou` e `k` a 0. Temos que comparar `frase[j]` com cada elemento do vetor `troca` e, se forem iguais, devemos trocar a letra da string `frase` pela letra certa:
```c
      while (achou == 0) {
        if (troca[k] == frase[j]) {
          achou = 1;
          if (k%2 == 0)
            frase[j] = troca[k+1];
          else
            frase[j] = troca[k-1];
        }
        else if (k == 2*n-1)
          achou = 1;
        k++;
      }
    }
```
Se `frase[j]` for igual a `troca[k]`, igualamos `achou` a 1 e verificamos se a letra está em uma posição par (`k%2 == 0`). Se estiver, trocamos `frase[j]` por `troca[k+1]`, senão, trocamos por `troca[k-1]`. É possível que o caractere `frase[j]` não seja encontrado em `troca`, isso significa que a letra está correta e não precisa se trocada, sendo assim igualamos `achou` a 1 para sair da repetição.

Depois de verificar todos os caracteres da string, vamos mostrar o resultado na tela usando `printf`:
```c
    printf("%s\n", frase);
  }
```

##### Para aprender um pouco mais sobre vetores: [Vetores](http://linguagemc.com.br/vetores-ou-arrays-em-linguagem-c/)
##### Para aprender um pouco mais sobre a estrutura for: [For](http://linguagemc.com.br/a-estrutura-de-repeticao-for-em-c/)
##### Para aprender um pouco mais sobre a estrutura while: [While](http://linguagemc.com.br/o-comando-while-em-c/)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
