import requests
def consultar_cep(cep):
    url = f'https://viacep.com.br/ws/{cep}/json/'
    resposta = requests.get(url)
    dados = resposta.json()
    
    if 'erro' in dados:
        return None
    
    logradouro = dados.get('logradouro', 'N/A')
    bairro = dados.get('bairro', 'N/A')
    cidade = dados.get('localidade', 'N/A')
    estado = dados.get('uf', 'N/A')
    
    return logradouro, bairro, cidade, estado
cep = input("Digite o CEP (somente números): ")
resultado = consultar_cep(cep)
if resultado:
    logradouro, bairro, cidade, estado = resultado
    print("Logradouro:", logradouro)
    print("Bairro:", bairro)
    print("Cidade:", cidade)
    print("Estado:", estado)


else:    print("CEP não encontrado ou inválido.")

