'''l) Elaborar um programa que efetue a leitura de valores positivos inteiros até que um valor negativo 
seja informado. Ao final devem ser apresentados o maior e o menor valores informados pelo 
usuário. '''

numero = int(input("Digite um número qualquer: "))

maior_numero = numero
menor_numero = numero

while numero >= 0:
    
    if numero > maior_numero:
        maior_numero = numero
    
    if numero < menor_numero:
        menor_numero = numero
    
    numero = int(input("Digite um número qualquer: "))

print(maior_numero)
print(menor_numero)
