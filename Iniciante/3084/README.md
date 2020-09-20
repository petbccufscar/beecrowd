# Problema:
Ezequiel possui um relógio muito antigo e valioso, mas algumas características dele foram perdidas com o passar do tempo. Os ponteiros ainda marcam as horas e os minutos corretamente, mas seus marcadores e números se tornaram ilegíveis.

Ezequiel utiliza um instrumento auxiliar para observar os ângulos formados pelos ponteiros de hora e de minuto. Ele pede para você ajudá-lo escrevendo um programa que indica a hora e o minuto do momento da medição. Considere que às 00:00 os dois ângulos medidos são iguais a zero e que ambos os ponteiros só se movimentam quando se completa uma unidade de tempo (hora ou minuto) correspondente.

**Problema Completo**: https://www.urionlinejudge.com.br/judge/pt/problems/view/3084

# Resolução:

Para resolver este problema, receberemos vários casos de teste com os ângulos formados pelos ponteiros de hora e minuto. Dado isso, faremos um laço de repetição para ler cada caso de teste e dentro desse laço realizaremos a conversão dos ângulos para horas e minutos correspondentes.

Iniciamos declarando as variáveis inteiras `angulo_horas` e `angulo_minutos`, que serão utilizadas para leitura dos ângulos sobre os ponteiros de hora e minuto, respectivamente.  

```c
int angulo_horas, angulo_minutos;
```
No problema, é especificado que os casos de teste são finalizados pelo fim de arquivo (EOF), portanto precisamos ler cada caso até encontrarmos o EOF. Para isso, utilizamos o `while` com o `scanf` como condição, isto é, o `while` só vai parar quando o `scanf` encontrar um EOF.

```c
while(scanf("%d %d", &angulo_horas, &angulo_minutos) != EOF)
``` 

Dessa forma, criamos um laço de repetição que lerá os ângulos formados pelos ponteiros de hora e minuto para cada caso de teste.  

Agora precisamos encontrar as horas e minutos correspondentes, para isso precisamos lembrar que às 00:00 os dois ângulos medidos são iguais a zero e que o intervalo de valor dos ângulos é de 0 a 360. O intervalo de valor das horas no relógio é de 0 a 12 e o de minutos é de 0 a 60. A conversão é a seguinte: 

- Ângulo para hora: `360/12 = 30`, então fazemos `angulo_horas/30` e teremos a hora correspondente. 
- Ângulo para minuto: `360/60 = 6`, então fazemos `angulo_minutos/6` e teremos o minuto correspondente.

Então precisamos fazer essa conversão para cada caso de teste, ou seja, dentro do `while` e apresentar o horário encontrado na forma `hh:mm`. Para isso, fazemos o seguinte:
```c
    printf("%02d:%02d\n", (angulo_horas/30), (angulo_minutos/6));
``` 

Note que utilizamos `%02d` para apresentar os valores, o `2` significa que queremos que o valor ocupe 2 espaços, mesmo que só tenha um dígito e o `0` é o dígito que vamos usar para preencher esse espaço vazio (caso haja). Se usássemos o `%d` normalmente, teríamos o problema de, por exemplo, printar o seguinte: `8:5` quando na verdade queremos que apresente `08:05`. 

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
* [Facebook](https://www.facebook.com/petbcc/),
* [Instagram](https://www.instagram.com/petbcc.ufscar/)
* ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com