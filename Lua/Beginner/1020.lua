dias = io.read('*n')

anos = math.floor(dias/365)
dias = dias%365
meses = math.floor(dias/30)
dias = dias%30

print(string.format('%d ano(s)', anos))
print(string.format('%d mes(es)', meses))
print(string.format('%d dia(s)', dias))