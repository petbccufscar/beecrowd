# Problema

Faça um programa que leia um vetor N[20]. Troque a seguir, o primeiro elemento com o último, o segundo elemento com o penúltimo, etc., até trocar o 10º com o 11º. Mostre o vetor modificado.

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/1175

# Resolução

O exercício pede uma solução para inverter a última possição com a primeira e repetir essa ação pras outras até atingir o ponto médio que é no caso 10ª e 11ª posição:

                                0
                                -5
                                ...
                                63
                                230

Portanto a saída do exercício fica com essa característica:        

                                N[0] = 230
                                N[1] = 63
                                ...
                                N[18] = -5
                                N[19] = 0

Iremos iniciar o exercício declarando as variáveis que iremos usar, incluindo o [vetor](http://linguagemc.com.br/vetores-ou-arrays-em-linguagem-c/#:~:text=O%20vetor%20é%20uma%20estrutura,inteiro%20denominado%20índice%20do%20vetor.) `N[20]` que também deve possuir um tipo e no caso do exercício em questão é `int`:
```c
        int N[20], aux,i, j;
```
Faremos a leitura dos valores que o vetor `N[20]` irá receber:

```c
        for(i=0; i<20; i++)
                scanf("%d",&N[i]);
```
Damos sequência para onde a lógica do exercício se estabelece, iniciamos fazendo a atribuição `j=19` e isso é com intuito de podermos acessar a última posição do vetor `N` e depois seguimos para o `for`:

```c
        j=19;
        for(i=0; i<10; i++)
        {
                aux=N[i];
                N[i]=N[j];
                N[j]=aux;
                j--;
        }

    
```
No `for` será feita uma troca de variável padrão utilizando uma variável `aux` como auxiliar, a única diferança de uma troca padrão de variável é que estamos trabalhando com vetor e precisamos ficar atentos à posição do mesmo e para isso utilizamos ambas as variáveis `i` e `j`, sendo `i` a que irá percorrer o vetor do inicio `N[0]` e `j` como explicado anteriormente do final `N[19]`. Repare que o `for` só percorre metade do vetor `N[20]` e isso é devido à condição de parada explicada no início do exercício, ponto médio.

E para finalizar precisamos mostrar a saída e para isso devemos utilizar um `for` para percorrer todo o vetor printando em cada posição que é representada por `i`:

```c
        for(i=0; i<20; i++)
                printf("N[%d] = %d\n",i,N[i]);

```


Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para petbcc.ufscar@gmail.com



