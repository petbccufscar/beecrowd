# Problema 

Júlio César usava um sistema de criptografia, agora conhecido como Cifra de César, que trocava cada letra pelo equivalente em duas posições adiante no alfabeto (por exemplo, 'A' vira 'C', 'R' vira 'T', etc.). Ao final do alfabeto nós voltamos para o começo, isto é 'Y' vira 'A'. Nós podemos, é claro, tentar trocar as letras com quaisquer número de posições.

###### [Link do problema](https://www.urionlinejudge.com.br/judge/pt/problems/view/1253)

# Resolução

Para resolver o problema, iremos utiizar o sistema da [tabela ASCII](https://web.fe.up.pt/~ee96100/projecto/Tabela%20ascii.htm). Enquanto houverem casos, iremos receber a frase codificiada com a cifra de César, e a quantidade de vezes que cada caractere da sentença foi deslocado para a direita. Subtraímos o valor na tabela ASCII de cada letra, para que mude para sua representação não codificada.

Começamos declarando nossas variáveis, do tipo inteiro (`int`) e do tipo caracter (`char`). Serão elas:
* `cifra[50]`, variável para a cifra recebida de até 50 caracteres, conforme indicado no exercício;
* `deslocamento`, para receber o quanto iremos deslocar a cadeia de caracteres da cifra recebida;
* `casos`, para receber quantos casos serão lidos pelo programa;
* `aux`, para armazenar a cifra descodificada;
* `i`, para iterar pelo laço de repetição.
```c
    int i, deslocamento = 0, casos = 0, aux = 0;
    char cifra[50];
```

Em seguida, lemos a quantidade de casos que o programa calculará, com a função `scanf`.
```c
    scanf("%d", &casos);
```

Iniciamos nosso laço de repetição `while` para, enquanto houverem casos, continuar executando a tradução da cifra.
```c
    while(casos--)
```

Lemos, então, a cifra e o valor de deslocamento.
```c
    scanf("%s", cifra);
    scanf("%d", &deslocamento);
```

Utilizaremos a estrutura de repetição `for` para iterar em todas as posições da cifra. Caso encontre um '\0', que representa o fim de uma entrada, saímos do `for` usando `break`.
```c
    for (i = 0; i < 50; i++){
        if (cifra[i] == '\0')
            break;
```

Caso o deslocamento, quando utilizado na cifra, faça com que a letra tenha código ASCII menor do que 65 (valor da letra A), significa que devemos ir para o final do alfabeto para fazer a descodificação, conforme explicado no enunciado de Y virar A. Valores menores do que 65 na tabela ASCII são utilizados para sinais de pontuação, símbolos, etc.
Para chegar ao final do alfabeto, adicionamos 26 (quantidade de letras do alfabeto).
Caso o valor esteja acima de 65, significa que o deslocamento resulta em uma letra válida da cifra. Com isso, apenas aplicamos o deslocamento.
```c
        if ((cifra[i] - deslocamento) < 65)
            aux = (cifra[i] - deslocamento) + 26;
        else
            aux = cifra[i] - deslocamento;
```

Por fim, exibimos a cifra traduzida, sem esquecer o '\n' no final para que a saída seja de acordo com o requisitado pelo URI.
```c
        printf("%c", aux);
        }
    printf("\n");
```

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso [Facebook](https://www.facebook.com/petbcc/), [Instagram](https://www.instagram.com/petbcc.ufscar/) ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
