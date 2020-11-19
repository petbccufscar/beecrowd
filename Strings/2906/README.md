# Problema:
Nowadays there are billions of email users. A little-known fact is that some email providers offer way more than the usual username@provider.com email address.

Some providers simply ignore dots in usernames. Thus, if John owns the username johnsmith, he could tell people that his email address is johnsmith@provider.com, john.smith@provider.com or john.s.mith@provider.com, among others. Emails sent to any of these addresses would end up on his mailbox.

Other providers allow appending the character “+” followed by any combination of letters and/or digits after the username. With this feature, by registering the username johnsmith, John would also be able to use johnsmith+friends@provider.com and johnsmith+2x3is6@provider.com.

Sometimes both features are available at once and in those cases john.smith+icpc@provider.com and john.smith+wants.2.eat.lemon.3.14@provider.com are valid addresses that John could use.

This is quite useful for users, who can manage different addresses to help organize their mailboxes and easily filter the newsletters eventually sent after registering on a new website. Unfortunately, this also opens up space for abuse. Some websites rely upon the fact that each email address identifies a single user. However, a misbehaving user might easily create multiple accounts by taking advantage of the multiple addresses allowed by the email provider.

After learning all of this your boss got really worried. What if the number of unique users that has been reported to the shareholders is not accurate, bloated by duplicate accounts instead? That brings you to the task at hand: given the list of all email addresses from the users database of the company, you must determine the real number of unique users, assuming that all email providers have both described features available.
 
##### Link do problema: https://www.urionlinejudge.com.br/judge/pt/problems/view/2906
 
 
# Resolução:

Em suma, já que a descrição do problema está em inglês, este consiste em contar quantos emails únicos cada entrada possui. O email é composto pelo usuário, parte anterior ao @ e pela parte posterior ao @, o domínio.
Sobre o usuário, caso haja pontos(`.`), estes são ignorados, assim como a parte posterior à um símbolo de mais (`+`). Então, por exemplo, os usuários `bob`, `b.o.b` e `bob+new` são tidos como iguais. Já sobre o domínio, nenhum caracter é ignorado.
 


Para a resolução do problema, iremos importar a biblioteca `string.h`, para utilizarmos a função `strcmp()`, `strcpy()`, `strcat()` e `strtok()`, e a biblioteca `stdlib.h`, para utilizarmos a função `malloc()`. 

Além disso, iremos utilizar o conceito de árvore binária para armazenarmos cada email. Cada nó da árvore (`no`) será composto por um vetor de caracteres de tamanho 100, que representa o email, e dois ponteiros de `no`, o da esquerda, que aponta para um email de string menor (caso aponte para algo) e o da direita, que aponta para um email de string maior (caso aponte para algo). 

Para isso, iremos declarar nosso tipo `no`, de forma global, utilizando `typedef struct`.

```c
typedef struct no{
    char email[100];
    struct no *esq;
    struct no *dir;

} no;
```

Também iremos declarar de forma global a variável do tipo inteiro `emailsUnicos` e atribuí-la o valor 0. Esta variável representa o número de emails únicos.

```c
int usuariosUnicos = 0;
```



Após isto, de forma global, iremos construir a nossa função `limpa` que irá limpar o usuário recebido pela função, removendo os caracteres ignorados, seja pontos (`.`) ou o mais (`+`) e a sua parte posterior.

Iremos declarar um vetor auxiliar `aux[101]` e duas variáveis inteiras `i`, referente ao usuário recebido `original[100]` e `j`, referente ao auxiliar `aux[101]`.

Depois, utilizaremos uma estrutura de repetição `while` que irá iterar enquanto não chegar ao fim de `original[100]`. A cada iteração do laço de repetição lemos um caracter do vetor e teremos 3 possibilidades:

- O caracter ser `+`, daí encerramos o laço com `break`; 
- O caracter ser `.`, daí ignoramos- o, incrementado `i`;
- O caracter não ser nenhum dos dois acima, daí copiamos-o para `aux` e incrementamos `i` e `j`.

```c
while (original[i]){
        
        if (original[i] == '+'){
            break;
        }
        else if(original[i] == '.'){
            i++;
        }
        else{
            aux[j] = original[i];
            j++;
            i++;
        }
    }
```

Feito isto, como optamos por uma função sem retorno `void`, precisamos alterar `original`. Esta irá receber o usuário, agora limpo( `auxiliar`) e, para indicar o fim do usuário, iremos utilizar um asterisco (`*`).
```c
for(i = 0; i < j; i++)
    original[i] = aux[i];
        
original[i] = '*';
```



Em seguida, ainda de forma global, iremos construir a nossa função `adiciona` que irá adicionar nós na árvore. Nossa função terá como parâmetros um ponteiro para um nó e uma string, que representa o email atual. Com isso, teremos 3 ocorrências:

Caso o nó recebido seja NULL, ou seja, o nó em questão ainda não existe e aquele tipo de email não foi lido anteriormente, iremos inicializá-lo da seguinte forma :
- alocamos o espaço de memória necessária de um nó, utilizando `malloc()`;
- atribuímos `NULL` aos ponteiros `esq` e `dir` deste nó, já que estes não apontam para nenhum outro nó ainda;
- atribuímos a `email` a string recebida como parâmetro pela nossa função `adiciona`;
- adicionamos 1 ao nosso contador de emails únicos (`emailsUnicos`).

```c
if (!ramo){
    ramo = (no * ) malloc(sizeof(no));
    ramo->esq = ramo->dir = NULL;
    strcpy(ramo->email, nome);
    emailsUnicos++;
    }
```

Caso o nó recebido não seja NULL, o nó em questão já foi inicializado, então só precisamos decidir se iremos para o nó a esquerda ou para o nó a direita. Decidiremos isso com base no tamanho da string recebida.
- Se for menor que o nó em que estamos, iremos para o nó da esquerda.

```c
else if (strcmp(ramo->email, nome) > 0)
        ramo->esq = adiciona(ramo->esq, nome);
```

- Se for maior que o nó em que estamos, iremos para o nó da direita.

```c
else if (strcmp(ramo->email, nome) < 0)
        ramo->dir = adiciona(ramo->dir, nome);
```

Ao fim da função, retornarmos a árvore, para que possamos construí-la e armazenar a alteração realizada a cada chamada da função. Vale ressaltar que caso o `email` do nó seja igual ao `email` recebido pela função, o retorno da função `strcmp()` será "0", então nada irá acontecer.

```c
return ramo;
```



**Com as preparações para utilizarmos a nossa estrutura de árvore feitas, mudamos nosso escopo para a função main() agora.** Iremos declarar uma variável inteira `n`, que indicará o número de emails fornecidos, dois vetores de caracteres de tamanho 100 (`usuario` e `dominio`), para lermos a string fornecida, o nó raiz da nossa árvore, inicializado com NULL e um ponteiro de caracter `usuarioLimpo`, que irá receber o retorno de `strtok()`.

```c
int n;
char usuario[100];
char dominio[100];
no *arvore = NULL;
char* usuarioLimpo;
```

Em seguida, lemos a quantidade de emails `n` e utilizaremos uma estrutura de repetição `while` que irá iterar `n` vezes.
A cada iteração do laço de repetição:
- lemos o email fornecido, armazenando a parte anterior ao arroba em `usuario` e a parte posterior em `dominio`;
- limpamos o usuário com `limpa(usuario)`;
- utilizamos `strtok(usuario, "*")`, para obtermos a parte de `usuario` anterior ao asterisco e armazenamos-a em `usuarioLimpo`;
- concatenamos `usuarioLimpo` e `dominio`, utilizando `strcat(usuarioLimpo, dominio)`;
- adicionamos o novo email na arvore utilizando `arvore = adiciona(arvore, usuarioLimpo)`
 
A árvore é atualizada a cada chamada de função, por isso utilizamos `arvore = adiciona(arvore, usuarioLimpo)`

```c
while (n--){
    scanf(" %[^@]%s", usuario, dominio);
    limpa(usuario);
    usuarioLimpo = strtok(usuario, "*");
    strcat(usuarioLimpo, dominio);
    arvore = adiciona(arvore, usuarioLimpo);
}
```

Em seguida, exibimos o número de emails únicos fornecidos.

```c
printf("%d\n", emailsUnicos);
```


##### Mais sobre alocação dinâmica: [alocação dinâmica](https://www.ime.usp.br/~pf/algoritmos/aulas/aloca.html)
##### Mais sobre alocação dinâmica de matrizes: [alocação dinâmica matrizes](http://www.inf.ufpr.br/roberto/ci067/14_alocmat.html)
##### Mais sobre árvore binária: [árvore binária](https://pt.wikibooks.org/wiki/Programar_em_C/Árvores_binárias)



Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
