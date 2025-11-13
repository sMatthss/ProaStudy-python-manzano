'''k) Elaborar um programa que apresente como resultado o valor do fatorial dos valores ímpares
situados na faixa numérica de 1 a 10. '''


for i in range(1, 11):
    
    if i % 2 == 1:
        fatorial = 1
        for x in range(1, i + 1):
            fatorial *= i
        print(f"{i}! = {fatorial}")
        