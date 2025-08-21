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

# 3- Calculadora de Média Escolar
nota1 = 7.5
nota2 = 8.0
nota3 = 6.5 
media = (nota1 + nota2 + nota3) / 3
print(f"Nota 1: {nota1}")
print(f"Nota 2: {nota2}")
print(f"Nota 3: {nota3}")
print(f"Média final: {media:.2f}")  

# 4- Calculadora de Consumo de Combustível
distancia_percorrida = 300
combustivel_gasto = 25  
consumo_medio = distancia_percorrida / combustivel_gasto
print(f"Distância percorrida: {distancia_percorrida} km")
print(f"Combustível gasto: {combustivel_gasto} litros")
print(f"Consumo médio: {consumo_medio:.2f} km/l")
