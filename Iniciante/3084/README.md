# Problema:
Ezequiel possui um relógio muito antigo e valioso, mas algumas características dele foram perdidas com o passar do tempo. Os ponteiros ainda marcam as horas e os minutos corretamente, mas seus marcadores e números se tornaram ilegíveis.

Ezequiel utiliza um instrumento auxiliar para observar os ângulos formados pelos ponteiros de hora e de minuto. Ele pede para você ajudá-lo escrevendo um programa que indica a hora e o minuto do momento da medição. Considere que às 00:00 os dois ângulos medidos são iguais a zero e que ambos os ponteiros só se movimentam quando se completa uma unidade de tempo (hora ou minuto) correspondente.

**Problema Completo**: https://www.urionlinejudge.com.br/judge/pt/problems/view/3084

# Resolução:

Iniciamos declarando as varíaveis inteiras "horas" e "minutos", que serão utilizadas para leitura dos ângulos sobre os ponteiros de hora e minuto, respectivamente.  

```c
int horas, minutos;
```

A entrada do programa consiste em vários casos de teste, portanto precisamos de um laço de repetição para a leitura de cada caso. No problema, é especificado que os casos de teste são finalizados pelo fim de arquivo (EOF), portanto precisamos ler cada caso até encontrarmos o EOF. Para cada caso de teste, precisamos resolver o problema proposto. 
Lembre-se que horas e minutos são dois inteiros tais que (0 ≤ horas, minutos < 360). O relógio clássico só tem 12 valores, portanto precisamos dividir os valores dos ângulos para que sejam no máximo 12, para isso divimos esses valores por 30 (360/30 = 12). É só isso que precisamos para encontrar as horas, porém para encontrar os minutos ainda precisamos multiplicar o valor encontrado por 5. No caso dos minutos, já que precisamos dividir por 30 e depois multiplicar por 5, essas operações são equivalentes a apenas dividir por 6, portanto é mais simples apenas fazer a divisão por 6. Após isso, resta apenas printar a resposta no formato pedido no exercício, podemos fazer de forma bem simples:

```c
while(scanf("%d %d", &horas, &minutos) != EOF)
    printf("%02d:%02d\n", (horas/30), (minutos/6));
``` 

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com