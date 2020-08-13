# Problema:   
Paulo e Pedro fizeram uma longa jornada desde que partiram do Brasil para competir na Final Mundial da Maratona, em Phuket, Tailândia. Notaram que a cada escala que faziam, tinham que ajustar seus relógios por causa do fuso horário.

Assim, para melhor se organizarem para as próximas viagens, eles pediram que você faça um aplicativo para celular que, dada a hora de saída, tempo de viagem e o fuso do destino com relação à origem, você informe a hora de chegada de cada vôo no destino.

Por exemplo, se eles partiram às 10 horas da manhã para uma viagem de 4 horas rumo a um destino que fica à leste, em um fuso horário com uma hora a mais com relação ao fuso horário do ponto de partida, a hora de chegada terá que ser: 10 horas + 4 horas de viagem + 1 hora de deslocamento pelo fuso, ou seja, chegarão às 15 horas. Note que se a hora calculada for igual a 24, seu programa deverá imprimir 0 (zero).

**Problema Completo**: https://www.urionlinejudge.com.br/judge/pt/problems/view/2057

# Resolução:

Para a resolução deste problema iniciaremos declarando as variaveis, estas irão armazenar os valores que serão passados, dentre essas o horário de saida, o tempo de voo e a alteração fuso em relação à origem. Logo após ja realizamos a leitura destes valores através da função `scanf`
```c
int saida, voo, fuso, chegada;

scanf("%d %d %d", &saida, &voo, &fuso);
```


Sobre o horario de saida, iremos tratar "0 horas" como "24 horas", pois se o valor contido em `fuso` for maior que o de `voo` poderiamos ter um valor negativo como resultado
```c
if(saida == 0)
	saida = 24;
```


Para calcularmos a saida, basta somar o horario de saida com o tempo de voo e ajustar com o fuso. Caso o valor resultante seja maior que 24 pegaremos o resto da divisão por 24, que indicaria ter passado o dia. Após isso realizamos a impressão do valor encontrador que será o horário de chegada
```c
chegada = ((saida + voo + fuso) % 24);

printf("%d\n", chegada);
```



Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com