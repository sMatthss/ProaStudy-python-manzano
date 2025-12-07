'''l. Elaborar um programa que efetue a leitura do nome e do sexo de uma pessoa, apresentando com 
saída  uma  das  seguintes  mensagens:  "Ilmo  Sr.",  se  o  sexo  informado  como  masculino,  ou  a 
mensagem "Ilma Sra.", para o sexo informado como  feminino. Apresente também junto da 
mensagem de saudação o nome previamente informado.'''

nome = input("Digite o seu nome: ")
sexo = input("Digite o seu sexo [M/F]: ")

if sexo.upper() == "M":
    print(f"Ilmo Sr. {nome}")
elif sexo.upper() == "F":
    print(f"Ilma Sra. {nome}")
else:
    print(f"Sexo invalido, digite M ou F")