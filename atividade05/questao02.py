def eh_palindromo(texto):
    texto_limpo = ''.join(c.lower() for c in texto if c.isalnum())
    return texto_limpo == texto_limpo[::-1]


texto = input("Digite um texto: ")
resultado = eh_palindromo(texto)
print(f"O texto é um palíndromo? {resultado}")
