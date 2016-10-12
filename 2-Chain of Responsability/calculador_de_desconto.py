# -*- coding: UTF-8 -*-
from descontos import Desconto_por_cinco_itens, Desconto_por_mais_de_quinhentos_reais, Sem_desconto

class Calculador_de_descontos(object):

    def calcula(self, orcamento):

        desconto = Desconto_por_cinco_itens(
            Desconto_por_mais_de_quinhentos_reais(
                Sem_desconto()
            )
        )
        return desconto.calcular(orcamento)

if __name__=='__main__':

    from orcamento import Orcamento, Item

    orcamento = Orcamento()
    orcamento.adiciona_item(Item('Item A', 100.0))
    orcamento.adiciona_item(Item('Item B', 100.0))
    orcamento.adiciona_item(Item('Item C', 100.0))
    orcamento.adiciona_item(Item('Item D', 100.0))
    orcamento.adiciona_item(Item('Item E', 101.0))

    calculador_de_descontos = Calculador_de_descontos() # instancio a classe
    desconto = calculador_de_descontos.calcula(orcamento)

    print 'Desconto calculado : %s' % (desconto)
