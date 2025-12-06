'''c. Ler quatro valores referentes a quatro notas escolares de um aluno e imprimir uma mensagem 
dizendo que o aluno foi aprovado, se o valor da média escolar for maior ou igual a 5. Se o aluno não 
foi aprovado, indicar uma mensagem informando esta condição. Apresentar junto das mensagens o 
valor da média do aluno para qualquer condição. '''

nota1 = float(input("Digite a primeira nota do aluno: "))
nota2 = float(input("Digite a segunda nota do aluno: "))
nota3 = float(input("Digite a terceira nota do aluno: "))
nota4 = float(input("Digite a quarta nota do aluno: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

print(f"--- Resultado Final ---")
print(f"Média do aluno: {media}")

if media >= 5:
    print("O aluno foi Aprovado!")
else:
    
    print("O aluno foi Reprovado!")