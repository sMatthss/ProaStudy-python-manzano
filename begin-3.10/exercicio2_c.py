'''c) Em uma eleição sindical concorreram ao cargo de presidente três candidatos (A, B e C). Durante a 
apuração dos votos foram computados votos nulos e votos em branco, além dos votos válidos para 
cada candidato. Deve ser criado um programa de computador que efetue a leitura da quantidade de 
votos válidos para cada candidato, além de efetuar  também a leitura da quantidade de votos nulos e 
votos em branco. Ao final o programa deve apresentar o número total de eleitores, considerando votos 
válidos, nulos e em branco; o percentual correspondente de votos válidos em relação à quantidade de 
eleitores; o percentual correspondente de votos válidos do candidato A em relação à quantidade de 
eleitores; o percentual correspondente de votos válidos do candidato B em relação à quantidade de 
eleitores; o percentual correspondente de votos válidos do candidato C em relação à quantidade de 
eleitores; o percentual correspondente de votos nulos em relação à quantidade de eleitores; e por último 
o percentual correspondente de votos em branco em relação à quantidade de eleitores.'''

votos_a = int(input("Digite a quantidade de votos no eleitor A: "))
votos_b = int(input("Digite a quantidade de votos no eleitor B: "))
votos_c = int(input("Digite a quantidade de votos no eleitor C: "))

votos_nulos = int(input("Digite a quantidade de votos que foram nulos: "))
votos_branco = int(input("Digite a quantidade de votos que foram nulos: "))

total_eleitores = votos_a + votos_b + votos_c + votos_nulos + votos_branco

total_votos_validos = votos_a + votos_b + votos_c

percentual_validos = (total_votos_validos / total_eleitores) * 100

percentual_a = (votos_a / total_eleitores) * 100
percentual_b = (votos_b / total_eleitores) * 100
percentual_c = (votos_c / total_eleitores) * 100

percentual_nulos = (votos_nulos / total_eleitores) * 100
percentual_branco = (votos_branco / total_eleitores) * 100

print("\n--- Resultados da Eleição ---")

print(f"1. Número total de eleitores: {total_eleitores}")

print("\n--- Percentuais (em relação ao total de eleitores) ---")
print(f"2. Percentual de Votos Válidos: {percentual_validos:.2f}%")

print(f"3. Percentual de Votos Válidos (Candidato A): {percentual_a:.2f}%")
print(f"4. Percentual de Votos Válidos (Candidato B): {percentual_b:.2f}%")
print(f"5. Percentual de Votos Válidos (Candidato C): {percentual_c:.2f}%")

print(f"6. Percentual de Votos Nulos: {percentual_nulos:.2f}%")
print(f"7. Percentual de Votos em Branco: {percentual_branco:.2f}%")