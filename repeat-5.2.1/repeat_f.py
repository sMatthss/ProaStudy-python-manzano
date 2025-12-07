'''f) Elaborar  um  programa  que  efetue  a  leitura  sucessiva  de  valores  numéricos  e  apresente  no  final  o 
total do somatório, a média aritmética e o total de valores lidos. O programa deve fazer as leituras 
dos  valores  enquanto  o  usuário  estiver  fornecendo  valores  positivos.  Ou  seja,  o  programa  deve 
parar  quando  o  usuário  fornecer  um  valor  negativo.  Não  se  esqueça  que  o  usuário  pode  entrar 
como primeiro número um número negativo, portanto, cuidado com a divisão por zero no cálculo da 
média.'''
contadora = 0
soma = 0

while True:

    numero = int(input("Digite um número: "))
    
    if numero >= 0:
        soma += numero
        contadora += 1
        media = soma / contadora
    else:
        print("Fim do programa!")

    if numero < 0:
        break

print(soma)
print(media)
print(contadora)
