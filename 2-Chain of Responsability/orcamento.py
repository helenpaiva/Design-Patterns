# -*- coding: UTF-8 -*-

class Orcamento(object):

    def __init__(self):
        self.__itens = [] # construtor cria uma lista de itens

    @property
    def valor(self):
        total = 0.0
        for item in self.__itens:
            total += item.valor
        return total

    # retornamos uma tupla ja q nao faz sentido alterar itens de um orcamento
    def obter_itens(self):
        return tuple(self.__itens)

    # perguntamos para o orcamento o total de itens
    def total_itens(self):
        return len(self.__itens)

    def adiciona_item(self, item):
        self.__itens.append(item)

# um item criado nao pode ser alterado. Propriedades somente leitura
class Item(object):

    def __init__(self, nome, valor):
        self.__nome = nome
        self.__valor = valor

    @property
    def valor(self):
        return self.__valor

    @property
    def nome(self):
        return self.__nome