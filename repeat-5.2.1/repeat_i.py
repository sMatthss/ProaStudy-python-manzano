'''i) Elaborar  um  programa  que  efetue  a  leitura  de  valores  positivos  inteiros  até  que  um  valor  negativo 
seja  informado.  Ao  final  devem  ser  apresentados  o  maior  e  o  menor  valores  informados  pelo 
usuário. '''

validador = 1

while True:

    try:
        numero = int(input("Digite um número inteiro qualquer: "))
    except:
        print("O número digitado deve ser inteiro!")

    if numero >= 0:
        if validador == 1:
            maior = numero
            menor = numero
            validador = 0

        elif numero > maior:
            maior = numero
        elif numero < menor:
            menor = numero

    if numero < 0:
        break

print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")