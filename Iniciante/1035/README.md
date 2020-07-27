# Problema:

Leia 4 valores inteiros A, B, C e D. A seguir, se B for maior do que C e se D for maior do que A, e a soma de C com D for maior que a soma de A e B e se C e D, ambos, forem positivos e se a variável A for par escrever a mensagem "Valores aceitos", senão escrever "Valores nao aceitos".

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/1035

# Resolução:

Devemos realizar a leitura de quatro valores inteiros A, B, C e D. Estes serão aceitos se obedecerem as seguintes restrições:
• B > C
• D > A
• (C + D) > (A + B)
• C é positivo
• D é positivo
• A é par

Caso contrário, os valores não são aceitos.


Com o intuito de facilitar determinadas verificações, incluiremos a biblioteca `stdbool.h`, a qual permite a utilização do tipo `bool` (booleano), armazenando valor `true` ou `false`. O ato de incluir uma nova biblioteca deve ser feito fora da função main.

```c
        #include <stdbool.h>
```


Como o enunciado nos forneceu os nomes das variáveis (do tipo inteiro) a serem utilizadas, declaramos A, B, C e D como `int`. Estas irão armazenar entradas fornecidas pelo usuário e, portanto, utilizamos a função `scanf()`, a qual conterá quatro argumentos `%d` para guardar cada um dos inteiros a serem utilizados.

```c
    int A, B, C, D;
    scanf("%d %d %d %d", &A, &B, &C, &D);
```


Para auxiliar na análise, criaremos 4 novas variáveis. Duas delas (`soma1` e `soma2`), inicializadas com o valor 0, serão do tipo inteiro e possuem a finalidade de armazenar o resultado das somas **C+D** e **A+B**, respectivamente. Já as variáveis `soma1_maior` e `par` serão do tipo `bool` (booleano) e, de início, irão guardar valor `false`, para que torne-se verdadeiro apenas caso as condições estipuladas sejam cumpridas.

```c
        int soma1=0, soma2=0;
      	bool soma_maior=false, par=false;
```


Realizaremos as operações determinadas pelo exercício para, posteriormente, verificar se correspondem ao desejado. Portanto, deve-se armazenar em `soma1` o valor da adição das variáveis C e D. O mesmo ocorre com `soma2`, A e B. Em seguida, verificamos através da estrutura `if` se a primeira soma possui solução de maior valor que a segunda. Em caso positivo, `soma1_maior` armazenará `true`.

```c
    soma1 = C+D;
  	soma2 = A+B;
  	if(soma1 > soma2)
  		soma1_maior = true;
```


A estrutura condicional `if` será incluída novamente, analisando se o valor contido em A é par. Define-se como número par aquele que, ao ser dividido por 2, contém resto igual a zero. Para isto, utilizamos a operação matemática conhecida como módulo: `%`. Esta realiza a divisão de dois números, retornando apenas o resto da operação. Assim, caso o módulo de A e 2 seja equivalente a 0, `par` irá armazenar `true`.

```c
    if(A%2 == 0)
  		par = true;
```


Por último, incluiremos em uma única estrutura `if` todas as condições exigidas pelo enunciado, unindo-as pelo operador lógico `&&`, o qual indica que cada uma das condições precisam ser cumpridas para que a saída exibida, através da função `printf()`, seja **"Valores aceitos"**. Caso alguma delas não for satisfeita, a execução será direcionada ao `else`, que exibe **"Valores nao aceitos"**.

Observação: é correto, mas não necessário, colocarmos nas condições a comparação `soma1_maior == true` (o mesmo ocorre para `par`). A estrutura `if` apenas é aceita quando todas as condições estabelecidas nesta são verdadeiras, ou seja, `B>C` deve ser uma suposição verdadeira, assim como `D>A`, `C>=0` e `D>=0`. Da mesma forma, as variáveis booleanas tem de corresponder a verdadeiro, e elas por si próprias já contém `true` ou `false`.

```c
    if(B>C && D>A && soma1_maior && C>=0 && D>=0 && par)
  		printf("Valores aceitos\n");
  	else
  		printf("Valores nao aceitos\n");
```


##### Para revisar sobre variáveis booleanas: [Boolean](https://www.educative.io/edpresso/what-is-boolean-in-c)
##### Para aprender mais sobre a estrutura condicional: [If e Else](https://www.cprogressivo.net/2013/01/O-testecondicional-IF-ELSE.html)
##### Para aprender mais sobre a operação módulo: [Operação Módulo](https://www.cprogressivo.net/2012/12/Operacoes-matematicas-em-C--Soma-subtracao-multiplicacao-divisao-e-modulo-ou-resto-da-divisao-e-precedencia-dos-operadores.html)
##### Para aprender mais sobre formatação de saída: [Printf](https://alvinalexander.com/programming/printf-format-cheat-sheet/)


Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou envie um e-mail com o assunto "URI" para petbcc.ufscar@gmail.com
