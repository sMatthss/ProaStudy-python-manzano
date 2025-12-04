'''a) Elaborar um programa de computador que efetue a leitura de quatro valores inteiros (variáveis A, B, C e 
D). Ao final o programa deve apresentar o resultado do produto (variável P) do primeiro com o terceiro 
valor, e o resultado do produto (variável P) do primeiro com o terceiro valor, e o resultado da soma 
(variável S) do segundo com o quarto valor. '''

valor_a = int(input("Digite o primeiro valor: "))
valor_b = int(input("Digite o segundo valor: "))
valor_c = int(input("Digite o terceiro valor: "))
valor_d = int(input("Digite o quarto valor: "))

valor_p = valor_a * valor_c
valor_s = valor_b + valor_d

print(f"O resultado do produto dos valores {valor_a} * {valor_c} = {valor_p}")
print(f"O resultado da soma dos valores {valor_b} + {valor_d} = {valor_s}")