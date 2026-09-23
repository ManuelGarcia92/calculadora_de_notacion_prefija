from constantes import OPERACIONES
class NodoOperacion:
    def __init__(self, operador):
        self.operador = operador
        self.hijos = []

    def evaluar(self) -> int | float:
        valor_hijos = [hijo.evaluar() for hijo in self.hijos]

        if self.operador in ("**", "$"):
            resultado = valor_hijos[-1]
            for valor in reversed(valor_hijos[:-1]):
                resultado = OPERACIONES[self.operador](valor, resultado)
        else:
            resultado = valor_hijos[0]
            for valor in valor_hijos[1:]:
                resultado = OPERACIONES[self.operador](resultado, valor)
        return resultado
       
class NodoNumero:
    def __init__(self, valor):
        self.valor = valor

    def evaluar(self) -> int | float:
        return self.valor