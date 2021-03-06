import re


class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def valida_url(self):
        if not self.url:
            raise ValueError('A URL está vazia!')

        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(self.url)
        if not match:
            raise ValueError("A url não está valida!")

    def get_url_base(self):
        indice_interrogacao = self.url.find('?')
        if indice_interrogacao != -1:
            url_base = self.url[:indice_interrogacao]
            return url_base
        else:
            return print('Indice não encontrado!')

    def get_url_parametros(self):
        indice_interrogacao = self.url.find('?')
        if indice_interrogacao != -1:
            url_parametro = self.url[indice_interrogacao + 1:]
            return url_parametro
        else:
            return print('Indice não encontrado!')

    def get_valor_parametro(self, parametro_busca):
        indice_paramentro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_paramentro + len(parametro_busca) + 1
        indice_ecomercial = self.get_url_parametros().find("&", indice_valor)
        if indice_ecomercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_ecomercial]
        return valor

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return 'URL: ' + self.url + '\n' + 'Parâmetros:' + self.get_url_parametros() + '\n' + 'Base: ' + self.get_url_base()

    def __eq__(self, other):
        return self.url == other.url


extrator_url = ExtratorURL("https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100")
valor_gerado = extrator_url.get_valor_parametro("quantidade")
print(valor_gerado)
