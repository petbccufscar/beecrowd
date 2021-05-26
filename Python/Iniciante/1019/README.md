# [Problema URI 1019](https://www.urionlinejudge.com.br/judge/pt/problems/view/1019)

Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica, e informe-o expresso no formato horas:minutos:segundos.

**Problema completo:** [https://www.urionlinejudge.com.br/judge/pt/problems/view/1019](https://www.urionlinejudge.com.br/judge/pt/problems/view/1019)


# Resolução:


Como descrito na introdução, o problema é bem simples, deverá ser obtido um número inteiro do usuário que representará o número de segundos transcorridos e será mostrado no final a seguinte estrutura: `H:MM:SS`, sendo o total de horas, minutos e segundos transcorridos, de acordo com os segundos dados pelo usuário.

Para obtenção do dado usa-se a função `input` com o caster `int()` para forçar o dado de entrada a ser um inteiro. 

``` python
    segundos = int(input())
```

Após isso é necessário fazer as conversões, que são:
- 1 hora, são 3.600 segundos;
- 1 minuto, são 60 segundos;

Sendo feitas da seguinte maneira:

``` python
    horas = segundos/3600 
    segundos = segundos%3600 #Uso do caracter '%' (resto), que calcula o resto da divisão entre segundos e 3600.
    minutos = segundos/60
    segundos = segundos%60
```

Porém, como estamos trabalando com segundos, é necessário que a cada conversão é retirado o valor que foi transformado em horas e minutos, e por isso é necessário usar o operador `%`, pois ele calcula o resto da divisão. Após todas as conversões usa-se a função `print` para imprimir a saída ao usuário. Completando o código do seguinte jeito:

``` python
    segundos = int(input()) #Obtenção de dados apartir da função input, com o caster de inteiro.
    horas = segundos/3600 
    segundos = segundos%3600 #Uso do caracter '%' (resto), que calcula o resto da divisão entre segundos e 3600.
    minutos = segundos/60
    segundos = segundos%60
    print("%d:%d:%d"%(horas,minutos,segundos))
```
