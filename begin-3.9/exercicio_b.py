'''b) Ler uma temperatura em graus Fahrenheit e apresentá-la convertida em graus Celsius. A fórmula de 
conversão é C ← (F - 32) * (5/9) , sendo F a temperatura em Fahrenheit e C a temperatura em Celsius. '''

fahrenheit = int(input("Digite a temperatura em Fahrenheit para a conversão: "))

celcius = (fahrenheit - 32) * (5/9)

print(f"A temperatura em Celcius é: {celcius}")