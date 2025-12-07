'''g) Elaborar  um  programa  que  apresente  como  resultado  o  valor  do  fatorial  dos  valores  ímpares 
situados na faixa numérica de 1 a 10.'''

contadora = 1


while True:

    if contadora % 2 == 1:
        antecessor = contadora
        fatorial = contadora
        while antecessor > 1:
            antecessor -= 1
            fatorial *= antecessor
        
        print(f" fatorial de {contadora}! = {fatorial}")

    contadora += 1
    if contadora > 10:
        break