# le as entradas e as armazena
time, speed = int(input()), int(input()) 

# imprime na tela a quantidade de litros
# dado a formula (Km/h * h) / Km/L
print("%.3f" % ((time*speed)/12))