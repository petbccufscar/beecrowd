segundos = io.read('*n')

horas = math.floor(segundos/3600)
segundos = segundos%3600
minutos = math.floor(segundos/60)
segundos = segundos%60

print(string.format('%d:%d:%d', horas, minutos, segundos))