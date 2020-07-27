# Problema

Você deve fazer um programa que apresente a sequencia conforme o exemplo abaixo.

I=1 J=7

I=1 J=6

I=1 J=5

I=3 J=9

I=3 J=8

I=3 J=7

...

I=9 J=15

I=9 J=14

I=9 J=13


**Problema completo**: https://www.urionlinejudge.com.br/judge/pt/problems/view/1097

# Resolução

Analisando a sequência de saída, identificamos 2 pontos que são cruciais para resolução do exercício

* I se mantêm constante por 3 linhas 
* J decai uma unidade a cada `printf` feito. Porém quando o `i` é alterado (+2), `j` faz o mesmo, comparado ao ´j´ inicial (antes de decair).   

Temos então, "bloquinhos" em que esse padrão se repete (a cada 3 linhas) e isso nos guiará pelo exercício.  

Primeiro vamos declar as variáveis a serem utilizadas neste problema, todas as variáveis serão inteiras dado que na saída do exercício vemos apenas números inteiros, ou seja `int`. 

Note que já definimos o valor inicial das variáveis `i` e `j`, assim como mostra na saída do exercicio.

```c
    int i = 1, j = 7;
    int k;
``` 

Analisando a saída do exercício, podemos ver que nosso ponto de parada pode ficar por conta do `i` já que `j` assume valores maiores e decai, o que poderia nos levar a problemas de lógica. Portanto, executaremos até que `i` assuma um valor maior que 9, aumentando de 2 em 2, como mostra a sequência de saída.

```c
    while(i <= 9){
        /*
            ...
        */
       i += 2;
    }
```

Note que usamos uma forma "[abreviada]"(https://pt.wikibooks.org/wiki/Programar_em_C/Opera%C3%A7%C3%B5es_matem%C3%A1ticas_(B%C3%A1sico)) da soma, i += 2 é o mesmo que i = i + 2.

Dentro desse loop `while` iremos fazer a variação de `j`. Para isso, precisaremos de mais um loop que repita 3 vezes um `printf`, usaremos para isso o loop `for`.

Analisando melhor a variação de `j`, podemos reescrevê-la como: (7-0), (7-1) e (7-2), que são os valores que `k` assume no loop interno. Assim, podemos escrever os valores de J como `(j-k)`.  

Note que não alteramos o valor de `j` durante o loop interno, portanto ele permanece com seu valor inicial. Assim, precisamos apenas somar 2 em seu valor total após o termino do loop interno para chegar no próximo "bloco" padrão da saída. 

```c
    while(i<=9){
        for(k=0;k<3;k++){
            printf("I=%d J=%d\n",i,(j-k));
        }
        i += 2;
        j += 2;
    }
```

Isso nos leva a saída igual a proposta pelo exercício, já que para cada valor de `i`, iremos escrever 3 valores de `j` e só ai, iremos somar 2 em `i` e `j` e passar ao próximo "bloco".



##### Para entender um pouco mais sobre os loops utilizados: [Loops](https://blog.masterdaweb.com/programacao-1/linguagem-c/loop-for-while-e-do-while-em-linguagem-c/)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com