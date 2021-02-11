# Problema:

Os estudantes da tua universidade recentemente adquiriram o desagradável hábito de cabular as aulas. Para enfrentar este problema o seu Conselho de Professores decidiu somente permitir que estudantes com ao menos 75% de presença prestem os exames. A partir de uma lista de nomes de estudantes e seus respectivos registros de frequência, imprima o nome dos estudantes que não obtiveram o mínimo de presença nas aulas e que consequentemente não poderão prestar os exames.

##### Link do problema: https://www.urionlinejudge.com.br/judge/pt/problems/view/1277
 
# Resolução:

O exercício consiste em ler um número específico de casos de teste e, para cada caso de teste, imprimir quais alunos não cumpriram o mínimo de presença.

Primeiro, instanciamos as variáveis necessárias, sendo elas: três vetores do tipo `char` (onde armazenaremos o `nome`, a `frequencia` e a `saida` do programa), 7 do tipo `int` (sendo `N` o número de estudantes; `T` o número de casos de teste; `p` para somar as presenças, `a` para somar as ausências; e `i`, `j` e `k` para serem índices dos vetores) e por fim um `char` (`c` para pegar o lixo que virá do`scanf`). Em seguida, lemos o `T`.

```c
    int N, T;
    char nomes[5000], freq[5000], saida[5000], c;
    int i, j, k, p, a;

    scanf("%d", &T);
    scanf("%c", &c);
```

Utilizaremos um `while(T > 0)` para passar por todos os casos de teste, sendo que, sempre ao final do mesmo, `T` será decrementada. Dentro do loop, inicialmente, iremos ler o `N` com `scanf` e `nomes` e `freq` com `gets`, em sequência _'limpamos'_ a saída (marcando o índice 0 como o final utilizando o `\0`) e zeramos todas as variáveis de índice e soma.

Após cada caso individual, marcamos o final da `saida` com o `\0` e imprimimos a respectiva saída.

```c
    while (T > 0)
    {
        scanf("%d", &N);
        scanf("%c", &c);
        gets(nomes);
        gets(freq);
        saida[0] = '\0';
        i = 0;
        j = 0;
        k = 0;
        p = 0;
        a = 0;

        \\código para cada caso individual

        saida[k - 1] = '\0';
        printf("%s\n", saida);
        T--;
    }
```

O código do caso individual será um `do{} while()` que irá verificar todas as frequências até chegar no final do respectivo vetor (ou seja, `\0`). Dentro das chaves iremos contar as presenças e faltas utilizando `if` e `else if`, feito isso para um aluno, iremos verificar a sua frequência e decidir se seu nome irá estar na `saida` ou não. Ao final do `do` iremos incrementar `i` que será nosso índice de `freq`.

```c
    if (freq[i] == 'P')
        p++;
    else if (freq[i] == 'A')
        a++;
    else if (freq[i] == ' ' || freq[i] == '\0')
    {
    //verifica a frequência
    }
    i++;
```

Para essa verificação utilizaremos um `if` para comparar se a presença é menor que 3 vezes as ausências (ou seja, conferir se o respectivo aluno tem uma presença menor que 75%). 

Caso isso seja _verdadeiro_ utilizaremos um `while` para armazenar o nome do aluno na `saida`, sendo que esse `while` vai parar de copiar os `chars` quando encontrar o fim da linha ou um espaço em branco e como o índice da `saida` é o `k` ele será incrementado em toda iteração do laço, assim como o `j` que é nosso índice de `nomes`. Antes do final do `if` copiamos o último `char` de `nomes`, incrementamos `j` e `k` e zeramos `p` e `a`.

Caso isso seja _falso_ utilizaremos um `while` para pular esse aluno, pois ele cumpriu a frequência, sendo que esse `while` vai parar de pular os `chars` quando encontrar um espaço em branco, ou seja vai incrementar `j` até achar um espaço em branco. Antes do final do `else`, incrementamos `j` e zeramos `p` e `a`.

```c
    if (p < a * 3)
    {
        while (nomes[j] != ' ' && nomes[j] != '\0')
        {
            saida[k] = nomes[j];
            k++;
            j++;
        }
        saida[k] = nomes[j];
        k++;
        j++;
        p = 0;
        a = 0;
    }
    else
    {
        while (nomes[j] != ' ')
        {
            j++;
        }
        j++;
        p = 0;
        a = 0;
    }
```


##### Para aprender um pouco mais sobre a estrutura while: [While](http://linguagemc.com.br/o-comando-while-em-c/)

##### Para aprender um pouco mais sobre a estrutura do{} while: [Do](http://linguagemc.com.br/comando-do-while/)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
