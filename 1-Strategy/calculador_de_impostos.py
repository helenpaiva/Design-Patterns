
class Calculador_de_impostos(object):

    def realiza_calculo(self, orcamento, imposto):  # orcamento eh uma classe

        imposto_calculado = imposto.calcula(orcamento)

        print imposto_calculado


if __name__ == '__main__':

    from orcamento import Orcamento
    from impostos import ICMS, ISS

    orcamento = Orcamento(500.0)  # instancia aqui a classe a passo o valor = 500.0

    calculador_de_impostos = Calculador_de_impostos()

    calculador_de_impostos.realiza_calculo(orcamento, ICMS())
