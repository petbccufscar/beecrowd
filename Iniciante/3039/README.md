# Problema:

 Papai Noel todo ano lê as cartinhas de Natal para saber o que dar de presente para cada criança. O problema é que muitas crianças não mandam suas cartinhas para o Papai Noel. Então ele decidiu que, para poupar o seu tempo, ele irá dar o mesmo presente para crianças que não mandaram cartinhas. Assim, ele decidiu que para os meninos ele irá dar um carrinho de brinquedo e para as meninas, uma boneca.

**Problema completo:** https://www.urionlinejudge.com.br/judge/pt/problems/view/3039

# Resoluçāo:

A solução deste exercício consiste em ler o caractere de entrada que corresponde ao gênero da criança, e verificar se o gênero dela é masculino ou feminino. A partir dessa informação, iremos acrescentar a quantidade de carrinhos, caso a criança seja do gênero masculino, e de bonecas se for do gênero feminino.

Primeiramente, iremos importar a biblioteca `stdlib.h`, pois utilizarmos a função `malloc()` para fazer alocação dinâmica.
```c
    #include <stdlib.h>
```

Então, iremos declarar as nossas variáveis inteiras. O inteiro `n` é o número de casos em que iremos analizar, `i` é uma variável auxiliar para laços, `carrinho` e `boneca` são variável que serão utilizadas para incrementar a quantidade de carrinhos e bonecas, respectivamente.

É preciso alocar dinamicamente a variável `*nome`, pois não sabemos previamente o tamanho dela, usamos ela para guardar o nome da criança. O caractere `genero` armazena o gênero da criança.
```c
    int n, i, carrinho, boneca;
    char *nome = (char*) malloc(sizeof(char));
    char genero;
```

Atribuímos 0 em ambas variáveis incrementadoras e usamos um `scanf` para guardar o valor de `n`.

```c
    carrinho = 0;
    boneca = 0;
    
    scanf ("%d",&n);
```

Dentro do primeiro laço `for`, lemos as variáveis `nome` e `genero`. Note que, lemos `nome` usando o especificador de formato `"%s "` com um espaço, pois queremos ler o espaço também.

Após a leitura, usamos um `if` para verificar se o `genero` é igual a F(indicando o gênero feminino), em caso afirmativo incrementamos em uma unidade da variável `boneca`, ao contrário aumentamos em um a variável `carrinho`, que indica o gênero masculino.

```c
for (i=0;i<n;i++){
        scanf ("%s ", nome);
        scanf ("%c", &genero);
        
        if (genero == 'F')
            boneca++;
        else
            carrinho++;
    }
```

Ao final, imprimimos a quantidade de carrinhos e bonecas.

```c
    printf ("%d carrinhos\n", carrinho);
    printf ("%d bonecas\n", boneca);
```


##### Para aprender um pouco mais sobre alocação dinâmica: [Alocação dinâmica](http://linguagemc.com.br/alocacao-dinamica-de-memoria-em-c/)
 
Caso tenha alguma dúvida sobre este problema ou sobre a resolução, entre em contato com o PET-BCC pelo nosso
[Facebook](https://www.facebook.com/petbcc/),
[Instagram](https://www.instagram.com/petbcc.ufscar/)
ou nos mande um e-mail com o assunto "URI" para  petbcc.ufscar@gmail.com
