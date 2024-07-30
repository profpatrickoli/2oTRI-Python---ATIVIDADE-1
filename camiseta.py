class Camiseta:
    # Método construtor
    def __init__(self, tamanho, cor, estilo, tecido, marca, preco):
        # ATRIBUTOS DA CLASSE CONTA
        self.__tamanho = tamanho
        self.__cor = cor
        self.__estilo = estilo
        self.__tecido = tecido
        self.__marca = marca
        self.__preco = preco

    @property
    def tamanho(self):
        return self.__tamanho
    @tamanho.setter
    def tamanho(self, valor):
        self.__tamanho = valor

    @property
    def cor(self):
        return self.__cor
    @cor.setter
    def cor(self, valor):
        self.__cor = valor

    @property
    def estilo(self):
        return self.__estilo
    @estilo.setter
    def estilo(self, valor):
        self.__estilo = valor

    @property
    def tecido(self):
        return self.__tecido
    @tecido.setter
    def tecido(self, valor):
        self.__tecido = valor

    @property
    def marca(self):
        return self.__marca
    @marca.setter
    def marca(self, valor):
        self.__marca = valor

    @property
    def preco(self):
        return self.__preco
    @preco.setter
    def preco(self, valor):
        self.__preco = valor

