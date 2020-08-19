# Problema:

O microblog Twitter é conhecido por limitar as postagens em 140 caracteres. Conferir se um texto vai caber em um tuíte é sua tarefa.

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/2165

# Resolução

O exercício consiste em ler uma cadeia de caracteres e verificar se o tamanho dela ultrapassa 140.

Nesse exercício se faz necessário a utilização da biblioteca das string, por isso devemos declarará
ao início:

```c
        #include <string.h>
```

Para isso iniciamos declarando a variável que sera utilizada:

```c
        char T[500];
```
`T` será nossa string que possui tamanho máximo de 500, informado pelo exercício.

Fazemos a leitura de `T` usando a função `fgets` da biblioteca `<string.h>`.

```c
        fgets(T, sizeof(T), stdin);
```

Após a leitura só resta verificar atravez de `if` se o tamanho é menor ou igual 140 ou maior:

```c
        if(strlen(T)<=140)
                printf("TWEET\n");
   
        else
                printf("MUTE\n");
```

Dentro do `if` estamos usando a função `strlen` que também é uma função da biblioteca `<string.h>`, ela pega/retorna o tamanho total de uma string que no caso é a nossa `T`, usamos esse retorno e fazemos a comparação com o limite de 140, caso estiver respeitando o limite printa "TWEET", caso não "MUTE".

##### Para aprender um pouco mais sobre String: [String](http://linguagemc.com.br/a-biblioteca-string-h/)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para petbcc.ufscar@gmail.com