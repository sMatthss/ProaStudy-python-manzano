'''h) Elaborar um programa que apresente como resultado o valor de uma potência de uma base
qualquer elevada a um expoente qualquer, ou seja, de BE
, em que B é o valor da base e E o valor
do expoente. Observe que neste exercício não pode ser utilizado o operador de exponenciação do
portuguol (^). '''

base = int(input("Digite a base da operação: "))
expoente = int(input("Digite o expoente da operação: "))
potencia = 1

for i in range(expoente+1):
    
    print(f"{base} * {i} = {potencia}")
    potencia *= base
    
