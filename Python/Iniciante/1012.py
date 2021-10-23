# Problema 1012 - URI - Iniciante - Nível 2

# Primeiro lemos os três valores
a, b, c = map(float, input().split())

pi = 3.14159

# Então calculamos as áreas
triangulo = a * c / 2
circulo   = c**2 * pi
trapezio  = (a + b) * c / 2
quadrado  = b**2
retangulo = a * b

# Então printamos as áreas, com três casas decimais
print(f'TRIANGULO: {triangulo:.3f}')
print(f'CIRCULO: {circulo:.3f}')
print(f'TRAPEZIO: {trapezio:.3f}')
print(f'QUADRADO: {quadrado:.3f}')
print(f'RETANGULO: {retangulo:.3f}')