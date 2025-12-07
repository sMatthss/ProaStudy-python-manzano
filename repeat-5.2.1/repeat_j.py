'''j) Elaborar  um  programa  que  apresente  o  resultado  inteiro  da  divisão  de  dois  números  quaisquer. 
Para a elaboração do programa, não utilizar em hipótese alguma o conceito do operador aritmético 
DIV.  A  solução  deve  ser  alcançada  com  a  utilização  de  looping.  Ou  seja,  o  programa  deve 
apresentar como resultado (quociente) quantas vezes o divisor cabe no dividendo. '''

numero1 = int(input("Digite um numero qualquer maior que 0: "))
numero2 = int(input("Digite outro numero qualquer maior que 0: "))
contadora = 0

while True:

    numero1 -= numero2

    contadora += 1

    if numero1 < numero2:
        break
print("=" * 30)
print(f"O quociente inteiro da divisão é igual a {contadora}")