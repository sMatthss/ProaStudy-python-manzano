'''h) Elaborar  um  programa  que  possibilite  calcular  a  área  total  de  uma  residência  (sala,  cozinha, 
banheiro, quartos, área de serviço, quintal, garagem, etc.). O programa deve solicitar a entrada do 
nome, a largura e o comprimento de um determinado cômodo. Em seguida, deve apresentar a área 
do  cômodo  lido  e  também  uma  mensagem  solicitando  do  usuário  a  confirmação  de  continuar 
calculando  novos  cômodos.  Caso  o  usuário  responda  “NAO”,  o  programa  deve  apresentar  o  valor 
total acumulado da área residencial.'''

area_casa = 0

while True: 

    print("=" * 30)
    nome = input("Digite o nome do comodo: ")
    largura = float(input("Digite a largura do comodo: "))
    comprimento = float(input("Digite o comprimento do comodo: "))

    print("=" * 30)
    area = largura * comprimento
    print(f"A area do comodo {nome} é {area}")


    area_casa += area
    
    cont = input("Você deseja calcular novos comodos? [S/N] ")
    if cont.upper() == "N":
        break

print("=" * 30)
print(f"A area total da casa é {area_casa}")