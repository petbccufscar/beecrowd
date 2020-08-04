# Problema:    
Faça um algoritmo para ler um valor A e um valor N. Imprimir a soma de A para cada i com os valores (0 <= i <= N-1). Enquanto N for negativo ou ZERO, um novo N(apenas N) deve ser lido.

**Problema completo**: https://www.urionlinejudge.com.br/judge/pt/problems/view/1149


# Resolução:
Apesar da descrição confusa, a resolução é simples.  


> "Imprimir a soma de A para cada i com os valores (0 <= i <= N-1)."

A lógica é somar o valor `A` com todos os valores de `0` a `N-1`, um a um. No exemplo de 3 e 2, temos:  
- 3 + 0 = 3
- 3 + 1 = 4
- Total: 3 + 4 = 7

Outro exemplo, com as entradas 2 e 3:  
- 2 + 0 = 2
- 2 + 1 = 3
- 2 + 2 = 4
- Total = 9  

> "Enquanto N for negativo ou ZERO, um novo N(apenas N) deve ser lido."

Significa ler a entrada N até que o valor seja positivo, ignorando números negativos ou 0.  


Dessa forma, o primeiro passo para resolver o exercício é declarar as variáveis necessárias para o problema: `A`, `N`, `i` e `soma`. Vamos utilizar a variável `i` em um loop e guardar a soma final em `soma`. Inicializamos `soma` com 0 para incrementar a variável depois.  

```c
int A, N, i, soma;

soma = 0;
```

Em seguida, faremos a leitura dos valores `A` e `N`.

```c
scanf("%d %d", &A, &N);
```

O exercício tenta complicar o raciocínio inserindo valores negativos e zeros em `N`. Para contornar, vamos simplesmente **ignorar** estes valores e ler `N` novamente até um número válido ser digitado. Faremos isso com um `while`, verificando se `N <= 0` e chamando a função `scanf`.

```c
while (N <= 0) {
    scanf("%d", &N);
}
```

Agora, tendo `A` e `N` válidos, vamos realizar as somas que o exercício pede, igual ao exemplo no início. Para isso, faremos um loop `for` de `i` até `N-1`.  
Dentro do loop, incrementamos a variável `soma` com `(A + i)`, que representará os exemplos `(3 + 0)`, `(3 + 1)`, etc.

```c
for (i = 0; i < N; i++) {
    soma += (A + i);
}
```

Ao final, exibimos o valor na tela com uma quebra de linha.

```c
printf("%d\n", soma);
```

##### Para revisar sobre o laço while: [O comando while](http://linguagemc.com.br/o-comando-while-em-c/)
##### Para revisar o laço for: [O comando for](http://linguagemc.com.br/a-estrutura-de-repeticao-for-em-c/)
    
Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
