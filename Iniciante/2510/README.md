# Problema:

Como todos sabem, existem diversos heróis que defendem a humanidade de capangas e forças do mal. Em Codham, uma das cidades mais sombrias que existem, vive Batmain, o cavaleiro das trevas. Após diversas batalhas, todos os seus vilões haviam sido capturados pelo Batmain e a sensação de segurança parecia fazer parte dos cidadãos de Codham novamente. Você trabalha para a polícia de Codham, em um reconhecido cargo de batprogramador e lhe foi solicitado a seguinte tarefa: dizer, para cada vilão, se ele alguma vez já foi capturado pelo cavaleiro das trevas.

##### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/2510

# Resolução:

O objetivo desse exercício é ler o nome de T vilões e responder `Y` se ele já foi capturado pelo herói ou `N` se ele não foi capturado. Como mostra no enunciado, Batmain já capturou todos os seus vilões, então independente do nome que for escrito, a resposta será `Y`. 

Nesse exercício vamos declarar duas variáveis do tipo `int` e uma do tipo `char`:
```c
    int T, i;
    char N[26];
```
`T` indica o número de nomes que vamos ler. `i` é uma variável auxiliar que vai ser usada na estrutura `for` e `N` é um vetor de `char` que vai armazenar o nome do vilão.

Primeiro vamos saber quantos nomes serão lidos. Para isso usamos `scanf`:
```c
    scanf("%d", &T);
```
Em seguida vamos iniciar o laço de repetição. Aqui lemos o vetor de `chars` como uma `string` (`%s`) usando `scanf` e mostramos na tela a mensagem `Y`:
```c
    for(i=0;i<T;i++) {
      scanf("%s", N);
      printf("Y\n");
    }
```
Quando usamos `scanf` para ler uma `string`, ela não pode superar o número de `chars` separados para a variável, que no caso é 26. Além disso, o `scanf` não permite que você escreva espaços dentro do nome.

##### Para aprender um pouco mais sobre a estrutura for: [For](http://linguagemc.com.br/a-estrutura-de-repeticao-for-em-c/)
##### Para aprender um pouco mais sobre string: [String](http://linguagemc.com.br/string-em-c-vetor-de-caracteres/)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
