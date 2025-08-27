import requests
def gerar_perfil_usuario():
    url = 'https://randomuser.me/api/'
    resposta = requests.get(url)
    dados = resposta.json()
    
    usuario = dados['results'][0]
    nome = f"{usuario['name']['first']} {usuario['name']['last']}"
    email = usuario['email']
    pais = usuario['location']['country']
    
    return nome, email, pais
nome, email, pais = gerar_perfil_usuario()
print("Nome:", nome)
print("Email:", email)
print("País:", pais)
