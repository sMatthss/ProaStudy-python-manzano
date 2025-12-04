'''l) Elaborar um programa que efetue a leitura de três valores (A, B e C) e apresente como resultado final à 
soma dos quadrados dos três valores lidos.'''

a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
c = int(input("Digite o terceiro valor: "))

quad_a = a * a
quad_b = b * b
quad_c = c * c

soma = quad_a + quad_b + quad_c

print(f"A soma do quadrado dos três valores é: {soma}")