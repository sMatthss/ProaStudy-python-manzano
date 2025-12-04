'''g) Ler quatro números inteiros e apresentar o resultado da adição e multiplicação, baseando-se na 
utilização do conceito da propriedade distributiva. Ou seja, se forem lidas as variáveis A, B, C, e D, 
devem ser somadas e multiplicadas A com B, A com C e A com D. Depois B com C, B com D e por fim 
C com D. Perceba que será necessário efetuar seis operações de adição e seis operações de 
multiplicação e apresentar doze resultados de saída.'''

a = int(input("Digite o primeiro numero inteiro: "))
b = int(input("Digite o segundo numero inteiro: "))
c = int(input("Digite o terceiro numero inteiro: "))
d = int(input("Digite o quarto numero inteiro: "))

soma_a1 = a + b
soma_a2 = a + c
soma_a3 = a + d

soma_b1 = b + c
soma_b2 = b + d

soma_c1 = c + d

mult_a1 = a * b
mult_a2 = a * c
mult_a3 = a * d

mult_b1 = b * c
mult_b2 = b * d

mult_c1 = c * d

print("## Resultado da soma dos valores ###")
print(f"A soma do valor {a} + {b} = {soma_a1}")
print(f"A soma do valor {a} + {c} = {soma_a2}")
print(f"A soma do valor {a} + {d} = {soma_a3}")
print(f"A soma do valor {b} + {c} = {soma_b1}")
print(f"A soma do valor {b} + {d} = {soma_b2}")
print(f"A soma do valor {c} + {d} = {soma_c1}")

print("## Resultado da multiplicação dos valores ###")
print(f"A multiplicação dos valores {a} * {b} = {mult_a1}")
print(f"A multiplicação dos valores {a} * {c} = {mult_a2}")
print(f"A multiplicação dos valores {a} * {d} = {mult_a3}")
print(f"A multiplicação dos valores {b} * {c} = {mult_b1}")
print(f"A multiplicação dos valores {b} * {d} = {mult_b2}")
print(f"A multiplicação dos valores {c} * {d} = {mult_c1}")