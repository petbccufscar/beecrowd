# Problema:
Júlio está criando um novo Smart Watch especialmente para programadores. É impressionante as vantagens que ele oferece e o conforto pra codar que ele tem. O relógio ainda está em desenvolvimento e ele prometeu consertar os bugs e colocar uns apetrechos melhores e, em troca, pediu um sistema simples para o modo Standy Bay. O problema é que o relógio por si só sempre tem o ângulo de inclinação do Sol/Lua(de 0 a 360). Valendo um relógio, caso deseja aceitar: dada em grau da inclinação do Sol/Lua, informe em qual período do dia ele se encontra.

##### Problema completo: https://www.urionlinejudge.com.br/judge/pt/problems/view/2685

# Resolução:

O objetivo desse exercício é indicar em qual período do dia estamos com base no ângulo de inclinação do Sol/Lua. Se for entre 0 e 90° está de dia, entre 90 e 180° está de tarde, entre 180 e 270° é noite e entre 270 e 360° está de madrugada, como 360° está na mesma posição que 0° em uma circunferência, é considerado de manhã.

Para começar, criamos a variável `m` do tipo `int`:
```c
    int m;
```
`m` representa o ângulo em graus que será usada para indicar o período do dia.

O exercício indica que ele terá vários casos de teste, isso significa que haverão leituras até o final do arquivo [EOF - End of File](https://pt.wikipedia.org/wiki/EOF). Fazemos a leitura do `m` no `scanf` dentro do `while`:
```c
    while (scanf("%d", &m) != EOF) {
```
Dentro do `while`, fazemos a leitura e comparamos ao EOF, portanto o `while` irá rodar até chegar no final do arquivo. Este é simbolizado pela quebra de linha (`\n`). Agora vamos verificar o ângulo dado e indicar qual período do dia ele indica:
```c
      if ((m >= 0) && (m < 90))
        printf("Bom Dia!!\n");
      else if ((m >= 90) && (m < 180))
        printf("Boa Tarde!!\n");
      else if ((m >= 180) && (m < 270))
        printf("Boa Noite!!\n");
      else if ((m >= 270) && (m < 360))
        printf("De Madrugada!!\n");
      else
        printf("Bom Dia!!\n");
    }
```
Separamos 5 situações diferentes para fornecer a resposta:
* O primeiro caso é quando o ângulo está entre 0 e 90 graus (`(m >= 0) && (m < 90)`), aqui escreveremos na tela a mensagem `Bom Dia!!`.
* O segundo caso é quando o ângulo está entre 90 e 180 graus (`(m >= 9) && (m < 180)`), aqui escreveremos na tela a mensagem `Boa Tarde!!`.
* O terceiro caso é quando o ângulo está entre 180 e 270 graus (`(m >= 180) && (m < 270)`), aqui escreveremos na tela a mensagem `Boa Noite!!`.
* O quarto caso é quando o ângulo está entre 0 e 90 graus (`(m >= 270) && (m < 360)`), aqui escreveremos na tela a mensagem `De Madrugada!!`.
* O último caso é quando o ângulo é 360°. Ele mostrará a mensagem `Bom Dia!!`.

##### Para aprender um pouco mais sobre a estrutura while: [While](http://linguagemc.com.br/o-comando-while-em-c/)
##### Para aprender um pouco mais sobre if e else: [Estruturas de decisão](http://linguagemc.com.br/estrutura-de-decisao-if-em-linguagem-c/)

Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
