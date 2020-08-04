# Problema:    
Este programa deve ler uma variável inteira X inúmeras vezes (deve parar quando o valor no arquivo de entrada for igual a zero). Para cada valor lido imprima a sequência de 1 até X, com um espaço entre cada número e seu sucessor.

**Problema completo**: https://www.urionlinejudge.com.br/judge/pt/problems/view/1146


# Resolução:
Para resolver o exercício, o primeiro passo é declarar as variáveis necessárias para o problema: `X` e `i`. Vamos utilizar a segunda variável em um loop.  

```c
int X, i;
```

Em seguida, faremos a leitura do valor `X`.

```c
scanf("%d", &X);
```

Para imprimir uma sequência de 1 até X, vamos utilizar um loop `while` que será executado enquanto `X != 0`.  
O exercício exige que não seja impresso espaço após o último número, então vamos utilizar a seguinte lógica:  

- Percorrer um laço `for` de `1` até `X-1`;
- Imprimir cada número com um espaço;
- Fora do laço, imprimir o último número `X` com a quebra de linha `\n`.

Ao final, devemos ler o número `X` para a próxima execução do `while`, utilizando novamente a função `scanf`.

```c
while (X != 0) {

    for(i = 1; i < X; i++)
        printf("%d ", i);
    
    printf("%d\n", X);

    scanf("%d", &X);
}
```

###### Note que, como o laço `for` possui apenas uma linha dentro, podemos omitir as chaves `{}`. Em códigos maiores, esta sintaxe não é recomendada.


##### Para revisar sobre o laço while: [O comando while](http://linguagemc.com.br/o-comando-while-em-c/)
##### Para revisar o laço for: [O comando for](http://linguagemc.com.br/a-estrutura-de-repeticao-for-em-c/)
    
Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
