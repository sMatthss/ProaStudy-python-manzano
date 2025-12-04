'''m) Elaborar um programa que efetue a leitura de três valores (A,B e C) e apresente como resultado final o 
quadrado da soma dos três valores lidos. '''

a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
c = int(input("Digite o terceiro valor: "))

soma = a + b + c

quad = soma * soma

print(f"O resultado do quadrado da soma dos três valores é: {quad}")