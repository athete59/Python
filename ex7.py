produto1= input("Olá! Tu está no mercado SuperBrasil, qual produto gostaria de cadastrar?")
produto2= input("Qual o segundo produto pra cadastro?")
produto3= input("E o terceiro?")
preco1=float(input(f"Certo cê gostaria de cadastrar: {produto1}, qual o preço dele? R$"))
preco2=float(input(f"E para a/o {produto2}, qual o preco? R$"))
preco3=float(input(f"Por fim, qual o preço da(o) {produto3} ? R$"))

melhorproduto=min(preco1,preco2,preco3)

if melhorproduto==preco1:
    print("O mais barato e a/o",produto1)
elif melhorproduto==preco2:
    print("O mais barato e a/o", produto2)
else:
    print("O mais barato e a/o", produto3)