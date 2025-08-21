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