# Problema

Você deve fazer um programa que apresente a sequencia conforme o exemplo abaixo.

I=0 J=1

I=0 J=2

I=0 J=3

I=0.2 J=1.2

I=0.2 J=2.2

I=0.2 J=3.2

.....

I=2 J=?

I=2 J=?

I=2 J=?


**Problema completo**: https://www.urionlinejudge.com.br/judge/pt/problems/view/1098

# Resolução

Analisando a sequência de saída, identificamos 2 pontos que são cruciais para resolução do exercício

* I se mantêm constante por 3 linhas 
* J assume 3 valores para o mesmo valor de `i` (j,j+1,j+2)
* Quando `i` se altera (+0.2), J também recebe a mesma alteração
* Temos duas formas de `printf`, uma apenas o número inteiro e uma com uma casa depois da vírgula.

Temos então, "bloquinhos" em que esse padrão se repete (a cada 3 linhas) e isso nos guiará pelo exercício.  

Primeiro vamos declar as variáveis a serem utilizadas neste problema, teremos 1 variável `double`, `i` para armazenar valores reais e duas auxiliares do tipo `int`, `k` e `contador`.

Note que já definimos o valor inicial da variável `i`, assim como mostra na saída do exercicio.

```c
    double i = 0;
    int k, contador;
``` 

Analisando a saída do exercício, podemos ver que nosso ponto de parada pode ficar por conta do `i`. Portanto, executaremos até que `i` assuma um valor maior que 2, aumentando de 0.2 em 0.2, como mostra a sequência de saída.

```c
    while(i < 2){
        /*
            ...
        */
       i += 0.2;
    }
```

Note que usamos uma forma "[abreviada]"(https://pt.wikibooks.org/wiki/Programar_em_C/Opera%C3%A7%C3%B5es_matem%C3%A1ticas_(B%C3%A1sico)) da soma, i += 0.2 é o mesmo que i = i + 0.2

Dentro desse loop `while` iremos fazer a variação do valor J. Para isso, precisaremos de mais um loop que repita 3 vezes para cada valor de `i`, usaremos para isso o loop `for`.

Analisando melhor a variação de J, podemos reescrevê-la como: (i+1), (i+2) e (i+3), que são os valores que `k` pode assumir no loop interno (`for(k=1;k<=3;k++)`). Assim, podemos escrever os valores de J como `(i+k)`.  

O problema define que temos que escrever o número como inteiro quando ele atingir valores inteiros (0 na primeira casa decimal), e com 1 casa decimal quando tiver casas decimais diferentes de 0. 

Para isso, usaremos a variável `contador` que nos auxiliará nisso. Para cada acréscimo +0.2 em `i`, teremos também +1 no `contador`, portanto, a cada 5 vezes que o loop interno é realizado (`i` chega ao próximo número inteiro [5*0.2]), devemos escrever sem casas decimais, o que pode ser verificado se `contador%5 == 0`. Veja que no primeiro caso temos (0%5 == 0) e para quando o `i` está em 1, o `contador` estará em 5, assim, (5%5 == 0).   
```c
     while(i<2){
        for(k=1;k<=3;k++){ 
            if (contador%5 == 0)
                printf("I=%.0lf J=%.0lf\n",i,(i+k));
            else
                printf("I=%.1lf J=%.1lf\n",i,(i+k));
        }
        contador += 1;
        i += 0.2;    
    }
```

Isso nos leva a saída igual a proposta pelo exercício, já que para cada valor de `i`, iremos escrever 3 valores de J e só ai, somaremos 0.2 em `i` e atualizaremos nosso `contador`.



##### Para entender um pouco mais sobre os loops utilizados: [Loops](https://blog.masterdaweb.com/programacao-1/linguagem-c/loop-for-while-e-do-while-em-linguagem-c/)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com