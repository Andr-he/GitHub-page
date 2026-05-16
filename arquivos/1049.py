filo = input()
classe = input()
alimentacao = input()

if filo == 'vertebrado':
    if classe == 'ave':
        if alimentacao == 'carnivoro':
            print()
            print('aguia')
        elif alimentacao == 'onivoro':
            print()
            print('pomba')
    elif classe == 'mamifero':
        if alimentacao == 'onivoro':
            print()
            print('homem')
        elif alimentacao == 'herbivoro':
            print()
            print('vaca')
elif filo == 'invertebrado':
    if classe == 'inseto':
        if alimentacao == 'hematofago':
            print()
            print('pulga')
        elif alimentacao == 'herbivoro':
            print()
            print('lagarta')
    elif classe == 'anelideo':
        if alimentacao == 'hematofago':
            print()
            print('sanguessuga')
        elif alimentacao == 'onivoro':
            print()
            print('minhoca')

