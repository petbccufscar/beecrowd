# Problema:

A ECI (Editio Chronica Incredibilis ou Editora de Crônicas Incríveis) é muito tradicional quando se trata de numerar as páginas de seus livros. Ela sempre usa a numeração romana para isso. E seus livros nunca ultrapassam as 999 páginas pois, quando necessário, dividem o livro em volumes.

Você deve escrever um programa que, dado um número arábico, mostra seu equivalente na numeração romana.

Lembre que I representa 1, V é 5, X é 10, L é 50, C é 100, D é 500 e M representa 1000.

Você deve escrever um programa que, dado um número arábico, mostra seu equivalente na [numeração romana](https://brasilescola.uol.com.br/matematica/algarismos-romanos.htm).

**Problema completo:** https://www.urionlinejudge.com.br/judge/pt/problems/view/1960

# Resoluçāo:

A ideia desse modo de resolução é achar o valor posicional da centena, dezena e unidade pertencentes a entrada do problema (`nroArabico`) para, em seguida, utilizá-lo como índice nos vetores: `*unidades`, `*dezenas` e `*centenas`. Estes possuem, respectivamente, os valores das unidades, dezenas e centenas em algarismos romanos, possibilitando que retornem o número romano correspondente. Tendo pré-armazenado as numerações romanas de centena, dezena e unidade; usamos uma função para poder juntar esses valores e mostrar o resultado convertido.

Para achar o valor posicional da centena, dividimos a entrada por 100. A dezena é encontrada dividindo o resto do cálculo anterior (pois assim sabemos qual o restante que ainda precisa ser convertido) por 10. Por fim, a unidade é obtida através do resto do cálculo da dezena.   

Primeiramente, como usaremos alocação dinâmica devido ao fato de trabalharmos com uma variável que seu tamanho muda conforme a entrada, importaremos a biblioteca `stdlib.h`; e como iremos trabalhar com strings, devemos também importar a biblioteca [`string.h`](http://linguagemc.com.br/a-biblioteca-string-h/).

```c
    #include <stdlib.h>
    #include <string.h>
```

Para iniciar, iremos declarar as variáveis inteiras: `nroArabico` (encarregada de guardar o número arábico fornecido na entrada);`indiceCentena`, `indiceDezena` e `indiceUnidade` (responsáveis por armazenar, respectivamente, a centena, dezena e unidade do número em questão).

```c
    int nroArabico;
    int indiceCentena, indiceDezena, indiceUnidade;  
```

Também iremos declarar 3 vetores de caracteres (`*unidades`, `*dezenas` e `*centenas`) que possuem os valores das unidades, dezenas e centenas em números romanos. Estas 3 variáveis são declaradas como ponteiros de caracteres pois armazenam caracteres que estão justapostos, ou seja, strings.

```c
    char *unidades[11] = {"","I","II","III","IV","V","VI","VII","VIII","IX","\0"};
    char *dezenas[11] = {"","X","XX","XXX","XL","L","LX","LXX","LXXX","XC","\0"};
    char *centenas[11] = {"","C","CC","CCC","CD","D","DC","DCC","DCCC","CM","\0"};
```

A última variável a ser declarada é `*nroRomano`. Sua função é armazenar o número romano resultante, que é a saída do problema. Além disso, como o tamanho desta varia conforme a entrada, usamos a função `malloc` da biblioteca `stdlib.h` para realizar a alocação dinâmica da variável. Colocamos com tamanho de 12, pois é o tamanho máximo que `*nroRomano` poderá ter.

```c
    char *nroRomano;
    nroRomano = (char *)malloc(12*sizeof(char));
```

Então, faremos a leitura do número arábico.

```c
    scanf("%d",&nroArabico);
```
Tendo esse valor guardado, é preciso achar o valor posicional da centena, dezena e unidade. 

```c
    indiceCentena = nroArabico/100;
    nroArabico = nroArabico%100;
    
    indiceDezena = nroArabico/10;
    indiceUnidade = nroArabico%10;
    
```

Após isso, utilizamos a função `strcat` para poder concatenar (ou seja, "juntar") os conteúdos da centena, dezena e unidade com a variável `nroRomano`.  

```c
    strcat(nroRomano, centenas[indiceCentena]);
    strcat(nroRomano, dezenas[indiceDezena]);
    strcat(nroRomano, unidades[indiceUnidade]);
```

Ao final, exibimos o resultado. 

```c
   printf("%s\n", nroRomano); 
```
 
##### Para aprender um pouco mais sobre vetor de caracteres: [Vetor de caracteres](http://linguagemc.com.br/string-em-c-vetor-de-caracteres/)

##### Para aprender um pouco mais sobre alocação dinâmica: [Alocação dinâmica](http://linguagemc.com.br/alocacao-dinamica-de-memoria-em-c/)
 
Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
