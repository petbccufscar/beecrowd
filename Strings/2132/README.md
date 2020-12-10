# Problema:

Uma brincadeira começa com uma das crianças desenhando um diagrama com estados (representados por bolinhas) ligados por transições (flechas ligando os estados). Cada transição tem uma letra e um número associados. Podemos fazer diversos passeios neste diagrama, partindo de um estado inicio caminhando por suas transições e terminando em um estado final. Um passeio forma uma palavra (obtida da concatenação das letras das transições percorridas) e tem um custo (que é dado pelo produto dos números destas transições).

Exemplo, considere o diagrama abaixo.

i[diagrama](https://resources.urionlinejudge.com.br/gallery/images/problems/UOJ_2132.png)


Todos os passeios iniciam no estado P e terminam em Q. O passeio que segue pelas transições (P,1A), (P,1A), (P,1B) e termina no estado Q forma a palavra AAB concatenando as letras de cada transição tem custo 1 (produto dos números destas transições).

O passeio que segue pelas transições (P,1A), (P,1A), (P,1B), (Q,2B) e termina no estado Q forma a palavra AABB e tem custo 2.

##### Link do problema: https://www.urionlinejudge.com.br/judge/pt/problems/view/2132
 
# Resolução:

O exercício consiste em ler casos de teste, até acabar o arquivo, e, para cada caso de teste, imprimir qual a palavra em questão (seu número) e a soma de todos os caminhos (produto dos valores dos saltos).

Primeiro instanciamos as variáveis necessárias, sendo elas: um vetor do tipo `char` (onde armazenaremos a string lida), três do tipo `int` (`i` será nosso índice para ler cada `char`; `tam` armazena o tamanho da `string` lida; e `caso` armazena o atual caso de teste) e um `long long int` (para armazenar o produto `total`).

```c
    char palavra[61];
    int i, tam, caso = 1;
    long long int total;
```

Utilizaremos um `while()` para passar por todos os casos de teste. Dentro dele utilizaremos um `scanf("%s", palavra) != EOF`, para saber quando chegamos ao final do arquivo. Primeiro imprimimos em qual palavra estamos, armazenamos o tamanho da palavra e zeramos o `total` (pois estamos começando um novo caso). No final do caso imprimimos o valor do total

```c
    while (scanf("%s", palavra) != EOF)
    {
        printf("Palavra %i\n", caso);
        tam = strlen(palavra);
        total = 0;

        //for() para calcular o total

    }

```

Utilizaremos um `for (i = 0; i < tam; i++)` para analizar caractere por caractere. Como pode-se perceber, o produto só será relevante quando chegar no estado `q`, que só pode ser alcançado se existir algum `b` na palavra e como depois de chegar ao estado  `q` todos os saltos tem valor 2 então podemos calcular o valor daquele caminho do `b` encontrado simplismente somando ao total o valor de 2 elevado ao numero de caracteres que faltam.

```c
    for (i = 0; i < tam; i++)
        {
            if (palavra[i] == 'b')
            {
                total = total + pow(2, tam - i - 1);
            }
        }
```

Por fim, imprimimos o valor total daquela palavra e uma linha em branco (por isso utilizaremos 2 `\n`) e incrementamos o valor de caso. Lembrando que como estamos utilizando um `long long int` imprimimos utilizando `%lld`

```c
    while (scanf("%s", palavra) != EOF)
    {
        //code

        //for ()
        
        printf("%lld\n\n", total);
        caso++;
    }
```


##### Para aprender um pouco mais sobre a estrutura while: [While](http://linguagemc.com.br/o-comando-while-em-c/)

##### Para aprender um pouco mais sobre a tipos de variáveis e suas respectivas impressões: [Variáveis](https://en.wikipedia.org/wiki/C_data_types)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
