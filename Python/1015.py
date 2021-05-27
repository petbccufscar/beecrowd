# Adicionando "math" para usar  "sqrt" e "pow"
import math 
# Lendo x1 e y1
x1, y1 = input().split(" ")
# Lendo x2 e y2
x2, y2 = input().split(" ")
# Imprimindo a distancia
print("%.4f" % (math.sqrt(math.pow((float(x2) - float(x1)), 2) + math.pow((float(y2) - float(y1)), 2))))