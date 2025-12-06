'''a. Ler dois valores numéricos inteiros e apresentar o resultado da diferença do maior pelo menor valor. '''

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

if numero1 > numero2:
    diferenca = numero1 - numero2
    print(f"A diferença entre o número {numero2} e {numero1} é {diferenca}")

else:
    diferenca = numero2 - numero1
    print(f"A diferença entre o número {numero1} e {numero2} é {diferenca}")
