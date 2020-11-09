# Problema:    
Uma aliteração ocorre quando duas ou mais palavras consecutivas de um texto possuem a mesma letra inicial (ignorando maiúsculas e minúsculas). Sua tarefa é desenvolver um programa que identifique, a partir de uma sequência de palavras, o número de aliterações que essa sequência possui.

Entrada<br/>
A entrada contém diversos casos de testes. Cada caso é expresso como um texto em uma única linha, contendo de 1 a 100 palavras separadas por um único espaço, cada palavra tendo de 1 a 50 letras minúsculas ou maiúsculas ('A'-'Z','a'-'z'). A entrada termina em EOF.

Saída<br/>
Para cada caso de teste imprima o número de aliterações existentes no texto informado.

**Problema Completo**: https://www.urionlinejudge.com.br/judge/pt/problems/view/1263


# Resolução:
O exercício pede para desenvolver um programa que identifique e conte aliterações em uma string, para isso precisamos comparar as letras iniciais das palavras consecutivas e julgar se elas caracterizam ou não uma aliteração. 

Para resolver esse problema, iremos utilizar as bibliotecas `<string.h>` e `<ctype.h>` para nos auxiliar em operações envolvendo strings. 

Inicialmente, declaramos as variáveis. Utilizamos a variável `frase` do tipo array de `char`, de tamanho 5099 para obedecer os limites impostos na entrada do problema, para armazenar a string de entrada. Declaramos também variáveis inteiras: `espaco`, para armazenar os índices em que se encontram os espaços da frase; `inicial` para o índice das letras iniciais das palavras; `count` para contar as aliterações na frase e `ehSequencia` para sabermos se estamos em sequência de iniciais iguais ou não.
```c
char frase[5099];
int espaco, inicial, count, ehSequencia; 
```

Para começar a resolução, precisamos definir um loop para ler todos os casos de teste. Fazemos então um `while` que fica em loop lendo a entrada até que ela seja EOF. Utilizamos o `fgets` para ler a entrada pois ele lê a linha toda, enquanto o usual `scanf` lê até o primeiro espaço. Para utilizar o `fgets` precisamos passar a variável que vai armazenar a entrada, o tamanho máximo da entrada e da onde essa entrada será lida (no caso `stdin` que é o teclado). A condição do `while` funciona pois quando o `fgets` receber um EOF, será retornado um `NULL` então o loop irá acabar. 

```c
while(fgets(frase, sizeof(frase), stdin) != NULL){ 
```

Dentro do `while` iniciamos nossas variáveis com o valor 0. Pois a primeira inicial é 0, nosso contador também deve ser iniciado em 0 e ainda não encontramos uma sequência, então `ehSequencia` também é 0. 

```c
inicial = 0; 
count = 0;
ehSequencia = 0;
```

Em seguida, iteramos pela string com um `for` que vai de 0 até o tamanho da string, para obter o tamanho da string, utilizamos a função [`strlen`](http://linguagemc.com.br/a-biblioteca-string-h/) da biblioteca `<string.h>`. Depois, temos um `if` para verificar se aquele caractere é um espaço ou não, se ele for um espaço, sabemos que o próximo caracter `(espaco+1)` é a inicial da próxima palavra. Então, comparamos a inicial da primeira palavra com a próxima, utilizamos a função [`tolower`](http://linguagemc.com.br/ctype-h-toupper-tolower-isalpha-isdigit-em-c/) (que é definida na biblioteca `<ctype.h>`) para os dois caracteres ficarem em caixa baixa, justamente para não haver distinção entre letras minúsculas e maiúsculas. Se as duas iniciais forem iguais, verificamos se estamos ou não em uma sequência com mais um `if`, se não estamos em uma sequência, isso é uma aliteração, portanto adicionamos um ao nosso contador e definimos `ehSequencia = 1`, pois agora estamos em uma sequência de iniciais consecutivas iguais. 

```c
for(espaco = 0; espaco < strlen(frase); espaco++)
    if(frase[espaco] == ' '){
        if(tolower(frase[inicial]) == tolower(frase[espaco+1])){
            if(!ehSequencia){
                count++;
                ehSequencia = 1;
            }
        }
```

Se as iniciais não forem iguais, ou seja se `if(tolower(frase[inicial]) == tolower(frase[espaco+1]))` retornar falso, então não estamos em uma sequência iniciais iguais, portanto `ehSequencia = 0`. Note que a variável `ehSequencia` funciona como uma variável booleana, 0 para falso e 1 para verdadeiro. Essa variável serve justamente para não contarmos aliterações a mais, pois podemos ter uma frase como por exemplo: "four fanatic fantastic fans" em que todas as iniciais são iguais, porém só há uma aliteração. Por isso, contamos uma aliteração quando as iniciais são iguais e não estão em sequência. Por fim, fazemos com que a próxima inicial seja o `espaco+1` , pois na próxima iteração vamos comparar com a palavra seguinte. 

```c
    else
        ehSequencia = 0;

    inicial = espaco+1;
}
```

Finalmente, apresentamos o resultado fazendo um `printf` do count.

```c
printf("%d\n", count); 
```
    
#### Para aprender um pouco mais sobre fgets: [Fgets](http://www.w3big.com/pt/cprogramming/c-function-fgets.html)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com

