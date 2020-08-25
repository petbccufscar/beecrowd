# Problema:
Novamente Júlio pede sua ajuda, ele esqueceu de um pequeno detalhe. Como o seu o programa anterior só informava uma saudação, ele pediu que transformasse o grau do Sol/Lua em HH:MM:SS. Então caso aceite: dado um grau relativo a posição do Sol/Lua, refaça o sistema só que agora além da saudação de cada período do dia, informe exatamente as horas, os minutos e segundos.

##### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/2686

# Resolução:

Esse exercício é uma continuação do exercício 2685. Seu onbjetivo é indicar em qual período do dia estamos e o horário com base no ângulo de inclinação do Sol/Lua. Se for entre 0 e 90° está de dia, entre 90 e 180° está de tarde, entre 180 e 270° é noite e entre 270 e 360° está de madrugada, como 360° está na mesma posição que 0° em uma circunferência, é considerado de manhã.

Para começar, criamos quatro variáveis, sendo `m` e `tempo` do tipo `float` e `hora` e `minuto` do tipo `int`:
```c
    float m, tempo;
    int hora, minuto;
```
`m` representa o ângulo em graus que será usada para indicar o período do dia, `tempo` indica um valor auxiliar que será convertido em minutos, `hora` e `minuto` representa o tempo descrito pelo ângulo dado em horas e minutos, respectivamente. 

O exercício indica que ele terá vários casos de teste, isso significa que haverão leituras até o final do arquivo [EOF - End of File](https://pt.wikipedia.org/wiki/EOF). Fazemos a leitura do `m` no `scanf` dentro do `while`:
```c
    while (scanf("%f", &m) != EOF) {
```
Dentro do `while`, fazemos a leitura e comparamos ao EOF, portanto o `while` irá rodar até chegar no final do arquivo. Este é simbolizado pela quebra de linha (`\n`). Agora vamos verificar o ângulo dado e determinar o horário que ele representa:
```c
      if (m < 90) {
        printf("Bom Dia!!\n");
```
Sabemos que o ângulo sempre será um valor entre 0 e 360 graus. Com isso verificamos se `m` é menor que 90 (`m < 90`) e, se for, mostramos a mensagem `Bom Dia!!`. Agora precisamos calcular a hora do dia:
```c 
        hora = 6;
        tempo = m/0.5;
        minuto = tempo*2;
            
        if (minuto >= 60) {
          hora = hora + (minuto/60);
          minuto = minuto%60;
        }
        printf("%02d:%02d:00\n", hora, minuto);
      }
```
Como está de dia, o horário deve estar entre 6 da manhã e meio-dia (12:00), por isso igualamos `hora` a 6. Em seguida calculamos quantos minuto a mais o ângulo indica. Analisando os casos de teste presentes no enunciado, descobrimos que 0,5° equivale a 2 minutos. Com isso, descobrimos quantos minutos temos dividindo `m` por 0,5 (`tempo = m/0.5`) e depois multiplicando o valor obtido por 2 (`minuto = tempo*2`). Agora resta descobrir o valor de `hora`:
```c            
        if (minuto >= 60) {
          hora = hora + (minuto/60);
          minuto = minuto%60;
        }
        printf("%02d:%02d:00\n", hora, minuto);
      }
```
Como 60 minutos equivalem a 1 hora, adicionamos na variável `hora` o resultado inteiro da divisão de `minuto` por 60. O resto dessa divisão pode ser obtido usando `%` e representará o tempo em minutos que vai aparecer na tela. Para apresentar o resultado usamos `printf` e, para que apareçam dois dígitos para os valores de hora e minuto na tela, fazemos `%02d`. O valor de segundos será sempre 00.

Para os períodos de tarde, noite e madrugada, o cálculo do horário funciona praticamente da mesma forma:
```c
      else if (m < 180) {
        printf("Boa Tarde!!\n");
        
        hora = 12;
        m = m-90;
        tempo = m/0.5;
        minuto = tempo*2;
            
        if (minuto >= 60) {
          hora = hora + (minuto/60);
          minuto = minuto%60;
        }
        printf("%02d:%02d:00\n", hora, minuto);
      }
```
No caso do período de tarde (quando `m` está entre 90 e 180), mostramos a mensagem `Boa Tarde!!` na tela, igualamos `hora` a 12 e subtraímos 90 do valor de `m` para não contar horas a mais.
```c
      else if (m < 270) {
        printf("Boa Noite!!\n");
        
        hora = 18;
        m = m-180;
        tempo = m/0.5;
        minuto = tempo*2;
            
        if (minuto >= 60) {
          hora = hora + (minuto/60);
          minuto = minuto%60;
        }
        printf("%02d:%02d:00\n", hora, minuto);
      }
```
No caso do período de noite (quando `m` está entre 180 e 270), mostramos a mensagem `Boa Noite!!` na tela, igualamos `hora` a 18 e subtraímos 180 do valor de `m` para não contar horas a mais.
```c
      else if (m < 360) {
        printf("De Madrugada!!\n");
        
        hora = 0;
        m = m-270;
        tempo = m/0.5;
        minuto = tempo*2;
            
        if (minuto >= 60) {
          hora = hora + (minuto/60);
          minuto = minuto%60;
        }
        printf("%02d:%02d:00\n", hora, minuto);
      }
```
No caso do período de madrugada (quando `m` está entre 270 e 360), mostramos a mensagem `De Madrugada!!` na tela, igualamos `hora` a 0 e subtraímos 270 do valor de `m` para não contar horas a mais.

O caso final é se `m` for 360. Como a posição 360° equivale à posição 0° em uma circunferência, mostramos na tela a mensagem `Bom Dia!!` e o horário `06:00:00`.
```c
      else
        printf("Bom Dia!!\n06:00:00\n");
    }
```
A chave no final serve para fechar o `while` do começo do código.

##### Para aprender um pouco mais sobre a estrutura while: [While](http://linguagemc.com.br/o-comando-while-em-c/)
##### Para aprender um pouco mais sobre if e else: [Estruturas de decisão](http://linguagemc.com.br/estrutura-de-decisao-if-em-linguagem-c/)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
