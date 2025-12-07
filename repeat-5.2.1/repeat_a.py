'''a) Apresentar os quadrados dos números inteiros de 15 a 200.'''

contadora = 15

while True:
    quad = contadora * contadora
    print(f"{contadora}^2 = {quad}")

    contadora += 1
    if contadora > 200:
        break