# Problema:   
O seu professor gostaria de fazer um programa com as seguintes características:

1. Leia uma data no formato DD/MM/AA;
2. Imprima a data no formato MM/DD/AA;
3. Imprima a data no formato AA/MM/DD;
4. Imprima a data no formato DD-MM-AA.

**Problema Completo**: https://www.urionlinejudge.com.br/judge/pt/problems/view/2764

# Resolução:

Iniciaremos a resolução deste problema declarando as variaveis que iremos utilizar, serão 3 variaveis do tipo inteiro onde iremos armazenar os valores correspondentes as datas que iremos receber como entrada
```c
  int dia, mes, ano;
```

Durante a nossa leitura através da função `scanf` ao deparar com um caractere "/" ele irá interromper a leitura e ira procurar por novos valores, salvando estes em cada variavel, dividindo em 3 blocos de numeros inteiros
```c
	scanf("%d/%d/%d", &dia, &mes, &ano);
```

Após realizada a leitura dos 3 valores inteiros iremos apenas imprimir estes seguindo a formatação proposta pelo problema
```c
  printf("%02d/%02d/%02d\n", mes, dia, ano);
  printf("%02d/%02d/%02d\n", ano, mes, dia);
  printf("%02d-%02d-%02d\n", dia, mes, ano);
```

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com