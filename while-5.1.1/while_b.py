#b) Apresentar o total da soma obtida dos cem primeiros números inteiros (1+2+3+4+...+98+99+100).

contadora = 1
somatoria = 0

while contadora <= 100:
    somatoria = somatoria + contadora
    contadora += 1

print(somatoria)