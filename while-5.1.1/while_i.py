'''i) Elaborar um programa que efetue a leitura de 10 valores numéricos e apresente no final o total do 
somatório e a média aritmética dos valores lidos.'''

contadora = 1
soma = 0
conta = 0

while contadora <= 10:

    valores = int(input("Digite 10 números: "))
    
    soma += valores
    conta = soma / contadora
    
    contadora += 1

print(soma)
print(conta)