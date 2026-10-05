num1=input("Digite um numero:")
num2=input("Digite outro numero:")
num3=input("Digite o terceiro e ultimo numero:")

if num1>num2 and num1>num3:
    max=num1
    print("O maior numero entre eles é: ", max)
    if num2>num3:
        min=num3
    else:
        min=num2
    print("e o menor entre eles e:", min)
elif num2>num1 and num2>num3:
    max=num2
    print("O maior numero entre eles é: ", max)
    if num1>num3:
        min=num3
    else:
        min=num1;
    print("e o menor entre eles e:", min)
elif num3>num1 and num3>num1:
    max=num3
    print("O maior numero entre eles é: ", max)
    if num2>num1:
        min=num1
    else:
        min=num2
    print("e o menor entre eles e:", min)
else:
    print("Todos os numeros sao iguais, tá doida é? e o numero e:", num1)





