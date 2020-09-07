# Problema:

O seu professor de programação gostaria que você fizesse um programa com as seguintes características:

1. Coloque sete espaços em branco e coloque o caractere 'A';
2. Coloque seis espaços em branco e coloque o caractere 'B', um espaço em branco e o caractere 'B';
3. Coloque cinco espaços em branco e coloque o caractere 'C', três espaço em branco e o caractere 'C';
4. Coloque quatro espaços em branco e coloque o caractere 'D', cinco espaço em branco e o caractere 'D';
5. Coloque três espaços em branco e coloque o caractere 'E', sete espaço em branco e o caractere 'E';
6. Repita o procedimento 4;
7. Repita o procedimento 3;
8. Repita o procedimento 2;
9. Repita o procedimento 1.

Exemplo de Saída:

                        	
       A
      B B
     C   C
    D     D
   E       E	
    D     D
     C   C
      B B
       A

###### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/2756

# Resolução

O exercício se resume em seguir os passos oferecidos por ele para exibir a saída desejada.

1. Coloque sete espaços em branco e coloque o caractere 'A':
**OBS:** Tenha em mente sempre utilizar a quebra de linha `\n`.
```c
       printf("       A\n");   
```

2. Coloque seis espaços em branco e coloque o caractere 'B', um espaço em branco e o caractere 'B':

```c
        printf("      B B\n");
```
3. Coloque cinco espaços em branco e coloque o caractere 'C', três espaço em branco e o caractere 'C':

```c
        printf("     C   C\n");
```
4. Coloque quatro espaços em branco e coloque o caractere 'D', cinco espaço em branco e o caractere 'D'    

```c
        printf("    D     D\n");
```

5. Coloque três espaços em branco e coloque o caractere 'E', sete espaço em branco e o caractere 'E':

```c
        printf("   E       E\n");
```

As instruções 6, 7, 8 e 9 são as repetições das instruções anteriores, a única diferença é que as letras devem aparecer na posição invertida começando pela 4, e com isso terminamos o exercício.

```c
        printf("    D     D\n");
        printf("     C   C\n");
        printf("      B B\n");
        printf("       A\n");
```


Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para petbcc.ufscar@gmail.com