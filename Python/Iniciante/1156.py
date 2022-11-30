soma = 0

for i in range(0, 20):
    soma += (2 * i + 1) / (2 ** i)
print("{:.2f}".format(soma))