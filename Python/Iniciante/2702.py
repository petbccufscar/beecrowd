# Problema 2702 - Beecrowd - Iniciante - Nível 1

# Leitura dos valores
Ca, Ba, Pa = map(int, input().split(' '))
Cr, Br, Pr = map(int, input().split(' '))

# Cálculo das refeições que estão em falta
# Um número negativo em Xr - Xa significa que refeições estão sobrando
# Ignoramos isso com max(0, X)
Cf = max(0, Cr - Ca)
Bf = max(0, Br - Ba)
Pf = max(0, Pr - Pa)

# Basta printar a soma
print(Cf + Bf + Pf)
