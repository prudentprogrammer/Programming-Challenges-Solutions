v = [float(x) for x in input().strip().split()]
A, B, C = v[0], v[1], v[2]
output = '''
TRIANGULO: %.3f
CIRCULO: %.3f
TRAPEZIO: %.3f
QUADRADO: %.3f
RETANGULO: %.3f
''' % (0.5 * A * C, 3.14159 * (C ** 2), ((A + B) / 2) * C, B ** 2, A * B)
print(output.strip())