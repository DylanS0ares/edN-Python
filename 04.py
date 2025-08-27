import requests
def consultar_cotacao(moeda):
    url = f'https://economia.awesomeapi.com.br/json/last/{moeda}-BRL'
    resposta = requests.get(url)
    dados = resposta.json()
    
    chave = f'{moeda}BRL'
    if chave not in dados:
        return None
    
    cotacao = dados[chave]
    valor_atual = cotacao['bid']
    valor_maximo = cotacao['high']
    valor_minimo = cotacao['low']
    data_hora = cotacao['create_date']
    
    return valor_atual, valor_maximo, valor_minimo, data_hora
moeda = input("Digite o código da moeda (ex: USD, EUR, GBP): ").upper()
resultado = consultar_cotacao(moeda)
if resultado:
    valor_atual, valor_maximo, valor_minimo, data_hora = resultado
    print(f"Cotação atual de {moeda} em BRL:")
    print("Valor Atual:", valor_atual)
    print("Valor Máximo:", valor_maximo)
    print("Valor Mínimo:", valor_minimo)
    print("Data e Hora da Última Atualização:", data_hora)
else:
    print("Moeda não encontrada ou inválida.")
