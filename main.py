url = "https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"

# Separa a base e os parâmetros

indice_interrogacao = url.find('?')

if indice_interrogacao != -1:
    url_base = url[:indice_interrogacao]

    url_paramentros = url[indice_interrogacao + 1:]
    print(url_paramentros)
else:
    print("Indice não encontrado")

# Busca o valor de um parâmetro

parametro_busca = 'moedaDestino'
indice_paramentro = url_paramentros.find(parametro_busca)
indice_valor = indice_paramentro + len(parametro_busca) + 1
indice_ecomercial = url_paramentros.find("&", indice_valor)
if indice_ecomercial == -1:
    valor = url_paramentros[indice_valor:]
else:
    valor = url_paramentros[indice_valor:indice_ecomercial]

print(valor)
