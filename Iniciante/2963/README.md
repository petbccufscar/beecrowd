# Problema 

O Reino dos Emparelhamentos é governado por um generoso Comendador. A fama do Comendador e de suas grandes qualidades é conhecida por todos, inclusive em reinos vizinhos. Uma de suas mais famosas qualidades é seu bom humor, que é nutrido diariamente por um bobo da corte, eleito anualmente no Grande Concurso de Comédia (GCC) do reino. O bobo da corte ajuda a aliviar as tensões das diversas reuniões polı́ticas que o cargo exige, alegrando não só o Comendador como também todo o reino.

O jovem Carlos é um grande comediante cujo sonho é se tornar bobo da corte na próxima tem- porada. Ele passou os últimos meses anotando piadas e trocadilhos dos mais diversos tipos, muitos dos quais sobre sua própria (diminuta) estatura. Chegou a época da eleição do bobo da corte, e um total de N candidatos se inscreveram. Cada um dos candidatos terá cinco minutos para se apresentar perante uma platéia. Após as apresentações, cada cidadão do Reino dos Emparelhamentos poderá votar em um dos candidatos, e o mais votado será o novo bobo da corte. Caso haja empate entre um ou mais candidatos, aquele que tiver feito a inscrição primeiro é eleito. Sabendo disso, o jovem Carlos passou noites na frente do escritório eleitoral e garantiu que sua inscrição fosse a primeira a ser feita.

Após a votação, resta apenas apurar os resultados. A urna eletrônica gera um relatório com N inteiros, correspondentes ao número de votos de cada candidato, ordenados pela ordem de inscrição. Sua missão é determinar se o jovem Carlos foi eleito ou não.
#### Problema completo: [https://www.urionlinejudge.com.br/judge/pt/problems/view/2963]

# Resolução

De início declaramos as variáveis que iremos usar no problema: `candidatos` que receberá a quantidade de candidatos concorrendo; `carlos` que receberá a quantidade de votos que Carlos teve; `outros_votos` que irá receber os valores dos votos recebidos por cada um dos outros candidatos.
``` c
        int candidatos, carlos, outros_votos;
```

Agora, leremos os valores de `candidatos` e `carlos` através da função `scanf`. Em seguida, descontamos 1 de `candidatos`, pois já recebemos os votos de Carlos.
``` c
    scanf("%d %d", &candidatos, &carlos);
    candidatos = candidatos - 1;
```
Dando continuidade, fazemos um loop `while` que enquanto receberá como condição `candidatos--`, isso faz com que a variável seja descontada em 1 a cada iteração do loop e, quando ela atingir o valor de 0, o loop será fechado. Sendo assim, recebemos em `outros_votos` os votos dos candidatos individualmente. Na sequência, comparamos o voto do candidato em questão com o de Carlos, se ele for maior, `carlos` receberá o valor de -1 para servir de controle na estrutura de condição que usaremos futuramente. 
``` c
    while (candidatos--) {
        scanf("%d", &outros_votos);
        if (outros_votos>carlos) {
            carlos = -1;
        }
    }
```

Por fim, fazemos um estrutura condicional `if`, onde se `carlos` for maior que -1 imprimos a mensagem: "S", através de uma função `printf`. Ademais, usamos um `else` caso `carlos` seja = -1 e imprimos "N". 
``` c
if (carlos > -1) {
        printf("S\n");
    }
    else {
        printf("N\n");
    }
``` 

