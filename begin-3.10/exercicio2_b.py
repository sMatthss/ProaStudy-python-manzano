'''b) Ler o valor correspondente ao salário mensal (variável SM) de um trabalhador e também o valor do 
percentual de reajuste (variável PR) a ser atribuído. Apresentar o valor do novo salário (variável NS).'''

sm = float(input("Digite o valor do salario de um trabalhador: "))
pr = float(input("Digite o percentual que sera feito o reajuste: "))

ns = sm * (pr / 100 + 1)
nsb = sm + (sm * pr / 100)

print(f"O novo salario do funcionario com o reajuste é: {ns}")
print(f"O novo salario do funcionario com o reajuste em outro calculo: {nsb}")