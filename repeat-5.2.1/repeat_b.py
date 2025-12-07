'''b) Elaborar um programa que apresente no final o somatório dos valores pares existentes na faixa de 
1 até 500.'''
soma = 0
contadora = 1

while True:

    if contadora % 2 == 0:
        soma += contadora

    contadora += 1

    if contadora > 500:
        break

print(f"O somatório dos valores pares de 1 até 500 é: {soma}")