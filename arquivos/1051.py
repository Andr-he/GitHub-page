Renda = float(input())
imposto = 0.00

if Renda <= 2000.00:
    print('Isento')
else:
    Renda = Renda - 2000.00
    if Renda <= 1000.00:
        imposto = Renda * 0.08
        print(f'R$ {imposto:.2f}')
    else:
        imposto = 1000.00 * 0.08
        Renda = Renda - 1000.00
        if Renda <= 1500.00:
            imposto+=Renda * 0.18
            print(f'R$ {imposto:.2f}')
        else:
            imposto+=1500.00*0.18
            Renda = Renda - 1500.00
            if Renda > 0:
                imposto+=Renda*0.28
                print(f'R$ {imposto:.2f}')



