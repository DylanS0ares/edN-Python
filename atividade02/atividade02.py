#Questão 01 

valor_em_reais = 100.00
taxa_dolar = 5.20
taxa_euro = 5.60

# 1- Conversor de Moedas

valor_em_dolar = valor_em_reais / taxa_dolar
valor_em_euro = valor_em_reais / taxa_euro

print(f"Valor em reais: R$",valor_em_reais)
print(f"Valor em dólares: $",round(valor_em_dolar,2))
print(f"Valor em euros: €",round(valor_em_euro,2))


#Questão 02

nome = "Camiseta"
preco_original = 50.00
porcentagem_desconto = 0.2
# 2- Calculadora de Desconto

valor_de_desconto = preco_original * porcentagem_desconto
preco_final = preco_original - valor_de_desconto
print(f"Produto: {nome}")
print(f"Preço original: R$ {preco_original:.2f}")
print(f"Valor do desconto: R$ {valor_de_desconto:.2f}")
print(f"Preço final com desconto: R$ {preco_final:.2f}")