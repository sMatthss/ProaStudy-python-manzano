#b) Apresentar os resultados de uma tabuada de multiplicar (de 1 até 10) de um número qualquer.

valor = int(input("Digite um número: "))

for i in range(1, 11):

    resultado = valor * i
    print(f"{valor} * {i} = {resultado}")