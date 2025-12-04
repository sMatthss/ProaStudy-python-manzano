'''e) Efetuar o cálculo e a apresentação do valor de uma prestação em atraso, utilizando a fórmula  
PRESTACAO ← VALOR + (VALOR * TAXA/100) * TEMPO).'''

valor = float(input("Digite o valor da prestação: "))
taxa = float(input("Digite a taxa cobrada pelo atraso: "))
tempo = int(input("Digite os meses em atraso: "))

prestacao = valor + (valor * taxa/100) * tempo

print(f"O valor a se pago sera: {prestacao:.2f}")