def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    gorjeta = valor_conta*(porcentagem_gorjeta/100)

    return round(gorjeta,2)

#Codigo Main
total_conta = float(input("Digite o valor total da conta: R$ "))
percentual_gorjeta = float(input("Digite a porcentagem da gorjeta (ex: 10 para 10%): "))

gorjeta = calcular_gorjeta(total_conta, percentual_gorjeta)

print(f"A gorjeta sugerida é: R$ {gorjeta}")