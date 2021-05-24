# Problema:

Em cada fase do jogo do Pula Sapo você deve conduzir seu anfíbio através de uma sequência de canos de alturas diferentes até chegar a salvo no cano mais à direita. Entretanto, o sapo só consegue sobreviver se a diferença de altura entre canos consecutivos for de, no máximo, a altura do pulo do sapo. Caso a altura do cano seguinte seja muito alta, o sapo bate no cano e cai. Se a altura do cano seguinte for muito baixa, o sapo não aguenta a queda. O sapo sempre começa em cima do cano mais à esquerda.

Neste jogo, a distância entre os canos é irrelevante, ou seja, o sapo sempre consegue alcançar o próximo cano com um pulo.

Você deve escrever um programa que, dadas as alturas dos canos e a altura do pulo do sapo, mostra se a fase do jogo pode ser vencida ou não.

**Problema completo:** https://www.urionlinejudge.com.br/judge/pt/problems/view/1961

# Resoluçāo:

Nesse problema, para ganhar a fase do jogo é necessário que a diferença entre duas alturas de canos consecutivos não seja maior que a altura do pulo do sapo. Caso contrário, a fase é perdida.

Primeiramente, declaramos as variáveis inteiras: `alturaPulo` para armazenar a altura do pulo do sapo; `nroCanos` que guarda o número de canos que o sapo irá pular; `i` para iteração dentro das estruturas `for`; `diffAlturas` representando o [módulo](https://www.matematica.pt/faq/modulo-numero.php) da diferença entre 2 alturas de canos consecutivos; e `ehGameOver` que indica se houve ou não alguma condição de derrota. 

```c
    int alturaPulo, nroCanos, i;
    int diffAlturas, ehGameOver = 0;
```
Então, faremos a leitura dos valores de `alturaPulo` e `nroCanos`.

```c
    scanf("%d %d", &alturaPulo, &nroCanos);
```

Possuindo os valores das variáveis anteriores, declaramos o vetor `alturaCanos`, que tem a quantidade de `nroCanos`; ele conterá os valores de altura de cada cano que o sapo irá pular.

```c
    int alturaCanos[nroCanos];
```

Assim armazenamos os valores de cada altura dentro do vetor.

```c
    for (i=0; i<nroCanos; i++){
            scanf("%d", &alturaCanos[i]);
    }
```

Após isso, iremos usar um `for` para percorrer todos os canos exceto o último; pois, ao chegar neste, significa que não há um seguinte a ser verificado no calculo da diferença entre alturas.

Para cada iteração verificamos se `diffAlturas` é maior do que `alturaPulo`, ou seja, se o pulo atual foge às condições necessárias. Em caso positivo, significa que a fase do jogo não foi vencida e, assim, o valor de `ehGameOver` é alterado para 1 e usamos o `break` para terminar a execução do `for` (já que não é preciso verificar as próximas alturas). Se a estrutura condicional `if` não for atendida, as iterações continuam normalmente.

```c
    for (i=0; i<nroCanos-1; i++){
        diffAlturas = abs(alturaCanos[i] - alturaCanos[i+1]);
        
        if (diffAlturas > alturaPulo){
            ehGameOver = 1;
            break;
        }    
    }
```

Por fim, exibimos a mensagem de acordo com o valor contido em `ehGameOver`: se for equivalente a zero, a fase foi vencida; se não, foi perdida.

```c
    if(ehGameOver == 0)
        printf("YOU WIN\n");
    else
        printf("GAME OVER\n");
```
 
##### Para aprender um pouco mais sobre vetores: [Vetores](http://linguagemc.com.br/vetores-ou-arrays-em-linguagem-c/)
 
Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
