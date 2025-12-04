'''k) Elaborar um programa que efetue a apresentação do valor da conversão em dólar de um valor lido em 
real. O programa deve solicitar o valor da cotação do dólar e também a quantidade de reais disponível 
com o usuário, para que seja apresentado o valor em moeda americana.'''

cotacao = float(input("Digite a cotação atual do dolar: "))
real = float(input("Digite quantos reais você possui: "))

dolar = real / cotacao

print(f"A valor em reais de: {real}R$ em dolares é: {dolar:.2f}U$")