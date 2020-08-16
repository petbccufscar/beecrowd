# Problema:

Na geometria Euclidiana, um polígono regular é um polígono em que todos os ângulos são iguais e todos os lados tem o mesmo comprimento. Um polígono simples é aquele cujos segmentos de reta não se interceptam. Abaixo pode-se ver vários mosaicos feitos por polígonos regulares.

Você deve escrever um programa que, dados o número e o comprimento dos lados de um polígono regular, mostre seu perímetro.

**Problema completo:** https://www.urionlinejudge.com.br/judge/pt/problems/view/1959

# Resoluçāo:

O [perímetro](https://mundoeducacao.uol.com.br/matematica/perimetro.htm.) é a medida do contorno de um polígono. Dessa forma, para calcula-lo é preciso fazer a soma de suas medidas; mas como os polígonos deste exercício são regulares, seu perímetro será igual ao tamanho dos lados multiplicado por sua quantidade.

Inicialmente declaramos as variáveis inteiras: `nroLados`, `tamLados` e `perimetro`. Tanto `tamLados` quanto `perimetro` são declaradas com o tipo `long long int`, pois podem ter valores muito grandes, que apenas o tipo de dado `int` não é capaz de armazenar.

```c
    int nroLados;
    long long int  tamLados, perimetro;
```

Então, faremos a leitura dos valores de `nroLados` e `tamLados`, nesta ordem. Note que `%lld` é usado para representar variáveis do tipo `long long int`.

```c
    scanf("%d %lld", &nroLados, &tamLados);
```
Após isso, calcularemos o valor do perímetro

```c
    perimetro = nroLados * tamLados;
```
Por fim, exibimos o resultado recém armazenado em `perimetro`.

```c
    printf("%lld\n", perimetro);
```
 
##### Para aprender um pouco mais sobre tipos de dados: [Tipo de dados em C](http://linguagemc.com.br/tipos-de-dados-em-c/)
 
Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com