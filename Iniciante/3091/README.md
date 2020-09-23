# Problema:
William, John é um aluno vidrado por matemática, mas poucas pessoas sabem disso. Certo dia, um de seus colegas de classe achando que John não sabia conceitos básicos da matemática o desafiou a realizar um simples cálculo que era: Calcular o resto da divisão de A ÷ B
Como John é muito tímido e vocês são melhores amigos, ele te informou qual era a resposta para o problema e pediu para que você passasse tal informação para esse colega que o desafiou. Você pode fazer isso ?
Dado dois inteiros A e B, diga qual o resto da divisão de A ÷ B que John passou para você.

**Problema completo:** https://www.urionlinejudge.com.br/judge/pt/problems/view/3091


# Resolução: 
De início, declaramos as variáveis que usaremos, todas do tipo `int`: `dividendo` que assumirá o valor a ser dividido; `divisor` que será o valor que dividirá a variável anterior; `resto` que receberá o valor excedente da divisão.
``` c
    int dividendo, divisor, resto;
```

Agora, leremos com `scanf` os valores do número a ser divido e o valor da divisão e atribuíremos os mesmos à `dividendo` e `divisor`, respectivamente.
``` c
    scanf("%d %d", &dividendo, &divisor);
```

Proseguindo, usamos `%` para retornar o valor do resto da divisão entre `dividendo` e `divisor`. Ademais, atribuímos esse valor à `resto`.
``` c
    resto = dividendo % divisor;
```

Por fim, imprimimos na tela, com `printf`, o valor de `resto` - não esquecendo de `\n`, por questões de padrão de resposta do URI, e de retornar 0.
``` c
    printf("%d\n", resto);
    return 0;
```
Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com