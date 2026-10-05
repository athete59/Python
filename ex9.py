nota=float(input("Digite a sua nota de 0 a 10:"))

while not (nota>0 and nota<=10):
    print("ERROR! PREENCHA NOVAMENTE")
    nota=float(input("Digite a sua nota:"))

print("A sua nota nesta disciplina e",nota)