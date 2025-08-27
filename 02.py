import requests
def gerar_perfil_usuario():
    url = 'https://randomuser.me/api/'
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
        dados = resposta.json()
        
        usuario = dados['results'][0]
        nome = f"{usuario['name']['first']} {usuario['name']['last']}"
        email = usuario['email']
        pais = usuario['location']['country']
        return nome, email, pais
    
    except (requests.RequestException, KeyError) as e:
        print("Erro ao obter dados do usuário:", e)
        return None, None, None
    
nome, email, pais = gerar_perfil_usuario()
print("Nome:", nome)
print("Email:", email)
print("País:", pais)
