# Problema:

Imprima uma linha contendo o número da pessoa que Theon deve dizer ser seu algoz. 

**Problema completo:** https://www.urionlinejudge.com.br/judge/pt/problems/view/1858

# Resoluçāo:

Ao ler de primeira pode parecer confuso, no entanto a ideia é mostrar a posiçāo que está o algoz de Theon, que é o menor número dos N inteiros T1, T2, ..., Tn.

Inicialmente declaramos as variáveis `n`, `i`, `algoz`, `menor` e `*v`. Em que `n` é a quantidade de algozes, `i` é usada para fazer iterações no for, `algoz` armazena a posição do algoz, `*v` é um ponteiro para um vetor que guarda os valores em que Theon pode ser atingido e menor irá armazenar o menor valor de `*v`.

```c
   int n, i, algoz = 0, menor = 999;
   int *v;
```


Em seguida, faremos a leitura do valor de `n` e a alocação de `*v`.

```c
scanf("%d",&n);
v = (int *) malloc(n * sizeof(int));
```

Após o passo anterior, iremos ter os valores de entrada da segunda linha, e para cada valor lido é feita uma comparaçāo a fim de que `menor` possua o menor valor. Caso `v[i] < menor`, menor irá receber o valor de `v[i]` e `algoz` terá seu valor alterado, como a posiçāo é iniciada em 1, adicionamos 1 a `i`.


```c
    for (i=0;i<n;i++){
            scanf("%d",&v[i]);
            if(v[i] < menor){
                menor = v[i];
                algoz = i + 1;
            }
        }
```
Por fim, exibimos a posiçāo do algoz. 

```c
    printf("%d\n",algoz);
```

 
##### Para aprender um pouco mais sobre o laço de repetição for: [For](http://linguagemc.com.br/a-estrutura-de-repeticao-for-em-c/)
 
##### Para aprender um pouco mais sobre alocação dinâmica: [Alocação](http://linguagemc.com.br/alocacao-dinamica-de-memoria-em-c/)

 
Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com