'''k) Elaborar um programa que possibilite calcular a área total de uma residência (sala, cozinha, 
banheiro, quartos, área de serviço, quintal, garagem, etc.). O programa deve solicitar a entrada do 
nome, a largura e o comprimento de um determinado cômodo. Em seguida, deve apresentar a 
área do cômodo lido e também uma mensagem solicitando do usuário a confirmação de continuar 
calculando novos cômodos. Caso o usuário responda “NAO”, o programa deve apresentar o valor 
total acumulado da área residencial. '''

area_residencia = 0

continuar = "S"

while continuar.upper() == "SIM" or continuar.upper() == "S":
    
    comodo = input("Digite o nome do cômodo: ")
    largura = float(input("Digite a largura do cômodo: "))
    comprimento = float(input("Digite o comprimento do cômodo: "))

    area_comodo = largura * comprimento
    area_residencia += area_comodo

    print(f"A área do cômodo: {comodo} é {area_comodo}")


    continuar = (input("Você deseja continuar? [SIM/NAO]: "))


print(f"A área total da residência é: {area_residencia}")
    
