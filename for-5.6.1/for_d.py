'''d) Elaborar um programa que apresente no final o somatório dos valores pares existentes na faixa de
1 até 500. '''

resultado = 0

for i in range(1, 501):

    if i % 2 == 0:
        resultado = resultado + i

print(resultado)