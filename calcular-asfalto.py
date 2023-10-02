#Programa que calcula quantidade de concreto para ruas

#Quantidade de asfalto
area = float(input('Inserir área em metros quadrados: '))
espessura = float(input('Inserir espessura em metros: '))
densidade = float(input('Inserir densidade: '))

asfalto = area * espessura * densidade

#Preço do asfalto por metro quadrado
if asfalto < 5000:
    preco = 150
elif 5000 < asfalto < 15000:
    preco = 250
else:
    preco = 450

#Preço total
preco_total = preco * asfalto

print(f'O preço total a ser pago para asfaltar a rua será {preco_total}')