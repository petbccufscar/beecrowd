# Problema:

Péricles é um rapaz que tem um interesse único por história. Utilizando seu atualizadíssimo navegador de internet rapoza cromada, conheceu até os sitios mais remotos e obscuros atrás de informações sobre a mitologia grega.

Por ironia do destino, o navegador de Péricles acabou sendo infectado por um malware com uma caracterísica peculiar: cada vez que Péricles fechava uma aba no seu navegador, outras duas abas apareciam! No entanto, quando Péricles clicou sem querer em uma das propagandas de uma aba, percebeu que, por um erro do navegador, a aba foi encerrada (sem abrir outras abas). Por causa do malware, todas as abas possuem irritantes propagandas.

Sua tarefa é descobrir com quantas abas que o navegador de Péricles ficou, sabendo o número inicial de abas e a sequência de ações de Péricles. As ações podem ser fechou (quando Péricles fechou uma aba) ou clicou (quando Péricles clicou em uma propaganda).

Exemplo de Entrada:

                    3 5
                    fechou
                    fechou
                    clicou
                    clicou
                    clicou
Saída: 2 

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/2061

# Resolução

Tendo como exemplo as entradas e a saída podemos entender melhor o exercício, que consiste em iniciar com o número de abas abertas e a quantidade de casos que serão testados, seguindo pelo valor de cada caso que será `fechou` (resulta em mais 1 aba) ou `clicou` (resulta em menos 1 aba).

Nesse exercício iremos utilizar uma biblioteca para poder trabalhar com string/vetor de char:

```c
        #include <string.h>
```

Seguimos declarando as variáveis que serão utilizadas:

```c
        int N, i, M;
        char str[20];
```
`N` o número de abas, `i` variável padrão utilizada no controle do `for`, `M` número de casos clicou/fechou, `str[20]` é a `string` responsável por armazenar as palavras clicou/fechou. O tamanho dela foi escolhido arbitrariamente, só tendo em mente que deve ser um valor maior ou igual a palavra que se pretende armazenar dentro da string.
Fazemos a leitura de `N` e `M` no `scanf`:

```c
        scanf("%d %d", &N, &M);
```

Seguimos para a construção do `for` onde será feito a lógica do exercício:

```c
        for (i = 0; i < M; i++)
        {
        scanf("%s", str);
      
        if(strcmp(str, "fechou")==0){
           N++;
        }
        else if(strcmp(str, "clicou")==0){
           N--;
        }
        }
```
Fazemos o `for` iterar até atingir `M` e dentro dele leremos se clicou ou fechou. Verificamos usando `if`, nosso condicional, se ele clicou ou fechou e para isso usamos a função `strcmp` da biblioteca `<string.h>` que irá comparar as strings e caso elas forem iguais retorna 0, assim entrando na condicional e incremento ou decremento nosso `N`(número de abas). 

Finalizamos printando a saída(número de abas restantes) pedida pelo Uri:

```c
        printf("%d\n", N);
```

##### Para aprender um pouco mais sobre Strings e sua biblioteca: [String](http://linguagemc.com.br/a-biblioteca-string-h/)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para petbcc.ufscar@gmail.com