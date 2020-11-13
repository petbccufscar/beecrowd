# Problema:

Seu professor de português não para de trazer coisas novas para a sala, e hoje não foi diferente. Existe uma cidade, segundo seu professor, onde as pessoas levam muito a sério a forma como elas se comunicam. Em especial, quando duas pessoas estão conversando, elas pensam muito nas frases antes de dizê-las, de forma a garantir que tal frase seja uma “frase completa”, ou talvez uma “frase quase completa”.

Considerando o nosso alfabeto de 26 letras, uma frase é dita “completa” quando ela contém todas as letras do alfabeto contidas nela. De modo semelhante, uma frase é dita “quase completa” se ela não é completa, porém contém ao menos metade das letras do alfabeto contidas nela. Quando uma frase não é “completa” e nem “quase completa”, ela é dita “mal elaborada”.

Seu professor lhe deu uma tarefa muito difícil: dadas várias frases trocadas entre vários habitantes da cidade citada, diga em qual das categorias acima a frase se encaixa.

##### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/1551

# Resolução:

O objetivo desse exercício é criar um programa que leia `n` frases e escreva se ela é uma frase “completa”, “quase completa” ou “mal elaborada”.

Vamos usar seis variáveis, em que cinco são do tipo `int` e uma é do tipo `char`:
```c
  int n, contador, i, j;
  int alfabeto[26];
  char frase[1001];
```
`n` representa quantos frases serão categorizadas. `contador` indica quantas letras diferentes foram usadas na frase. `i` e `j` são variáveis auxiliares para a estrutura `for`. `alfabeto` é um vetor de `int` que vai indicar se uma determinada letra está presente na frase. `frase` é uma string que representa a frase que vai ser analisada.

Precisamos saber quantos casos de teste vão ser realizados. Para isso, vamos usar um `scanf` para ler `n`:
```c
  scanf("%d", &n);
```
Para poder categorizar as frases, temos que garantir que uma mesma letra não seja considerada duas vezes na frase. Para isso criamos o vetor `alfabeto`. Esse vetor possui 26 posições, cada uma representando uma letra (a 1ª posição do vetor representa a letra "a", a 2ª posição do vetor representa a letra "b" etc.). Os valores nesse vetor serão 0, se a letra não estiver na frase, ou 1, se estiver. Para inicializar esse vetor atribuímos 0 a todas as posições de `alfabeto`:
```c
  for(i = 0; i < 26; i++)
    alfabeto[i] = 0;
```
Feito isso, podemos começar a leitura e categorização das frases. Vamos criar um laço de repetição `for` para fazer `n` testes:
```c
  for(i = 0; i < n; i++) {
    contador = 0;
    scanf(" %1001[^\n]", frase);
```
Igualamos `contador` a 0 e lemos a string `frase`. `%1001[^\n]` significa que a leitura da variável será feita até a presença de um `\n` ou até chegar a 1001 caracteres. Com a `frase`, vamos verificar quais letras estão presentes nessa frase usando outro `for`:
```c
    for(j = 0; j < strlen(frase); j++) {
      if (frase[j] >= 'a' && frase[j] <= 'z')
        if (alfabeto[frase[j] - 'a'] == 0)
          alfabeto[frase[j] - 'a'] = 1;
    }
```
Aqui usamos a função `strlen` da biblioteca [string.h](http://linguagemc.com.br/a-biblioteca-string-h/) para determinar o tamanho da string `frase`. Na iteração usamos dois `if`:
* O primeiro `if` verifica se o caractere escrito é uma letra minúscula do alfabeto (`frase[j] >= 'a' && frase[j] <= 'z'`). Se for, podemos verificar a condição do segundo `if`.
* O segundo `if` verifica se essa é a primeira vez que a letra aparece na string (`alfabeto[frase[j] - 'a'] == 0`). Se for, atribuímos 1 na posição que representa a letra presente em `frase[j]` no vetor `alfabeto`. Note que dentro dos colchetes está escrito uma subtração entre `frase[j]` e `'a'`, que são valores do tipo `char`. Nesse caso a subtração é feita utilizando o valor decimal da [tabela ASCII](https://pt.wikipedia.org/wiki/ASCII) que representa o caractere.

Depois de verificar todos os caracteres de `frase`, vamos contar quantas letras diferentes estão na string. Criamos um `for` e, para cada valor 1 presente em `alfabeto`, incrementamos `contador` e igualamos `alfabeto[j]` a 0, para usar o vetor na próxima verificação:
```c
    for(j = 0; j < 26; j++) {
      if (alfabeto[j] == 1) {
        contador++;
        alfabeto[j] = 0;
      }
    }
```
Para finalizar a categorização da frase, vamos escrever se ela é completa, quase completa ou mal elaborada. Se a frase tiver menos de 13 letras diferentes (`contador < 13`), mostramos na tela a mensagem `frase mal formulada`. Se tiver entre 13 e 25 letras (`contador < 26`), mostramos a mensagem `frase quase completa`. Se tiver todas as letras do alfabeto, a resposta será `frase completa`:
```c
    if (contador < 13)
      printf("frase mal elaborada\n");
    else if (contador < 26)
      printf("frase quase completa\n");
    else
      printf("frase completa\n");
  }
```

##### Para aprender um pouco mais sobre vetores: [Vetores](http://linguagemc.com.br/vetores-ou-arrays-em-linguagem-c/)
##### Para aprender um pouco mais sobre a estrutura for: [For](http://linguagemc.com.br/a-estrutura-de-repeticao-for-em-c/)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
