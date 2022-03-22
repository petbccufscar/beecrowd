while True: 
    x = int(input())
    y = x
    i = 0
    soma = 0
    if(x == 0):
        break
    if(x % 2 == 0):
        for i in range(5):
            soma = soma + y
            y = y + 2
    else:
        y = y + 1
        for i in range(5):
            soma = soma + y
            y = y + 2
    print(soma)
    if(x==0):
        break