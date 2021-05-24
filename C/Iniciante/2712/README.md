# Problema:   

O rodízio municipal de veículos de São Paulo é uma restrição à circulação de veículos automotores na cidade. Implantado desde 1996 com o propósito de melhorar as condições ambientais reduzindo a carga de poluentes na atmosfera, se consolidou como um instrumento para reduzir congestionamentos nas principais vias da cidade, nos horários de maior movimento. Nas vias delimitadoras não é permitido o tráfego de caminhões e automóveis que estejam dentro da restrição. Há uma escala que determina em quais dias da semana quais veículos não podem circular. Essa escala é regida pelo último dígito da placa do veículo, sendo:

- Segunda-feira, dígito final da placa 1 e 2
- Terça-feira, dígito final da placa 3 e 4
- Quarta-feira, dígito final da placa 5 e 6
- Quinta-feira, dígito final da placa 7 e 8
- Sexta-feira, dígito final da placa 9 e 0

Os motoristas que são flagrados violando a restrição de circulação são autuados com multa e quatro pontos na carteira de habilitação.

**Problema Completo**: https://www.urionlinejudge.com.br/judge/pt/problems/view/2712

# Resolução:

O problema consiste em verificar se uma placa é válida e, caso seja, exibir o dia de seu rodízio. Como vamos trabalhar com letras, faremos uso da biblioteca `string.h`, importada no início do código.

Além disso, para deixar o código mais organizado, vamos criar uma função que verifica se uma placa é válida. A função recebe um ponteiro de caracteres e retorna 0 ou 1, sendo 0 para um formato incorreto e 1 para um formato válido.  
Começamos declarando a função e um contador `i`.

```c
int placaValida(char *placa) {
    int i;
```

A primeira verificação que fazemos é se a placa contém 8 dígitos (3 letras, 1 traço e 4 números). Para isso, utilizamos a função `strlen()`, contida na biblioteca `string.h`. Caso a placa não tenha 8 caracteres, retornamos 0.

```c
    if (strlen(placa) != 8)
        return 0;
```

Em seguida, verificamos os 3 primeiros caracteres da placa e, caso algum não esteja entre `[A-Z]`, retornamos 0. Fazemos a verificação ao contrário: caso `placa[i]` esteja abaixo de `'A'` ou acima de `'Z'`, entramos na condição.  
É importante lembrar que, quando utilizamos um caractere em C, a linguagem o interpreta como um número da [tabela ASCII](https://www.ime.usp.br/~kellyrb/mac2166_2015/tabela_ascii.html).

```c
    for (i = 0; i < 3; i++)
        if (placa[i] < 'A' || placa[i] > 'Z')
                return 0;
```

O 4º caractere, na posição `placa[3]`, deve ser o traço `-` da placa. Caso não seja, retornamos 0.

```c
    if (placa[3] != '-')
        return 0;
```

Por último, verificamos se os últimos 4 dígitos são números. Utilizamos a mesma lógica das letras, verificando se a posição `placa[i]` é menor que `'0'` ou maior que `'9'`.

```c
    for (i = 4; i < 8; i++)
        if (placa[i] < '0' || placa[i] > '9')
            return 0;
```

Caso a função não tenha retornado até o momento, significa que o formato da placa é válido. Dessa forma, retornamos 1 e encerramos a função.

```c
    return 1;
}
```

_______________________________

Agora, na função principal, declaramos três variáveis: a quantidade de casos `N`, um contador `i` e a `placa[100]` (o tamanho máximo 100 está nas especificações de entrada).

```c
int N, i;
char placa[100];
```

Recebemos a quantidade de casos de teste.

```c
scanf("%d", &N);
```

Para cada caso de teste, recebemos a placa e verificamos se ela é válida, utilizando a função criada no início.

```c
for (i = 0; i < N; i++) {
    scanf("%s", placa);

    if (placaValida(placa) == 1) {
```

Caso seja, seguimos a tabela do enunciado para exibir qual o dia de seu rodízio.

```c
        if (placa[7] == '1' || placa[7] == '2')
            printf("MONDAY\n");

        else if (placa[7] == '3' || placa[7] == '4')
            printf("TUESDAY\n");

        else if (placa[7] == '5' || placa[7] == '6')
            printf("WEDNESDAY\n");

        else if (placa[7] == '7' || placa[7] == '8')
            printf("THURSDAY\n");

        else if (placa[7] == '9' || placa[7] == '0')
            printf("FRIDAY\n");
```

Se a placa não é válida, exibimos `"FAILURE"` e encerramos o caso de teste.

```c
    } else {
        printf("FAILURE\n");
    }
}
```

##### Para aprender mais sobre caracteres e codificação ASCII: [Resto divisão inteira](https://www.pucsp.br/~so-comp/cursoc/aulas/c240.html)
##### Para conhecer as funções da biblioteca `string.h`: [A biblioteca string.h](http://linguagemc.com.br/a-biblioteca-string-h/)


Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
