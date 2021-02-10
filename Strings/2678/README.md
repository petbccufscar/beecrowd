# Problema:
Desde os telefones de discagem analógica, era costume em alguns países associar aos números de discagem algumas letras, de forma que poderia-se atribuir a um número de telefone, uma palavra de fácil memorização. Este tipo de associação podemos ver na figura abaixo, que representa o "discador" de um telefone digital:

Esta prática não é muito comum no Brasil, mas existem algumas empresas que utilizam, um exemplo é uma empresa seguradora, que divulga como número de telefone: "333-PORTO". Fazendo uma associação entre letras e números, o número real de telefone é: "33376786" (o símbolo '-' é descartado). Atualmente como os telefones aceitam discagem por voz, ao ditar um número memorizado com letras e palavras, é preciso de uma tradução. A você foi pedido um programa que receba um texto representando um número de telefone e devolva o número real do telefone.

**Problema completo:** https://www.urionlinejudge.com.br/judge/pt/problems/view/2678


# Resolução

Inicialmente deve-se notar que foi pedido apenas o número que deve ser digitado de acordo com a letra, e não a sequência desse número. Por exemplo, por mais que para digitar a letra O neste telefone precisamos pressionar 666, só devemos inserir no número de telefone o número 6 uma vez.

Declaramos as seguintes variáveis: um caractere `c`, que receberá a entrada caractere a caractere e um vetor de caracteres nomeado de `teclado` que contêm todas as 24 possibilidades de referência de uma letra a um número, ou seja, como há 3 letras no número 2, inserimos o 2 três vezes no nosso vetor de referências.

```c
    char c;
    char *teclado = "22233344455566677778889999";
```

Partimos para um loop `while` que lê a entrada até o `EOF` e armazena ná variável `c`.

```c
    while (scanf("%c", &c) != EOF){

    }
```

Dentro do loop `while` criamos verificações para dividir esse caractere de entrada em 4 categorias: letra minúscula, letra maiúscula, números e caracteres especiais e damos tratamentos diferentes para cada.

* Caso letra minúscula: Printamos na tela a posição do vetor dada pela subtração do valor ASCII do caractere `c` do caractere `'a'`.

* Caso letra maiúscula: Printamos na tela a posição do vetor dada pela subtração do valor ASCII do caractere `c` do caractere `'A'`.

* Caso número: Printamos na tela o número.

* Caso caractere especial (`\n`, * ou #): Printamos o caractere especial na tela.

Para os casos que temos uma letra, a explicação se dá pela preparação do vetor e como a tabela ASCII tem seus valores decimais crescentes quando se trata do alfabeto, podemos subtrair da primeira letra `'a'` ou `'A'` para o caso das maiúsculas. Exemplo: para `c = 'A'` printaremos `teclado[c-'A']`que é equivalente a `teclado[0]` ou seja, 2.

```c
while (scanf("%c", &c) != EOF) {
    if ('a' <= c && c <= 'z')
        printf("%c", teclado[c-'a']);
    if ('A' <= c && c <= 'Z')
        printf("%c", teclado[c-'A']);
    if ('0' <= c && c <= '9')
        printf("%c", c);
    if (c == '\n' || c == '*' || c == '#')
        printf("%c", c);
}
```


**Saiba mais sobre tabela ASCII em: [Tabela ASCII](https://web.fe.up.pt/~ee96100/projecto/Tabela%20ascii.htm)**

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
