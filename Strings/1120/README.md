# Problema:

Durante anos, todos os contratos da Associação de Contratos da Modernolândia (ACM) foram datilografados em uma velha máquina de datilografia.

Recentemente Sr. Miranda, um dos contadores da ACM, percebeu que a máquina apresentava falha em um, e apenas um, dos dígitos numéricos. Mais especificamente, o dígito falho, quando datilografado, não é impresso na folha, como se a tecla correspondente não tivesse sido pressionada. Ele percebeu que isso poderia ter alterado os valores numéricos representados nos contratos e, preocupado com a contabilidade, quer saber, a partir dos valores originais negociados nos contratos, que ele mantinha em anotações manuscritas, quais os valores de fato representados nos contratos. Por exemplo, se a máquina apresenta falha no dígito 5, o valor 1500 seria datilografado no contrato como 100, pois o 5 não seria impresso. Note que o Sr. Miranda quer saber o valor numérico representado no contrato, ou seja, nessa mesma máquina, o número 5000 corresponde ao valor numérico 0, e não 000 (como ele de fato aparece impresso).

##### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/1120

# Resolução:

Para esse problema, temos que identificar os caracteres (dígitos) que precisamos retirar e para retirá-los recuamos a esquerda todos os dígitos a direita do dígito identificado, sobreescrevendo o dígito "problemático".


Na declaração de variáveis, temos `char digito` que receberá da entrada, o dígito que apresenta falha, `char valor[200]` que receberá também da entrada o valor íntegro, sem falhas, `int n` é o tamanho da string `valor`, `i, j` são auxiliares para iteração.

```c
char digito, valor[200];
int n, i, j;
```

Começamos recebendo as variáveis da entrada, e iniciamos o loop `while` que tem como condição de parada a variável `digito` ser diferente de 0. Ao fim do loop, fazemos mais uma leitura e verificação, para os novos valores de `digito` e `valor`.  

```c
scanf("%c", &digito);
scanf("%s", valor);

while(digito != '0'){
    .
    .
    .
    scanf("%c", &digito);
    scanf("%s", valor);
}
```

Na primeira etapa do loop, atualizamos o valor de `n` com o tamanho da string `valor` através da função `strlen()` que retorna o tamanho da cadeia de caracteres, com isso, iniciamos um loop `for` que vai de 0 a `n`, percorrendo toda a string.

Durante o loop, a cada caractere verificamos se ele é igual ao `digito` que apresenta falha, para podermos tratá-los e removê-lo da string. Assim que entrar nesse `if`, percorremos daquele ponto até o fim, recuando os digitos da direita, ou seja, `valor[j] = valor[j+1]`. Assim que chegamos ao último caractere, o loop `for` se encerra e trocamos o último dígito para 0 e reduzimos o valor de `n` em 1, que refere-se ao tamanho do vetor de caracteres `valor`.


Note que também decrementamos o contador `i` para que aquela posição (que foi substituida pelo dígito a direita, seja verificada novamente)

```c
while (digito != '0'){
    n = strlen(valor);
    for (i = 0; i < n; i++) {
        if (valor[i] == digito) {
            for (j = i; j < n; j++)
                valor[j] = valor[j+1];
            valor[n-1] = 0;
            n--;
            i--;
        }
    }

    .
    .
    .

```

Após remover todos os digitos que apresentam falha do vetor `valor`, temos também que remover os zeros a esquerda do nosso número, como dito no enunciado.

Fazemos isso com outro loop for, idêntico ao anterior, porém, com a verificação `if(valor[i] == '0')` que remove todos os 0's iniciais do vetor `valor`, e assim que um dígito diferente de 0 aparecer, o `else break` encerra esse segundo loop `for`.

```c
    while (digito != '0'){
        
        .
        .
        .

        for (i = 0; i < n-1; i++) {
            if (valor[i] == '0') {
                for (j = i; j < n; j++)
                    valor[j] = valor[j+1];
                valor[n-1] = 0;
                n--;
                i--;
            }
            
            else
                break;
        }

        .
        .
        .
    }
```

Após retirar os dígitos indesejáveis, fazemos uma última verificação para caso o vetor esteja vazio, ou seja, `n == 0`. Em caso positivo, substituímos o primeiro dígito por 0 e o segundo pelo indicador de fim de string `\0`. Isso é feito porque caso o `valor` seja 0000, todos serão considerados 0 a esquerda, enquanto apenas os 3 primeiros deveriam ser considerados, portanto, mantemos um na string.


E após todas essas verificações e tratamentos, podemos exibir a variável `valor` devidamente tratado como sugere a saída do problema.

```c
while (digito != '0'){
    
    .
    .
    .

    if (n == 0) {
        valor[0] = '0';
        valor[1] = '\0';
    }

    printf("%s\n", valor);

    scanf(" %c", &digito);
    scanf("%s", valor);
}
```


Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
