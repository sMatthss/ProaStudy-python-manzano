'''i. Elaborar  um  programa  que  efetue  a  leitura  de  um  número  inteiro  e  apresentar  uma  mensagem 
informando se o número é par ou ímpar.'''
try:
    num = int(input("Digite um número: "))

    if num % 2 == 0:
        print(f"O número {num} é par")
    else:
        print(f"O número {num} é impar")
except:
    print("Digite um número válido")