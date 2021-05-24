# Problema:

A escola pretende trocar o chão de uma sala de aula e o diretor aproveitou para passar uma tarefa aos alunos. A sala tem a forma de um retângulo com L metros de largura e C metros de comprimento, onde L e C são inteiros. O diretor precisa comprar ladrilhos de cerâmica para cobrir todo o chão da sala. Seria fácil calcular quantos ladrilhos seriam necessários se cada ladrilho tivesse 1 metro quadrado. O problema é que o pequeno ladrilho que o diretor quer comprar é um quadrado de 1 metro de diagonal, não de lado. Além disso, ele quer preencher o chão da sala com as diagonais dos ladrilhos alinhadas nas laterais da sala, como na figura.

![Imagem_Da_Descrição](https://resources.urionlinejudge.com.br/gallery/images/problems/UOJ_2786.png)

A loja fornecerá ladrilhos do tipo 1: inteiros; do tipo 2, que são da metade do tipo 1, cortados na diagonal; e ladrilhos do tipo 3, que correspondem à metade do tipo 2. Veja os três tipos de ladrilhos na figura.

É muito claro que 4 ladrilhos do tipo 3 são sempre necessários para os cantos da sala. A tarefa que o diretor passou para os alunos é calcular o número de ladrilhos dos tipos 1 e 2 necessários. Na figura, para L = 3 e C = 5, eram necessários 23 do tipo 1 e 12 do tipo 2. Seu programa precisa calcular, dados os valores de L e C, a quantidade de ladrilhos tipo 1 e tipo 2.

**Problema Completo:** https://www.urionlinejudge.com.br/judge/en/problems/view/2786

# Resolução:

Para resolver este problema apenas utilizamos os comandos `scanf`, `printf` e fazemos um cálculo relativamente simples. Primeiramente, dentro da `int main(){}` devemos declarar as variáveis que serão utilizadas para a resolução deste problema, que no caso são `Largura` e `Comprimento` do tipo inteiro, que receberão seus valores através do comando `scanf`; E as variáveis `tipo1` e `tipo2` também do tipo inteiro, que serão utilizadas para realizar o cálculo e receberão o número de ladrilhos do tipo 1 e tipo 2 necessários.

```c
int Largura,Comprimento,tipo1,tipo2;
```

Após informarmos as variáveis que serão utilizadas dentro da `int main(){}`, usamos o comando `scanf` para informamos as medidas da sala em questão, sendo `Largura` e `Comprimento`, metros de largura e metros de comprimento, respectivamente.

```c
scanf("%d %d",&Largura,&Comprimento);
```

Em seguida, com os valores de `Largura` e `Comprimento` declarados, basta fazermos o cálculo para descobrirmos o número de ladrilhos do tipo 1 e do tipo 2. O cálculo é feito da seguinte forma:

```c
tipo1 = (Largura+Largura-1)*(Comprimento-1)+L;
tipo2 = ((Largura-1)*2) + ((Comprimento-1)*2);
```

E por fim, escrevemos o nosso resultado com o comando `printf`, conforme demonstrado abaixo.

```c
printf("%d\n", tipo1);
printf("%d\n", tipo2);
```
