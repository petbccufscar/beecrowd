tempoGasto = io.read('*n')
velocidadeMedia = io.read('*n')

distancia = velocidadeMedia * tempoGasto
litros = distancia / 12.0

print(string.format('%.3f', litros))