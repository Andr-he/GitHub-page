N, Q = map(float, input().split())

if (N < 1 or N > 5):
    print('Produto nao existente')
elif (N == 1):
    print(f'Total: R$ {4 * Q:.2f} ')
elif (N == 2):
    print(f'Total: R$ {4.50 * Q:.2f} ')
elif (N == 3):
    print(f'Total: R$ {5 * Q:.2f}')
elif (N == 4):
    print(f'Total: R$ {2 * Q:.2f} ')
elif (N == 5)   :
    print(f'Total: R$ {1.50 * Q:.2f} ')

