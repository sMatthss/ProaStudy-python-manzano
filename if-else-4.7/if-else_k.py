'''k. Elaborar  um  programa  que  efetue  a  leitura  de  um  determinado  valor  inteiro,  e  efetue  a  sua 
apresentação, caso o valor não seja maior que três.'''
try:
    num = int(input("Digite um número: "))

    if num <= 3:
        print(num)
    else:
        print("O número não pode ser maior que três!")

except:
    print("Digite um número valido!")