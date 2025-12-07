'''g. Efetuar a leitura de quatro números inteiros e apresentar os números que são divisíveis por 2 e 3.'''

try:
    num_1 = int(input("Digite o primeiro número: "))
    num_2 = int(input("Digite o segundo número: "))
    num_3 = int(input("Digite o terceiro número: "))
    num_4 = int(input("Digite o quarto número: "))

    if num_1 % 6 == 0:
        print(f"O número {num_1} é divisivel por 2 e 3")
    else:
        print(f"O número {num_1} NÃO é divivel por 2 e 3!")

    if num_2 % 6 == 0:
        print(f"O número {num_2} é divisivel por 2 e 3")
    else:
        print(f"O número {num_2} NÃO é divivel por 2 e 3!")

    if num_3 % 6 == 0:
        print(f"O número {num_3} é divisivel por 2 e 3")
    else:
        print(f"O número {num_3} NÃO é divivel por 2 e 3!")
    if num_4 % 6 == 0:
        print(f"O número {num_4} é divisivel por 2 e 3")
    else:
        print(f"O número {num_4} NÃO é divivel por 2 e 3!")

except:
    print("Digite um número válido!")