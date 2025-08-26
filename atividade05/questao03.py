def calcular_preco_final(preco_original, porcentagem_desconto):
    desconto = preco_original * (porcentagem_desconto / 100)
    preco_final = preco_original - desconto
    return round(preco_final, 2)
# Codigo Main
preco = float(input("Digite o preço original do produto: R$ "))
percentual_desconto = float(input("Digite a porcentagem de desconto (ex: 10 para 10%): "))
preco_com_desconto = calcular_preco_final(preco, percentual_desconto)
print(f"O preço final com desconto é: R$ {preco_com_desconto}")
