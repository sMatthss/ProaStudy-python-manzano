'''f. Efetuar a leitura de três valores (variáveis A, B e C) e apresentá-los dispostos em ordem crescente. '''

try:
    var_a = int(input("Digite o primeiro número: "))
    var_b = int(input("Digite o segundo nmero: "))
    var_c = int(input("Digite o terceiro número: "))

    if var_a > var_b and var_a > var_c:
        if var_b > var_c:
            print(f"O número em ordem crescente é: {var_c}, {var_b}, {var_a}")
        else:
            print(f"O número em ordem crescente é: {var_b}, {var_c}, {var_a}")

    elif var_b > var_a and var_b > var_c:
        if var_a > var_c:
            print(f"O número em ordem crescente é: {var_c}, {var_a}, {var_b}")
        else:
            print(f"O número em ordem crescente é: {var_a}, {var_c}, {var_b}")
    elif var_c > var_a and var_c > var_b:
        if var_a > var_b:
            print(f"O número em ordem crescente é: {var_b}, {var_a}, {var_c}")
        else:
            print(f"O número em ordem crescente é: {var_a}, {var_b}, {var_c}")
    else:
        print("Os números não podem ser iguais!")
except:
    print("Digite um número valido")

