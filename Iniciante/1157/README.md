# Problema

Ler um número inteiro N e calcular todos os seus divisores.

**Problema completo**: https://www.urionlinejudge.com.br/judge/pt/problems/view/1157

# Resolução

Para esse exercício, precisaremos do conceito de [divisores](https://mundoeducacao.uol.com.br/matematica/multiplos-divisores.htm), temos dois pontos que devem ser levados em consideração.

1. Todo divisor de um número é de menor ou igual valor que o próprio número.
2. Para y ser divisor de x, x dividido por y deve possuir resto = 0.

Primeiramente, iremos declarar nossas variáveis. Como dito pelo problema, declaramos `N` como um inteiro e também um `i` que será nossa variável auxiliar para o loop.

```c
    int N, i;
``` 

Tendo a variável declarada, podemos recebe-la do usuário utilizando o `%d` para se referir ao inteiro `N`.

```c
    scanf("%d",&N);
```

Agora, com um loop `for` iremos percorrer todos os números inteiros anteriores a `N` (incluindo N) com a variável `i` (Ponto 1 levantado no começo dessa explicação).
Com o trecho `if(N%i == 0)` fazemos a verificação se o resto da divisão de `N`por `i ` é 0, caso positivo, o escrevemos na tela com a função `printf`.

```c
    for(i = 1; i <= N; i++){
        if(N%i == 0){
            printf("%d\n",i);
        }
    }
```

#### Aprenda um pouco mais sobre operadores e expressões: [Operadores](https://pt.wikibooks.org/wiki/Programar_em_C/Operadores)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com