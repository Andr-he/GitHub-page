import math 

A, B, C = map(float, input().split())

if (pow(B, 2)-4*A*C) > 0 and A != 0:
    R1 = (-B + math.sqrt(pow(B, 2)-4*A*C))/(2*A)
    R2 = (-B - math.sqrt(pow(B, 2)-4*A*C))/(2*A)

    print(f'R1 = {R1:.5f}')  
    print(f'R2 = {R2:.5f}')  
else:
    print('Impossivel calcular')


