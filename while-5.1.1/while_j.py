'''j) Elaborar um programa que apresente os resultados da soma e da média aritmética dos valores 
pares situados na faixa numérica de 50 a 70.'''

contadora = 50
soma = 0
div = 0
media = 0

while contadora <= 70:

    if contadora % 2 == 0:
        soma += contadora
        div += 1
    
    contadora += 1

media = soma / div

print(soma)
print(media)