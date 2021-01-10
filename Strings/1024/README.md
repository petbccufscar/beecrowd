# Problema:

Solicitaram para que você construisse um programa simples de criptografia. Este programa deve possibilitar enviar mensagens codificadas sem que alguém consiga lê-las. O processo é muito simples. São feitas três passadas em todo o texto.

Na primeira passada, somente caracteres que sejam letras minúsculas e maiúsculas devem ser deslocadas 3 posições para a direita, segundo a tabela ASCII: letra 'a' deve virar letra 'd', letra 'y' deve virar caractere '|' e assim sucessivamente. Na segunda passada, a linha deverá ser invertida. Na terceira e última passada, todo e qualquer caractere a partir da metade em diante (truncada) devem ser deslocados uma posição para a esquerda na tabela ASCII. Neste caso, 'b' vira 'a' e 'a' vira '`'.

Por exemplo, se a entrada for “Texto #3”, o primeiro processamento sobre esta entrada deverá produzir “Wh{wr #3”. O resultado do segundo processamento inverte os caracteres e produz “3# rw{hW”. Por último, com o deslocamento dos caracteres da metade em diante, o resultado final deve ser “3# rvzgV”.

**Problema completo:** https://www.urionlinejudge.com.br/judge/pt/problems/view/1024


# Resolução: 
Inicialmente, na função `main`, declaramos as variáveis `n`, do tipo inteiro, que indica a quantidade de linhas a serem tratadas, os contadores `i` e `j`, `palavra`, do tipo ponteiro, que aloca um vetor de char de 1000 posições e `tamanho`, um vetor de tamanho `n`
``` c
    int n, i = 0, j;
    char *palavra = (char *) malloc(sizeof(char) * 1000);
    int tamanho[n];
```

Logo após a declaração, será realizada a leitura da quantidade de linhas.
``` c
    scanf("%d ", &n);
```
Após a leitura, o programa entrará num loop `while`, que rodará enquanto o contador `i` for menor que a quantidade de linhas `n`.
``` c
  	while (i < n)
```

A partir disso o programa irá receber a variável `palavra` por meio da função `gets`.
```c
	 gets(palavra);
	 tamanho[i] = 0;
```

O `tamanho`, por sua vez, será iniciado com o valor 0, seguido por um `while` que irá acrescentar +1 ao `tamanho` enquanto a palavra não chegar ao fim. 
```c
	tamanho[i] = 0;
	while(palavra[tamanho[i]] != '\0')
    	tamanho[i]++;
```

Em seguida, a solução possui um while que percorre os caracteres na tabela ASCII referentes às letras de **a** a **z** e anda três casas para frente.
```c
	    j = 0;            
        while (j < tamanho[i]) {
            if ((palavra[j] >= 97 && palavra[j] <= 122) 
			|| ((palavra[j] >= 65 && palavra[j] <= 90)))
                palavra[j] = (char) (palavra[j] + 3);
            
            j++;
        }
```

Na segunda passada, há um while para que a palavra seja invertida, sendo assim, o primeiro caractere é substituído pelo último, e assim por diante.
```c
        j = 0;
        while (j < tamanho[i] >> 1) {
            
            char letra = palavra[j];
            palavra[j] = palavra[tamanho[i]-j-1];
            palavra[tamanho[i]-j-1] = letra;
            
            j++;
        }
```

Na terceira e última passada, dividimos a palavra na metade em `j = tamanho[i] >> 1` e o caractere é substituído pelo caractere à sua esquerda. Por fim, retorna-se a palavra criptografada.
```c
        j = tamanho[i] >> 1;
        while (j < tamanho[i]) {
            
            palavra[j] = (char) (palavra[j] - 1);
            
            j++;
            
        } 
        printf("%s\n", palavra);   
        i++;
    }
    return 0;
}
```

**Saiba mais sobre ponteiros em: [Endereços e ponteiros](https://www.ime.usp.br/~pf/algoritmos/aulas/pont.html)**

**Saiba mais sobre tabela ASCII em: [Tabela ASCII](https://web.fe.up.pt/~ee96100/projecto/Tabela%20ascii.htm)**

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com