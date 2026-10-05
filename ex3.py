nome=input("Qual o seu nome?")
age1=int(input("Qual a sua idade?"))
print("Cadastro de cliente 1 concluído")
nome2=input("Qual o seu nome?")
age2=int(input("Qual a sua idade?"))

if age1>age2:
    print("O cliente 1:",nome,"é mais velho que o cliente 2:", nome2)
elif age1<age2:
    print("O cliete 2:",nome, "é mais velho que o cliente 1:", nome2)
else:
    print("O cliente 1", nome, "tem a mesma idade do cliente 2:",nome2)

print(not age2!=age1)