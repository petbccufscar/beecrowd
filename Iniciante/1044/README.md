# Problema

Leia 2 valores inteiros (A e B). Após, o programa deve mostrar uma mensagem "Sao Multiplos" ou "Nao sao Multiplos", indicando se os valores lidos são múltiplos entre si.

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/1044

# Resolução

O problema pede para ler dois valores inteiros A e B, portanto usamos int:
```c
        int A,B;
	    scanf("%d%d", &A, &B);
```
Começamos verificando se alguma das variáveis são iguais a 0, pois essa não é um condição aceitável devido 0 ser múltiplo de todos os números naturais:
```c
        if (B==0||A==0)
        {
            return 0;   
        }
```
A verificação é feita com um dos [Operadores Lógicos em C](http://linguagemc.com.br/operadores-logicos-em-c/#:~:text=Os%20operadores%20lógicos%20são%20utilizados,condições%20simples%20em%20expressões%20lógicas.) que represeta o igual no caso "==". Caso a condição do if for aceita/verdade ele irá retornar 0 o que faz com que o código termine nesse ponto.

Faremos a verifição se os números são múltiplos ou não usando if e else:
**OBS:**[Condição para números serem múltiplos](https://alunosonline.uol.com.br/matematica/divisibilidade-multiplos-e-divisores.html)

```c
        if (((A%B)==0||(B%A)==0))  
        {
            printf("Sao Multiplos\n");
        }
        else                           
        {
            printf("Nao sao Multiplos\n");
        }
```
A [porcentagem - "%"](http://linguagemc.com.br/resto-de-uma-divisao-inteira-em-c/) representa o resta da divisão, que no caso de ser igual a 0 irá representar que são múltiplos.
Se não(else). Caso esse resto for diferente de 0 eles não são múltiplos 

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para petbcc.ufscar@gmail.com




