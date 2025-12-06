'''e. Efetuar a leitura de três valores (variáveis A, B e C) e efetuar o cálculo da equação completa de 
segundo grau, apresentando as duas raízes, se para os valores informados for possível efetuar o 
referido cálculo. Lembre-se de que a variável A deve ser diferente de zero.'''

var_a = int(input("Digite o valor A: "))
var_b = int(input("Digite o valor B: "))
var_c = int(input("Digite o valor C: "))

if var_a == 0:
    print("O valor A deve ser maior que 0!")
else:
    delta = var_b**2 - 4 * var_a * var_c #calculo do delta

    if delta > 0:

        raiz1 = (-var_b + delta ** 0.5) / (2 * var_a)
        raiz2 = (-var_b - delta ** 0.5) / (2 * var_a)

        print(f"A primeira raiz é: {raiz1}")
        print(f"A segunda raiz é: {raiz2}")
    
    elif delta == 0:
        
        raiz = -var_b / (2 * var_a)
        print(f"Raiz unica: {raiz}")
    else:
        print("não a raizes")