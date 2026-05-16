A, B, C = map(float, input().split())
pi= 3.14159

Triangulo = A*C/2
Circulo = pi*C**2
Trapezio = (A+B)*C/2
Quadrado = B**2
Retangulo = A*B

print(f'TRIANGULO: {Triangulo:.3f}')
print(f'CIRCULO: {Circulo:.3f}')
print(f'TRAPEZIO: {Trapezio:.3f}')
print(f'QUADRADO: {Quadrado:.3f}')
print(f'RETANGULO: {Retangulo:.3f}')