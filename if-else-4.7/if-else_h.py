'''h. Efetuar a leitura de cinco números inteiros e identificar o maior e o menor valores. '''

try:
    num_1 = int(input("Digite o primeiro número: "))
    num_2 = int(input("Digite o segundo número: "))
    num_3 = int(input("Digite o terceiro número: "))
    num_4 = int(input("Digite o quarto número: "))
    num_5 = int(input("Digite o quinto número: "))

    maior = num_1
    menor = num_2

    if num_2 > maior:
        maior = num_2
    if num_3 > maior:
        maior = num_3
    if num_4 > maior:
        maior = num_4
    if num_5 > maior:
        maior = num_5

    if num_2 < menor:
        menor = num_2
    if num_3 < menor:
        menor = num_3
    if num_4 < menor:
        maior = num_4
    if num_5 < menor:
        menor = num_5

    print(f"O maior número é {maior}")
    print(f"O maior número é {menor}")
except:
    print("Digite um número valido!")