from constantes import SIMBOLOS
import nodos

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.limite = len(tokens)
        self.pos = 0

    def advance(self):
        if self.pos < self.limite:
            token = self.tokens[self.pos]
            self.pos += 1
            return token
        return None

    def peek(self, pasos=0):
        if self.pos + pasos < self.limite:
            return self.tokens[self.pos + pasos]
        return None

    def match(self, tipo, pasos=0):
        token = self.peek(pasos)
        return token is not None and token.tipo == tipo 

    def consumir(self, tipo, mensaje_error):
        if self.match(tipo):
            return self.advance()
        raise Exception(mensaje_error) 

    def parsear(self) -> list:
        instrucciones = []
        
        if self.match("FIN"):
            raise Exception("Expresión vacia")
        
        instrucciones.append(self.expre())

        if self.peek() and not self.match("FIN"):
            raise Exception("Quedan tokens sin procesar")
    
        return  instrucciones
    
    def expre(self):
        self.consumir("LIS_IZQ", "La operación debe empezar con un [")
        operador = self.advance()
        if not operador.valor in SIMBOLOS:
            raise Exception("Esperaba un operador")
        nodo = nodos.NodoOperacion(operador.valor)

        while not self.match("LIS_DER"):
            nodo.hijos.append(self.factor())

        self.consumir("LIS_DER", "La operación debe terminar con un ]")
        return nodo
    
    def factor(self):
        if self.match("LIS_IZQ"):
            return self.expre()
        
        if self.match("NUMERO"):
            token = self.advance()
            return nodos.NodoNumero(token.valor)
        
        raise Exception("Esperaba un número")