'''e) Elaborar um programa que efetue a leitura de 15 valores numéricos inteiros e no final apresente o 
total do somatório da fatorial de cada valor lido.'''

contadora = 1
soma = 0

while True:

    try:
        numero = int(input(f"Digite o {contadora}º número: "))
        antecessor = numero
    except:
        print("Entrada invalida! Digite um número inteiro!")
        continue

    if numero < 0:
        fatorial = 0
    elif numero <= 1:
        fatorial = 1
    else:
        fatorial = 1
        while antecessor > 1:
            fatorial *= antecessor
            antecessor -= 1
    soma += fatorial

    contadora += 1
    if contadora > 15:
        break

print(soma)