# Problema: 1071    
Leia 2 valores inteiros X e Y. A seguir, calcule e mostre a soma dos números impares entre eles.

**Problema Completo**: https://www.urionlinejudge.com.br/judge/pt/problems/view/1071


# Resolução:
Para a resolução deste problema iremos receber 2 valores e teremos que percorrer os valores que estão entre estes e realizar a soma, apenas dos ímpares, e ao final imprimir o valor total.

Utilizamos uma variável para utilizar como contador, duas variáveis que irão armazenar os valores que serão passados, uma variável auxiliar a qual usaremos para realizar a inversão entre os valores, e uma variável que irá armazenar a soma final dos valores que são ímpares.
```c
int contador, X, Y, aux, soma;
```

Realizamos a leitura dos valores iniciais que serão passados, isso é feito através da função `scanf`
```c
scanf("%d%d",&X,&Y);
```

Para realizarmos a verificação dos valores que estão entre os valores passados, é necessário sabermos qual destes é o maior, para assim conseguirmos utilizar a função `for` e percorrer os valores. Para isso realizamos a troca de valores, mantendo o menor em `X` e o maior em `Y`.
```c
  if(X>Y){
    aux=X;
    X=Y;
    Y=aux;
  }
```

Após ter deixado o menor valor em `X` e o maior valor em `Y`, iremos percorrer os valores que estão entre estes buscando por valores ímpares, os quais iremos somar e armazenar o valor em `soma`.
```c
  soma=0;
  for(contador=X+1; contador<Y; contador++){
    if(contador%2!=0)
      soma+=contador;
  }
```

Ao final do laço de iterações, imprimimos o valor final encontrado através da função `printf`
```c   
  printf("%d\n",soma);
```

    
Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
