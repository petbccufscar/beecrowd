# Problema:
Em cada quarto há apenas uma tomada de energia disponível. Precavidos, os três membros do time e o técnico compraram cada um uma régua de tomadas, permitindo assim ligar vários aparelhos na única tomada do quarto de hotel; eles também podem ligar uma régua em outra para aumentar ainda mais o número de tomadas disponíveis. No entanto, como as réguas têm muitas tomadas, eles pediram para você escrever um programa que, dado o número de tomadas em cada régua, determine o número máximo de aparelhos que podem ser conectados à energia num mesmo instante.

##### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/1930

# Resolução:

O objetivo desse exercício é calcular quantos aparelhos podem ser colocados para carregar ao mesmo tempo. Temos que lembrar que cada régua vai estar ligada em outra então uma tomada das três primeiras réguas já estarão ocupadas.

Para começar, criamos cinco variáveis do tipo `int`:
```c
    int t1, t2, t3, t4, soma;
```
`t1`, `t2`, `t3` e `t4` são as variáveis que representam quantas tomadas têm em uma régua. `soma` será usada para guardar o resultado que buscamos no exercício.

Precisamos ler os valores de `t1`, `t2`, `t3` e `t4`. Usamos o `scanf` para ler os valores:
```c
    scanf("%d%d%d%d", &t1, &t2, &t3, &t4);
```
Podemos escrever mais de um valor dentro de um `scanf` usando vários `%d`. Sabendo quantas tomadas tem cada régua, somamos quantos aparelhos podem ser carregados:
```c
    soma = t1 + t2 + t3 + t4 - 3;
```
Lembre que uma régua está ligada na outra, então devemos desconsiderar 3 tomadas para chegar ao resultado final.

Por fim, escrevemos na tela o resultado usando `printf`. O `\n` no fim serve para pular uma linha na tela depois de mostrar o texto:
```c
    printf("%d\n", soma);
```

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
