# Problema

Leia 2 valores inteiros (A e B). Após, o programa deve mostrar uma mensagem "Sao Multiplos" ou "Nao sao Multiplos", indicando se os valores lidos são múltiplos entre si.

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/1044

# Resolução

Sempre lembrar de inserir as bibliotecas padrões:
```c
        #include <stdio.h>
        #include <stdlib.h>
```
O problema pede para ler dois valores inteiros A e B, portanto usamos int:
```c
        int A,B;
	    scanf("%d%d", &A, &B);
```
Começamos verificando se alguma das variáveis são iguais a 0, pois essa não é um condição aceitável devido 0 ser múltiplo de todos os números naturais:
```c
        if (B==0||A==0)
        {
            return 0;   //Caso um deles seja igual a 0 o codigo eh finalizado
        }
```
Faremos a verifição se os números são múltiplos ou não usando if e else:
**OBS:**[Condição para números serem múltiplos](https://alunosonline.uol.com.br/matematica/divisibilidade-multiplos-e-divisores.html)
```c
        if (((A%B)==0||(B%A)==0))  //A "%" representa o resta da divisao, que no caso de ser igual a 0 ira representar que sao multiplos
        {
            printf("Sao Multiplos\n");
        }
        else                       //Se esse resto for diferente de 0 eles nao sao multiplos     
        {
            printf("Nao sao Multiplos\n");
        }
```
Sempre lembre de finalizar o código:
```c
        return 0;
```

##### Para aprender mais sobre Operadores: 
[Operadores em C](https://www.tutorialspoint.com/cprogramming/c_operators.htm)


