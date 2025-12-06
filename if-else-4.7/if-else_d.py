'''d. Ler quatro valores referentes a quatro notas escolares de um aluno e imprimir uma mensagem 
dizendo que o aluno foi aprovado, se o valor da média escolar for maior ou igual a 7. Se o valor da 
média for menor que 7, solicitar a nota de exame, somar com o valor da média e obter nova média. 
Se a nova média for maior ou igual a 5, apresentar uma mensagem dizendo que o aluno foi 
aprovado em exame. Se o aluno não foi aprovado, indicar uma mensagem informando esta 
condição. Apresentar com as mensagens o valor da média do aluno, para qualquer condição.'''

nota1 = float(input("Digite a primeira nota do aluno: "))
nota2 = float(input("Digite a segunda nota do aluno: "))
nota3 = float(input("Digite a terceira nota do aluno: "))
nota4 = float(input("Digite a quarta nota do aluno: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

print(f"--- Resultado Final ---")
print(f"Média do aluno: {media}")

if media >= 7:
    print("O aluno foi Aprovado!")
else:
    print("Média insuficiente para aprovação direta. Necessário Exame.")
    exame = float(input("Digite a nota do exame do aluno: "))
    nova_media = (media + exame) / 2

    if media >= 5:
        print(f"Nova média do aluno: {media}")
        print("O aluno foi Aprovado do exame!")
    else:
        print(f"Nova média do aluno: {media}")
        print("O aluno foi Reprovado!")