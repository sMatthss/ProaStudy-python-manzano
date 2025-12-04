'''f) Ler dois valores (inteiros, reais ou caracteres) para as variáveis A e B, e efetuar a troca dos valores de 
forma que a variável A passe a possuir o valor da variável B e a variável B passe a possuir o valor da 
variável A. Apresentar os valores trocados'''

valor_a = input("Digite o primeiro valor: ")
valor_b = input("Digite o segundo valor: ")

valor_c = valor_a
valor_a = valor_b
valor_b = valor_c

print(f"valor da segunda variavel: {valor_a}\nvalor da primeira variavel: {valor_b}")