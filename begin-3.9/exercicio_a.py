'''a) Ler uma temperatura em graus Celsius e apresentá-la convertida em graus Fahrenheit. A fórmula de 
conversão é F ← (9 * C + 160) / 5, sendo F a temperatura em Fahrenheit e C a temperatura em Celsius. '''

celcius = int(input("Digite a temperatura em Celcius para a conversão: "))

fahrenheit = (9 * celcius + 160) / 5

print(f"A temperatura em Fahrenheit é: {fahrenheit}")