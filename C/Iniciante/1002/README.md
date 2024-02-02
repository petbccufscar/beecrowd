<img src="../../../docs/icon.png" align="right" />

# 1002 - Área da Circunferência

**Link do Problema:** [Área da Circunferência](https://www.urionlinejudge.com.br/judge/pt/problems/view/1002)

## Problema:

A fórmula para calcular a área de uma circunferência é: area = π . raio². Considerando para este problema que π = 3.14159. Efetue o cálculo da área, elevando o valor de raio ao quadrado e multiplicando por π.

## Resolução:

O problema pede o cálculo da área de uma circunferência, para obtê-la, devemos declarar e ler os valores para assim calcular a área com a fórmula informada.

Declaramos então, variáveis do tipo `double` (ponto flutuante de dupla precisão) como requerido pelo enunciado:
```c
double area, raio, pi;
```

Iremos receber do usuário o valor do `raio` e salvar o resultado em `area`. Como os valores podem ser decimais, declaramos com o tipo `double`, para não perdermos informações.

Temos que o valor de `pi` já foi definido pelo problema "Considerando para este problema que π = 3.14159" podemos então atribuir esse valor à nossa variável `pi`:
```c
pi = 3.14159;
```

Para leitura, usamos a função `scanf`:
```c
scanf("%lf",&raio);
```

Utilizamos `%lf` porque estamos recebendo um valor `double` do usuário.

Agora fazemos uma atribuição à variável `area` seguindo a fórmula de área de uma circunferência:
```c
area = (raio * raio) * pi;
```

E por fim, escrevemos o resultado na tela utilizando a função `printf`:
```c
printf("A= %.4lf\n",area);
```

Utilizamos `.4` para a saída ficar com 4 casas de precisão (como mostra nos exemplos de saída do problema).
`%lf` será substituído pelo valor contido em `area`.

## Material Auxiliar

- Para aprender um pouco mais sobre variáveis: [Variáveis](http://linguagemc.com.br/variaveis-em-linguagem-c/)
- Para entender sobre entradas e saídas: [Entrada e Saída](http://linguagemc.com.br/operacoes-de-entrada-e-saida-de-dados-em-linguagem-c/)

## Contato

Se você tiver alguma dúvida, sugestão ou precisar de suporte, por favor, sinta-se à vontade para entrar em contato conosco:

- **E-mail:** petbcc.ufscar@gmail.com

Você também pode criar uma **Issue** no [GitHub](https://github.com/petbccufscar/ufscar-planner/issues) para relatar problemas, sugerir melhorias ou contribuir para o desenvolvimento do UFSCar Planner. Estamos sempre abertos para receber feedback e colaboração. Obrigado!