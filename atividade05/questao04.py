from datetime import datetime
def calcular_dias_vivo(data_nascimento):
    data_atual = datetime.now()
    dias_vivo = (data_atual - data_nascimento).days
    return dias_vivo
# Codigo Main
data_nascimento_str = input("Digite sua data de nascimento (DD/MM/AAAA): ")
data_nascimento = datetime.strptime(data_nascimento_str, "%d/%m/%Y")
dias_vivo = calcular_dias_vivo(data_nascimento)
print(f"Você está vivo há {dias_vivo} dias.")
